#!/usr/bin/env node
// Installer CLI for LCS skills. Supports installing into remote target repo.
// Usage examples:
//  npx --yes ./scripts/claude-skills.js add-target https://github.com/owner/target-repo -s https://github.com/mdhb2/lean-coding-skills -y
//  npx --yes ./scripts/claude-skills.js add-target https://github.com/owner/target-repo -s local -y --push
//  npx --yes ./scripts/claude-skills.js install-local

const { execSync, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

function log(...args) { console.log(...args); }
function die(msg) { console.error(msg); process.exit(1); }

function copyRecursiveSync(src, dest, overwrite = true) {
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
    for (const name of fs.readdirSync(src)) {
      const s = path.join(src, name);
      const d = path.join(dest, name);
      copyRecursiveSync(s, d, overwrite);
    }
  } else {
    if (fs.existsSync(dest) && !overwrite) return;
    fs.copyFileSync(src, dest);
  }
}

function ensureClaudeSkillsDir(baseDir) {
  const target = path.join(baseDir, '.claude', 'skills');
  const legacy = path.join(baseDir, '.agents', 'skills');
  if (!fs.existsSync(target)) fs.mkdirSync(target, { recursive: true });
  // If legacy exists and target is empty, migrate automatically
  try {
    if (fs.existsSync(legacy) && fs.existsSync(target) && fs.readdirSync(target).length === 0) {
      copyRecursiveSync(legacy, target, true);
      log('Migrated skills from .agents/skills → .claude/skills');
    }
  } catch (e) {
    // non-fatal migration failure
  }
  return target;
}

function cloneRepo(url, tmpDir) {
  try {
    log('Cloning', url, 'to', tmpDir);
    execFileSync('git', ['clone', '--depth=1', url, tmpDir], { stdio: 'inherit' });
  } catch (err) {
    die('git clone failed. Ensure git is installed and URL is valid.');
  }
}

function gitCommitAndMaybePush(repoDir, message, doPush) {
  try {
    execFileSync('git', ['add', '.'], { cwd: repoDir, stdio: 'inherit' });
    try {
      execFileSync('git', ['commit', '-m', message], { cwd: repoDir, stdio: 'inherit' });
    } catch (e) {
      // nothing to commit is non-fatal
    }
    if (doPush) {
      execFileSync('git', ['push'], { cwd: repoDir, stdio: 'inherit' });
    }
  } catch (err) {
    die('git commit/push failed. Check credentials and remote access.');
  }
}

function installLocal() {
  const src = path.join(process.cwd(), 'skills');
  if (!fs.existsSync(src)) die('No skills/ folder in current directory.');
  const target = ensureClaudeSkillsDir(process.cwd());
  for (const name of fs.readdirSync(src)) {
    if (!fs.statSync(path.join(src, name)).isDirectory()) continue;
    const srcPath = path.join(src, name);
    const destPath = path.join(target, name);
    log('Copying', name, '->', destPath);
    copyRecursiveSync(srcPath, destPath, true);
  }
  log('Done. Skills copied to .claude/skills');
}

function addTargetCommand(targetRepoUrl, options) {
  if (!targetRepoUrl) die('missing target repo url. Usage: add-target <target-repo-url> [-s <source> | local] [-y] [--push]');
  const tmpTarget = fs.mkdtempSync(path.join(os.tmpdir(), 'claude-target-'));
  cloneRepo(targetRepoUrl, tmpTarget);
  // determine source
  let source = options.source;
  let sourceTmp = null;
  let sourcePath = null;
  if (!source || source === 'this') {
    // use this package's skills folder
    const repoRoot = path.resolve(__dirname, '..');
    const localSkills = path.join(repoRoot, 'skills');
    if (!fs.existsSync(localSkills)) die('This package has no skills/ folder to use as source.');
    sourcePath = localSkills;
  } else if (source === 'local') {
    // use CWD skills
    const localSkills = path.join(process.cwd(), 'skills');
    if (!fs.existsSync(localSkills)) die('No skills/ folder in current working directory.');
    sourcePath = localSkills;
  } else if (source.startsWith('http') || source.endsWith('.git')) {
    sourceTmp = fs.mkdtempSync(path.join(os.tmpdir(), 'claude-source-'));
    cloneRepo(source, sourceTmp);
    const possible = path.join(sourceTmp, 'skills');
    if (!fs.existsSync(possible)) die('Source repo has no skills/ folder.');
    sourcePath = possible;
  } else {
    die('Unsupported source argument. Use "this" (default), "local", or a git URL.');
  }

  // copy skills into target repo .claude/skills
  const targetClaudeSkills = ensureClaudeSkillsDir(tmpTarget);
  for (const name of fs.readdirSync(sourcePath)) {
    if (!fs.statSync(path.join(sourcePath, name)).isDirectory()) continue;
    const s = path.join(sourcePath, name);
    const d = path.join(targetClaudeSkills, name);
    log('Copying', name, '->', d);
    copyRecursiveSync(s, d, true);
  }

  const commitMsg = `chore: add lcs skills from ${options.source || 'this-package'}`;
  gitCommitAndMaybePush(tmpTarget, commitMsg, options.push);

  // cleanup source tmp if used
  if (sourceTmp) {
    try { fs.rmSync(sourceTmp, { recursive: true, force: true }); } catch (e) {}
  }

  log('Done. Skills installed into target repo at', tmpTarget);
  log('If you want changes pushed to remote, rerun with --push after verifying local clone.');
  log('To persist locally: copy .claude/skills from the temp dir into your workspace or run with --push to push to remote.');
}

function help() {
  console.log(`claude-skills installer

Usage:
  add-target <target-repo-url> [-s <source>|local|this] [-y] [--push]
    Clone target repo, copy skills into .claude/skills, commit. --push optionally pushes commit (requires credentials).

  install-local
    Copy local ./skills into .claude/skills in current working directory.

Examples:
  npx --yes ./scripts/claude-skills.js add-target https://github.com/owner/target-repo -s this -y
  npx --yes ./scripts/claude-skills.js add-target https://github.com/owner/target-repo -s https://github.com/mdhb2/lean-coding-skills -y --push
  npx --yes ./scripts/claude-skills.js install-local
`);
}

async function main() {
  const argv = process.argv.slice(2);
  if (argv.length === 0) return help();
  const cmd = argv[0];
  if (cmd === 'add-target') {
    const target = argv[1];
    const opts = {
      source: null,
      push: false,
      yes: argv.includes('-y') || argv.includes('--yes')
    };
    for (let i = 2; i < argv.length; i++) {
      const a = argv[i];
      if (a === '-s' || a === '--source') {
        opts.source = argv[++i];
      } else if (a === '--push') {
        opts.push = true;
      }
    }
    addTargetCommand(target, opts);
    return;
  }
  if (cmd === 'install-local') {
    installLocal();
    return;
  }
  help();
}

main();
