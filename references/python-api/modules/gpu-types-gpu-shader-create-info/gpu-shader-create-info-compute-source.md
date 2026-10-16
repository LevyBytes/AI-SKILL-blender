# gpu.types.GPUShaderCreateInfo: compute_source ( source )

compute_source ( source )

compute shader source code written in GLSL.

Example:

```text
"""void main() {
int2 index = int2(gl_GlobalInvocationID.xy);
vec4 color = vec4(0.0, 0.0, 0.0, 1.0);
imageStore(img_output, index, color);
}"""
```

Parameters :

source ( str ) – The compute shader source code.

See also

GLSL Cross Compilation

[Related references](INDEX.md).
