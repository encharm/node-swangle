async function buildBindings() {
  cp.execSync('node-gyp rebuild', (err) => {
    if (err) {
      throw new Error('node-gyp failed with: ' + err);
    }
  });
}

async function run() {
  // skip for now
  //await buildBindings();
}

run();
