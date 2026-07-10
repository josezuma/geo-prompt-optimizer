#!/usr/bin/env node
const { execSync } = require('child_process');
const args = process.argv.slice(2);
execSync(`python3 ${__dirname}/../scripts/optimizer.py ${args.map(a => `"${a}"`).join(' ')}`, { stdio: 'inherit' });
