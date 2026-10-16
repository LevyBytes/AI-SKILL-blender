# Light Path Node

## Light Path Node

### Light Path Node

Identify the incoming ray type for which the shader is executing. Useful for non-physically-based tricks. See Light Paths documentation for ray type meanings.

### Inputs

None.

### Properties

None.

### Outputs

- **Is Camera Ray** — 1.0 for camera rays, 0.0 otherwise.
- **Is Shadow Ray** — 1.0 for shadow rays, 0.0 otherwise.
- **Is Diffuse Ray** — 1.0 for diffuse rays, 0.0 otherwise.
- **Is Glossy Ray** — 1.0 for glossy rays, 0.0 otherwise.
- **Is Singular Ray** *(Cycles Only)* — 1.0 for singular rays, 0.0 otherwise.
- **Is Reflection Ray** *(Cycles Only)* — 1.0 for reflection rays, 0.0 otherwise.
- **Is Transmission Ray** *(Cycles Only)* — 1.0 for transmission rays, 0.0 otherwise.
- **Is Volume Scatter Ray** *(Cycles Only)* — 1.0 for volume scatter rays, 0.0 otherwise.
- **Ray Length** *(Cycles Only)* — Distance the light ray traveled since last bounce or camera.
- **Ray Depth** — Number of surface bounces (reflections/transmissions). Note: Transparent shaders don't count as normal bounces.
- **Diffuse Depth** *(Cycles Only)* — Count of diffuse reflections/transmissions.
- **Glossy Depth** *(Cycles Only)* — Count of glossy reflections/transmissions.
- **Transparent Depth** *(Cycles Only)* — Count of transparent surface passes.
- **Transmission Depth** *(Cycles Only)* — Count of transmissive surface passes. Typical use: avoid render artifacts (black spots from bounce limits) by switching from transmissive to diffuse past a threshold. See Mix Shader.
- **Portal Depth** *(Cycles Only)* — Count of Ray Portal BSDF passes.

### EEVEE Support

EEVEE has no true ray concept, but outputs some ray-path controls for Cycles compatibility:

- **Is Camera** — Supported.
- **Is Shadow** — Supported.
- **Is Diffuse** — Supported.
- **Is Glossy** — Supported.
- **Is Singular** — Not supported (same as Is Glossy).
- **Is Reflection** — Not supported (same as Is Glossy).
- **Is Transmission** — Not supported (same as Is Glossy).
- **Ray Length** — Distance from camera to shading point.
- **Ray Depth** — Current light-cache baking bounce.
- **Diffuse Depth** — Same as Ray Depth during diffuse baking.
- **Glossy Depth** — Same as Ray Depth during specular baking.
- **Transparent Depth** — Not supported (defaults to 0).
- **Transmission Depth** — Not supported (same as Glossy Depth).

Note: Is Glossy doesn't work with Screen Space Reflections/Refractions but works with reflection planes (with or without SSR).

[Related references](INDEX.md).
