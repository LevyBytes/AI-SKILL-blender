# Fresnel Node

## Fresnel Node

### Fresnel Node

Calculate how much light reflects off a layer versus passing through. The output weight suits layering shaders via Mix Shader nodes. Reflection amount depends on the angle between surface normal and viewing direction.

Common use: Mix two BSDFs with Fresnel as the blending factor. For glass, mix between glossy refraction and reflection. At grazing angles, more light reflects than refracts, as in the physical world.

Two-layer materials work similarly: place a glossy coating over a diffuse base and mix them with Fresnel. This specifies that refracted light through the coating hits the diffuse layer and bounces.

### Inputs

- **IOR** — Index of refraction of the material being entered.
- **Normal** — Bump or normal map input to affect the output.

### Properties

None.

### Outputs

- **Factor** — Fresnel weight indicating the probability light reflects versus transmitting through.

[Related references](INDEX.md).
