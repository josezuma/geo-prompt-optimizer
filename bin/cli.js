#!/usr/bin/env node
const path = require('path');
const { spawnSync } = require('child_process');

const script = path.join(__dirname, '..', 'scripts', 'optimizer.py');
const args = process.argv.slice(2);

const result = spawnSync('python3', [script, ...args], {
  stdio: 'inherit',
  shell: false,
});

process.exit(result.status || 0);
