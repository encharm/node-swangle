const { execSync } = require('child_process');
const os = require('os');

async function run() {
  const arch = `${os.platform()}-${os.arch().toLowerCase()}`;
  try {
    await execSync('node-gyp rebuild');
    if (arch === 'darwin-arm64') {
      await execSync('install_name_tool -change ./libGLESv2.dylib @rpath/libGLESv2.dylib build/Release/nodejs_gl_binding_darwin_arm64.node');
      await execSync('install_name_tool -change ./libEGL.dylib @rpath/libEGL.dylib build/Release/nodejs_gl_binding_darwin_arm64.node');
    }
  } catch (e) {
    console.error(e);
  }
}

run();
