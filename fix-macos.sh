install_name_tool -change ./libGLESv2.dylib @rpath/libGLESv2.dylib build/Release/nodejs_gl_binding_darwin_arm64.node
install_name_tool -change ./libEGL.dylib @rpath/libEGL.dylib build/Release/nodejs_gl_binding_darwin_arm64.node
