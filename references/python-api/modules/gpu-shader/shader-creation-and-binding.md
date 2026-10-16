# gpu.shader creation and binding

gpu.shader. create_from_info ( shader_info )

Build a shader out of a GPUShaderCreateInfo.

Parameters :

shader_info (gpu.types.GPUShaderCreateInfo) – GPUShaderCreateInfo

Returns :

Shader object corresponding to the given shader info.

Return type :

gpu.types.GPUShader

gpu.shader. from_builtin ( shader_name , * , config = 'DEFAULT' )

These are the shaders baked into Blender's own code (refer to Built-in shaders).
Each of them reads the uniform mat4 ModelViewProjectionMatrix ,
which you can adjust through the gpu.matrix module.

A shader configuration relying on clip_planes is also selectable: pass CLIPPED as the config parameter. Be aware that doing so means you must also set the value of mat4 ModelMatrix by hand.

Parameters :

- shader_name ( str ) – One of the builtin shader names.

- config ( str ) – One of these types of shader configuration:

- DEFAULT

- CLIPPED

Returns :

Shader object corresponding to the given name.

Return type :

gpu.types.GPUShader

gpu.shader. unbind ( )

Release the currently bound shader object.

[Related references](INDEX.md).
