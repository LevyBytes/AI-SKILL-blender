# gpu.shader: uniform and polyline shaders

`UNIFORM_COLOR`

Attributes :

vec3 pos

Uniforms :

vec4 color

`POLYLINE_FLAT_COLOR`

Attributes :

vec3 pos, vec4 color

Uniforms :

vec2 viewportSize, float lineWidth

`POLYLINE_SMOOTH_COLOR`

Attributes :

vec3 pos, vec4 color

Uniforms :

vec2 viewportSize, float lineWidth

`POLYLINE_UNIFORM_COLOR`

Attributes :

vec3 pos

Uniforms :

vec2 viewportSize, float lineWidth, vec4 color

`POINT_FLAT_COLOR`

Attributes :

vec3 pos, vec4 color

Uniforms :

float size

`POINT_UNIFORM_COLOR`

Attributes :

vec3 pos

Uniforms :

vec4 color, float size

[Related references](INDEX.md).
