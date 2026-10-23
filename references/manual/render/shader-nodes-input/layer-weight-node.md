# Layer Weight Node

## Layer Weight Node

### Layer Weight Node

Output a weight for shader layering with Mix Shader nodes.

### Inputs

- **Blend**: Bias output toward 0 or 1 for uneven shader mixing.
- **Normal**: Bump or normal map to affect output.

### Properties

None.

### Outputs

- **Fresnel**: Dielectric Fresnel weight for layering diffuse and glossy (e.g., plastic materials). Like the Fresnel node but in the 0.0–1.0 range for convenience.
- **Facing**: Weight blending from first to second shader as surface orientation shifts from viewer-facing to grazing.

[Related references](INDEX.md).
