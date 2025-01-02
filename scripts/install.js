const { execSync } = require('child_process');
const os = require('os');

const arch = `${os.platform()}-${os.arch().toLowerCase()}`;
console.log('install ', arch)

if (arch === 'darwin-arm64') {
  execSync('install_name_tool -change ./libGLESv2.dylib @rpath/libGLESv2.dylib build/Release/nodejs_gl_binding_darwin_arm64.node');
  execSync('install_name_tool -change ./libEGL.dylib @rpath/libEGL.dylib build/Release/nodejs_gl_binding_darwin_arm64.node');
}
