# Glossy BSDF

## Glossy BSDF

### Glossy BSDF

Add microfacet-based reflection for metal and mirror-like surfaces.

### Inputs

- **Color** — Surface color (physically: light reflection probability per wavelength).
- **Roughness** — Reflection sharpness. 0.0 is perfectly sharp; higher values smooth reflection.
- **Anisotropy** *(Cycles Only)* — Stretch reflection along surface tangent. 0.0 = isotropic; higher values = elongated highlights perpendicular to tangent; negative values = highlights along tangent. Seen in metallic materials.
- **Rotation** — Rotate anisotropic tangent direction. 0.0 = 0°, 0.25 = 90°, 1.0 = 360°. Can be textured.
- **Normal** — Shading normal. Defaults to standard shading normal when unconnected.
- **Tangent** — Shading tangent. Defaults to standard shading tangent when unconnected.

### Properties

**Distribution** — Microfacet model.

- **GGX** — GGX distribution.
- **Multiscatter GGX** — Accounts for multiple microfacet scattering. More energy-conservative; prevents excessive darkening.
- **Beckmann** *(Cycles Only)* — Beckmann distribution.

### Outputs

- **BSDF** — Standard shader output.

### Examples

Sharp Glossy example. / Sharp Glossy behavior. / Rough Glossy example. / Rough Glossy behavior. / Anisotropic shading at 0°, 90°, and textured tangent rotation. Example blend-file.

[Related references](INDEX.md).
