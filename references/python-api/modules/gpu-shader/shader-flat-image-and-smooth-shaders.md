# gpu.shader: flat image and smooth shaders

## GPU Shader Utilities (gpu.shader)

### GPU Shader Utilities (gpu.shader)

This module opens up the internal functions of GPUShader.

Built-in shaders

A mat4 ModelViewProjectionMatrix uniform is present on every built-in shader.

You change its value through the gpu.matrix module.

Important

Be sure to set shader uniforms explicitly so that leftover values from earlier runs are not carried over.

`FLAT_COLOR`

Attributes :

vec3 pos, vec4 color

Uniforms :

none

IMAGE

Attributes :

vec3 pos, vec2 texCoord

Uniforms :

sampler2D image

`IMAGE_SCENE_LINEAR_TO_REC709_SRGB`

Attributes :

vec3 pos, vec2 texCoord

Uniforms :

sampler2D image

Note :

Expect texture to be in scene linear color space

`IMAGE_COLOR`

Attributes :

vec3 pos, vec2 texCoord

Uniforms :

sampler2D image, vec4 color

`IMAGE_COLOR_SCENE_LINEAR_TO_REC709_SRGB`

Attributes :

vec3 pos, vec2 texCoord

Uniforms :

sampler2D image, vec4 color

Note :

Expect texture to be in scene linear color space

`SMOOTH_COLOR`

Attributes :

vec3 pos, vec4 color

Uniforms :

none

[Related references](INDEX.md).
