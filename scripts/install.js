const { execSync } = require('child_process');

async function run() {
  try {
    await execSync('node-gyp rebuild');
  } catch (e) {
    console.error(e);
  }
}

run();
