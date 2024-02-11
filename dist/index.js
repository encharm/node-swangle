"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.createWebGLRenderingContext = void 0;
var bindings = require("bindings");
var binding = bindings("nodejs_gl_binding_" + process.platform + "_" + process.arch);
;
var createWebGLRenderingContext = function (args) {
    if (args === void 0) { args = {}; }
    var width = args.width || 1;
    var height = args.height || 1;
    var webGLCompability = args.webGLCompability || false;
    var majorVersion = args.majorVersion || 3;
    var minorVersion = args.minorVersion || 0;
    return binding.createWebGLRenderingContext(width, height, majorVersion, minorVersion, webGLCompability);
};
exports.createWebGLRenderingContext = createWebGLRenderingContext;
//# sourceMappingURL=index.js.map