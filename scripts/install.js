const { execSync } = require('child_process');

async function run() {
  await execSync('node-gyp rebuild');
}

run();
