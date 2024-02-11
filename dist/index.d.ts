interface ContextArguments {
    width?: number;
    height?: number;
    webGLCompability?: boolean;
    majorVersion?: number;
    minorVersion?: number;
}
declare const createWebGLRenderingContext: (args?: ContextArguments) => WebGLRenderingContext | WebGL2RenderingContext;
export { createWebGLRenderingContext };
