# Glass BSDF

## Glass BSDF

### Glass BSDF

Create glass-like shading by mixing refraction and reflection at grazing angles. Like transparent shaders, only pure white becomes transparent. Glass causes noise from caustics; combine with transparent shaders for shadows to improve results. See referenced details.

### Inputs

- **Color** - Surface color (physically: light transmission probability per wavelength).
- **Roughness**: Refraction sharpness. 0.0 is perfectly sharp; higher values smooth refraction.
- **IOR**: Index of refraction defining ray direction change. 1.0 passes rays straight (like transparent); higher values refract more.
- **Normal**: Shading normal.

### Thin Film *(Cycles Only)*

Simulate thin film interference effects that color specular reflection based on view angle, film thickness, and IOR of both film and material. Common in oil films, soap bubbles, and coatings. Affects transmission as well as reflections.

- **Thickness**: Film thickness in nanometers. 0 disables simulation. 100–1000 nm is strongest (visible light range).
- **IOR**: Film index of refraction (1.0–2.0 typical range). 1.33 approximates water. At 1.0 or matching main IOR, the film effect vanishes (optically blends in).

### Properties

**Distribution**: Microfacet model.

- **GGX**: GGX distribution.
- **Multiscatter GGX**: Accounts for multiple microfacet scattering. More energy-conservative; prevents excessive darkening.
- **Beckmann** *(Cycles Only)* — Beckmann distribution.

### Outputs

- **BSDF**: Standard shader output.

### Examples

Sharp Glass example. / Sharp Glass behavior. / Rough Glass example. / Rough Glass behavior.

[Related references](INDEX.md).
