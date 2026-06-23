#!/usr/bin/env node
// LCS Skills Validation Script
// Checks structural integrity and Chain of Truth compliance across all skills.
// No runtime dependencies beyond Node.js built-ins.

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SKILLS_DIR = path.join(ROOT, 'skills');
const CONTRACT_PATH = path.join(SKILLS_DIR, 'lcs-shared', 'contract.md');
const README_PATH = path.join(ROOT, 'README.md');
const COT_SKILL_PATH = path.join(SKILLS_DIR, 'lcs-chain-of-truth', 'SKILL.md');
const PACKAGE_PATH = path.join(ROOT, 'package.json');

// Canonical level mapping sourced from contract.md
// Update this table when contract.md changes.
const CANONICAL_LEVELS = {
  'lcs-explore':         'Light',
  'lcs-toprd':           'Standard',
  'lcs-onboarding':      'Standard',
  'lcs-debug':           'Standard',
  'lcs-self-improvement':'Standard',
  'lcs-prd-reviewer':    'Strict',
  'lcs-tosrs':           'Strict',
  'lcs-task-slicer':     'Strict',
  'lcs-doc-finalizer':   'Strict',
  'lcs-codebase-doc':    'Strict',
  'lcs-debug-ext':       'Very Strict',
  'lcs-task-executor':   'Very Strict',
  'lcs-task-executer':   'Very Strict',
  'lcs-chain-of-truth':  'Meta',
  'lcs-shared':          'Meta',
};

const VALID_LEVELS = new Set(['Light', 'Standard', 'Strict', 'Very Strict', 'Meta']);
const CANONICAL_EXECUTOR = 'lcs-task-executor';
const LEGACY_EXECUTOR    = 'lcs-task-executer';
const MINIMAL_SKILL_FILES = new Set(['lcs-shared']);
const WORK_ITEMS_CORRUPTED = '.lcs/work-items/' + '-/';
const DOCS_CORRUPTED = '.lcs/docs/' + '-/';
const ARCHIVE_CORRUPTED = '.lcs/archive/' + '-/';
const ANALYSIS_CORRUPTED = '-' + 'analysis.md';
const CORRUPTED_PLACEHOLDERS = [
  WORK_ITEMS_CORRUPTED,
  DOCS_CORRUPTED,
  ARCHIVE_CORRUPTED,
];
const SCANNED_EXTENSIONS = new Set(['.md', '.js', '.json', '.py', '.ps1']);
const SKIPPED_DIRS = new Set(['.git', 'node_modules']);

let errors = [];
let warnings = [];
let passed = 0;

function fail(msg)  { errors.push('  FAIL: ' + msg); }
function warn(msg)  { warnings.push('  WARN: ' + msg); }
function pass(msg)  { passed++; process.stdout.write('  PASS: ' + msg + '\n'); }

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function readFile(filePath) {
  if (!fs.existsSync(filePath)) return null;
  return fs.readFileSync(filePath, 'utf8');
}

function walkFiles(dir, out = []) {
  if (!fs.existsSync(dir)) return out;
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (!SKIPPED_DIRS.has(name)) walkFiles(full, out);
    } else if (SCANNED_EXTENSIONS.has(path.extname(name))) {
      out.push(full);
    }
  }
  return out;
}

function rel(filePath) {
  return path.relative(ROOT, filePath).replace(/\\/g, '/');
}

/** Parse YAML frontmatter block between opening and closing --- */
function parseFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return null;
  const block = match[1];
  const result = {};
  // Only capture non-indented key: value lines (top-level scalar fields).
  // Skips indented continuation lines from block scalars (description: |).
  for (const rawLine of block.split('\n')) {
    const line = rawLine.replace(/\r$/, '');
    const m = line.match(/^([a-zA-Z]\w*):\s*(.*)$/);
    if (m) result[m[1].trim()] = m[2].trim();
  }
  return result;
}

/** Extract the declared Chain of Truth level from SKILL.md body */
function extractCoTLevel(content) {
  // Match "## Chain of Truth Level\n\nLevel: <value>" (with optional blank lines)
  const m = content.match(/##\s+Chain of Truth Level[\s\S]*?Level:\s*([^\n\r]+)/);
  if (!m) return null;
  return m[1].trim();
}

/** Check that "## Chain of Truth Report" appears before "## Handoff" in text */
function cotReportBeforeHandoff(content) {
  const cotMatch = content.match(/^## Chain of Truth Report\s*$/m);
  const handoffMatch = content.match(/^## Handoff\s*$/m);
  const cotIdx = cotMatch ? cotMatch.index : -1;
  const handoffIdx = handoffMatch ? handoffMatch.index : -1;
  if (cotIdx === -1) return { hasCot: false, handoffExists: handoffIdx !== -1 };
  return { hasCot: true, handoffExists: handoffIdx !== -1, before: cotIdx < handoffIdx };
}

// ---------------------------------------------------------------------------
// Check 1 — every skill folder has a valid SKILL.md with frontmatter
// Check 2 — folder name matches `name` field
// Check 3 — exactly one Chain of Truth Level declared, value valid
// Check 4 — declared level matches canonical mapping
// Check 5 — ## Chain of Truth Report appears before ## Handoff
// ---------------------------------------------------------------------------

function checkSkills() {
  const entries = fs.readdirSync(SKILLS_DIR);
  const skillFolders = entries.filter(e => {
    const full = path.join(SKILLS_DIR, e);
    return fs.statSync(full).isDirectory();
  });

  for (const folder of skillFolders) {
    const skillMdPath = path.join(SKILLS_DIR, folder, 'SKILL.md');

    // Check 1 — SKILL.md exists
    if (!fs.existsSync(skillMdPath)) {
      fail(`[${folder}] missing SKILL.md`);
      continue;
    }

    const content = fs.readFileSync(skillMdPath, 'utf8');
    const lineCount = content.split(/\r?\n/).length;

    if (content.startsWith('--- name:')) {
      fail(`[${folder}] SKILL.md starts with collapsed frontmatter ('--- name:')`);
      continue;
    }

    if (!content.startsWith('---\n') && !content.startsWith('---\r\n')) {
      fail(`[${folder}] SKILL.md must start with standalone YAML delimiter followed by newline`);
      continue;
    }

    if (lineCount < 20 && !MINIMAL_SKILL_FILES.has(folder)) {
      fail(`[${folder}] SKILL.md has suspiciously low line count (${lineCount}); possible newline collapse`);
    }

    const fm = parseFrontmatter(content);

    // Check 1b — valid frontmatter
    if (!fm) {
      fail(`[${folder}] SKILL.md has no valid YAML frontmatter`);
      continue;
    }
    if (!fm.name) {
      fail(`[${folder}] SKILL.md frontmatter missing 'name' field`);
      continue;
    }
    if (!fm.description) {
      warn(`[${folder}] SKILL.md frontmatter missing 'description' field`);
    }
    pass(`[${folder}] SKILL.md exists with valid frontmatter`);

    // Check 2 — folder name matches name field
    if (fm.name !== folder) {
      fail(`[${folder}] folder name '${folder}' != frontmatter name '${fm.name}'`);
    } else {
      pass(`[${folder}] folder name matches frontmatter name`);
    }

    // Check 3 — exactly one CoT Level declaration
    const allCoT = [...content.matchAll(/##\s+Chain of Truth Level[\s\S]*?Level:\s*([^\n\r]+)/g)];
    if (allCoT.length === 0) {
      fail(`[${folder}] no '## Chain of Truth Level' declaration found`);
    } else if (allCoT.length > 1) {
      fail(`[${folder}] multiple '## Chain of Truth Level' declarations found (${allCoT.length})`);
    } else {
      const levelVal = allCoT[0][1].trim();
      // Normalize "Very Strict (4)" -> "Very Strict" etc.
      const normalized = levelVal.replace(/\s*\(\d+\)/, '').trim();
      if (!VALID_LEVELS.has(normalized)) {
        fail(`[${folder}] declared level '${levelVal}' is not a valid level (Light/Standard/Strict/Very Strict/Meta)`);
      } else {
        pass(`[${folder}] Chain of Truth Level declared: ${normalized}`);

        // Check 4 — matches canonical mapping
        if (folder in CANONICAL_LEVELS) {
          const expected = CANONICAL_LEVELS[folder];
          if (normalized !== expected) {
            fail(`[${folder}] level mismatch: SKILL.md says '${normalized}', canonical mapping says '${expected}'`);
          } else {
            pass(`[${folder}] level matches canonical mapping (${expected})`);
          }
        } else {
          warn(`[${folder}] not in canonical mapping — add to CANONICAL_LEVELS in this script and contract.md`);
        }
      }
    }

    // Check 5 — ## Chain of Truth Report before ## Handoff
    // lcs-chain-of-truth is a meta-protocol; it intentionally has no self-applied CoT Report.
    // lcs-shared has no Handoff — skip.
    const skipCotReportCheck = new Set(['lcs-chain-of-truth', 'lcs-shared']);
    if (!skipCotReportCheck.has(folder)) {
      const { hasCot, handoffExists, before } = cotReportBeforeHandoff(content);
      if (!handoffExists) {
        warn(`[${folder}] no '## Handoff' section found — cannot verify CoT Report placement`);
      } else if (!hasCot) {
        fail(`[${folder}] '## Chain of Truth Report' missing; must appear before '## Handoff'`);
      } else if (!before) {
        fail(`[${folder}] '## Chain of Truth Report' appears AFTER '## Handoff' — must come before`);
      } else {
        pass(`[${folder}] ## Chain of Truth Report appears before ## Handoff`);
      }
    }
  }
}

// ---------------------------------------------------------------------------
// Check 6 — repo-wide corruption and collapse guards
// ---------------------------------------------------------------------------

function checkRepoCorruption() {
  for (const filePath of walkFiles(ROOT)) {
    const content = readFile(filePath) || '';
    const relative = rel(filePath);

    for (const placeholder of CORRUPTED_PLACEHOLDERS) {
      if (content.includes(placeholder)) {
        fail(`${relative} contains corrupted placeholder '${placeholder}'`);
      }
    }

    const analysisPattern = new RegExp('(^|[^A-Za-z0-9}])' + ANALYSIS_CORRUPTED.replace('.', '\\.'));
    if (analysisPattern.test(content)) {
      fail(`${relative} contains corrupted placeholder '${ANALYSIS_CORRUPTED}'`);
    }

    if (path.basename(filePath) === 'SKILL.md' && content.startsWith('--- name:')) {
      fail(`${relative} starts with collapsed frontmatter ('--- name:')`);
    }

    if (path.extname(filePath) === '.js' && content.startsWith('#!/usr/bin/env node //')) {
      fail(`${relative} has collapsed Node shebang comment`);
    }
  }
}

// ---------------------------------------------------------------------------
// Check 7 — package.json test script runs validator
// ---------------------------------------------------------------------------

function checkPackageTestScript() {
  const raw = readFile(PACKAGE_PATH);
  if (!raw) {
    fail('package.json missing');
    return;
  }

  let pkg;
  try {
    pkg = JSON.parse(raw);
  } catch (err) {
    fail(`package.json is not valid JSON: ${err.message}`);
    return;
  }

  const testScript = pkg.scripts && pkg.scripts.test;
  if (!testScript || !testScript.includes('scripts/validate-skills.js')) {
    fail('package.json test script must run scripts/validate-skills.js');
  } else {
    pass('package.json test script runs scripts/validate-skills.js');
  }
}

// ---------------------------------------------------------------------------
// Check 8 — canonical executor lcs-task-executor exists
// Check 9 — legacy lcs-task-executer still exists
// ---------------------------------------------------------------------------

function checkExecutors() {
  const canonicalPath = path.join(SKILLS_DIR, CANONICAL_EXECUTOR, 'SKILL.md');
  if (!fs.existsSync(canonicalPath)) {
    fail(`canonical executor '${CANONICAL_EXECUTOR}' missing SKILL.md`);
  } else {
    const fm = parseFrontmatter(fs.readFileSync(canonicalPath, 'utf8'));
    if (!fm || fm.name !== CANONICAL_EXECUTOR) {
      fail(`canonical executor SKILL.md name mismatch: expected '${CANONICAL_EXECUTOR}', got '${fm && fm.name}'`);
    } else {
      pass(`canonical executor '${CANONICAL_EXECUTOR}' exists with correct name`);
    }
  }

  const legacyPath = path.join(SKILLS_DIR, LEGACY_EXECUTOR, 'SKILL.md');
  if (!fs.existsSync(legacyPath)) {
    fail(`legacy executor '${LEGACY_EXECUTOR}' missing — must not be removed (backward compat)`);
  } else {
    const fm = parseFrontmatter(fs.readFileSync(legacyPath, 'utf8'));
    if (!fm || fm.name !== LEGACY_EXECUTOR) {
      fail(`legacy executor SKILL.md name mismatch: expected '${LEGACY_EXECUTOR}', got '${fm && fm.name}'`);
    } else {
      pass(`legacy executor '${LEGACY_EXECUTOR}' still exists with correct name`);
    }
  }
}

// ---------------------------------------------------------------------------
// Check 10 — cross-document level consistency spot-check
// Verifies that README.md, contract.md, and lcs-chain-of-truth/SKILL.md all
// mention the same set of key skills at the same levels.
// ---------------------------------------------------------------------------

const SPOT_CHECK = [
  { skill: 'lcs-explore',       level: 'Light' },
  { skill: 'lcs-debug',         level: 'Standard' },
  { skill: 'lcs-debug-ext',     level: 'Very Strict' },
  { skill: 'lcs-task-executor', level: 'Very Strict' },
  { skill: 'lcs-task-executer', level: 'Very Strict' },
  { skill: 'lcs-codebase-doc',  level: 'Strict' },
];

function checkCrossDocConsistency() {
  const readme  = readFile(README_PATH)  || '';
  const contract = readFile(CONTRACT_PATH) || '';
  const cotSkill = readFile(COT_SKILL_PATH) || '';

  if (!readme)   { warn('README.md not found — skipping cross-doc consistency check'); return; }
  if (!contract) { warn('contract.md not found — skipping cross-doc consistency check'); return; }
  if (!cotSkill) { warn('lcs-chain-of-truth/SKILL.md not found — skipping cross-doc consistency check'); return; }

  for (const { skill, level } of SPOT_CHECK) {
    // README level summary table: "| Very Strict | lcs-task-executor, ..."
    // contract.md canonical table: "| Very Strict | lcs-task-executor, ..."
    // lcs-chain-of-truth SKILL.md mapping table: "| `lcs-task-executor` | Very Strict (4) | ..."
    const readmeOk   = readme.includes(skill) && readme.includes(level);
    const contractOk = contract.includes(skill) && contract.includes(level);
    const cotSkillOk = cotSkill.includes(skill) && cotSkill.includes(level);

    if (!readmeOk) {
      fail(`cross-doc: README.md does not associate '${skill}' with level '${level}'`);
    }
    if (!contractOk) {
      fail(`cross-doc: contract.md does not associate '${skill}' with level '${level}'`);
    }
    if (!cotSkillOk) {
      fail(`cross-doc: lcs-chain-of-truth/SKILL.md does not associate '${skill}' with level '${level}'`);
    }
    if (readmeOk && contractOk && cotSkillOk) {
      pass(`cross-doc: '${skill}' → ${level} consistent across README, contract, lcs-chain-of-truth`);
    }
  }
}

// ---------------------------------------------------------------------------
// Run all checks
// ---------------------------------------------------------------------------

console.log('\n=== LCS Skills Validator ===\n');

console.log('--- Skill structure checks ---');
checkSkills();

console.log('\n--- Repository corruption checks ---');
checkRepoCorruption();

console.log('\n--- package.json checks ---');
checkPackageTestScript();

console.log('\n--- Executor checks ---');
checkExecutors();

console.log('\n--- Cross-document consistency ---');
checkCrossDocConsistency();

// ---------------------------------------------------------------------------
// Summary
// ---------------------------------------------------------------------------

console.log('\n=== Summary ===');
console.log(`Passed:   ${passed}`);
console.log(`Warnings: ${warnings.length}`);
console.log(`Errors:   ${errors.length}`);

if (warnings.length > 0) {
  console.log('\nWarnings:');
  warnings.forEach(w => console.log(w));
}

if (errors.length > 0) {
  console.log('\nErrors:');
  errors.forEach(e => console.log(e));
  console.log('\nValidation FAILED.\n');
  process.exit(1);
} else {
  console.log('\nValidation PASSED.\n');
}
