#!/usr/bin/env node
// Small installer CLI for LCS skills to make them runnable via npx
// Usage (local): npx --yes ./scripts/claude-skills.js add <git-url> [-y]

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

function log(...args) { console.log(...args); }
function die(msg) { console.error(msg); process.exit(1); }

function copyRecursiveSync(src, dest) {
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
    for (const name of fs.readdirSync(src)) {
      copyRecursiveSync(path.join(src, name), path.join(dest, name));
    }
  } else {
    fs.copyFileSync(src, dest);
  }
}

function ensureAgentsDir() {
  const target = path.join(process.cwd(), '.agents', 'skills');
  if (!fs.existsSync(target)) fs.mkdirSync(target, { recursive: true });
  return target;
}

function cloneRepo(url, tmpDir) {
  try {
    log('Cloning', url, 'to', tmpDir);
    execSync(`git clone --depth=1 ${url} "${tmpDir}"`, { stdio: 'inherit' });
  } catch (err) {
    die('git clone failed. Ensure git is installed and URL is valid.');
  }
}

function addCommand(url, yes) {
  if (!url) die('missing git url. Usage: add <git-url> [-y]');
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'claude-skills-'));
  cloneRepo(url, tmp);
  const skillsSrc = path.join(tmp, 'skills');
  if (!fs.existsSync(skillsSrc)) die('No skills/ folder found in repo root.');
  const target = ensureAgentsDir();
  for (const name of fs.readdirSync(skillsSrc)) {
    const srcPath = path.join(skillsSrc, name);
    const destPath = path.join(target, name);
    log('Copying', name, '->', destPath);
    copyRecursiveSync(srcPath, destPath);
  }
  // cleanup
  try { fs.rmSync(tmp, { recursive: true, force: true }); } catch (e) {}
  log('Done. Skills installed to .agents/skills');
  if (!yes) log('Run: git add .agents/skills && git commit -m "chore: add skills" to persist changes');
}

function installLocal() {
  const src = path.join(process.cwd(), 'skills');
  if (!fs.existsSync(src)) die('No skills/ folder in current directory.');
  const target = ensureAgentsDir();
  for (const name of fs.readdirSync(src)) {
    const srcPath = path.join(src, name);
    const destPath = path.join(target, name);
    log('Copying', name, '->', destPath);
    copyRecursiveSync(srcPath, destPath);
  }
  log('Done. Skills copied to .agents/skills');
}

function updateCommand(url, yes) {
  // same as add for now (overwrite)
  addCommand(url, yes);
}

function help() {
  console.log(`claude-skills installer

Usage:
  add <git-url> [-y]      Clone repo and copy skills/* into .agents/skills/
  update <git-url> [-y]   Same as add (overwrite)
  install-local            Copy local ./skills into .agents/skills/

Examples:
  npx --yes ./scripts/claude-skills.js add https://github.com/mdhb2/lean-coding-skills -y
  npx --yes ./scripts/claude-skills.js install-local
`);
}

async function main() {
  const argv = process.argv.slice(2);
  if (argv.length === 0) return help();
  const cmd = argv[0];
  if (cmd === 'add') {
    const url = argv[1];
    const yes = argv.includes('-y') || argv.includes('--yes');
    addCommand(url, yes);
    return;
  }
  if (cmd === 'update') {
    const url = argv[1];
    const yes = argv.includes('-y') || argv.includes('--yes');
    updateCommand(url, yes);
    return;
  }
  if (cmd === 'install-local') {
    installLocal();
    return;
  }
  help();
}

main();
