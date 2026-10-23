# Mix Shader

## Mix Shader

### Mix Shader

Combine two shaders via blending. Useful for layering, where Factor input (e.g., Blend Weight node) controls mixing.

### Inputs

- **Shader**: Shaders to mix. Incoming rays strike either with the specified Factor probability.
- **Factor**: Blend weight. 0 = first shader; 1 = second shader.

### Properties

None.

### Outputs

- **Shader**: Standard shader output.

### Examples

Glossy and diffuse shader mix creates a ceramic material.

[Related references](INDEX.md).
