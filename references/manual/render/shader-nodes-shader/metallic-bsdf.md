# Metallic BSDF

## Metallic BSDF

### Metallic BSDF

Recreate metal appearance.

### Inputs

### F82 Tint

- **Base Color** — Material color at normal viewing angle.
- **Edge Tint** — Material color at 82° viewing angle.

### Physical Conductor

- **IOR** — Refractive index per channel (real part of complex IOR, denoted n).
- **Extinction** — Extinction coefficients per channel (imaginary part, denoted k).

### Common

- **Roughness** — Reflection sharpness. 0.0 = perfectly sharp; higher = smoother.
- **Anisotropy** *(Cycles Only)* — Anisotropy amount. Higher = elongated highlights along tangent; negative = perpendicular highlights.
- **Rotation** *(Cycles Only)* — Anisotropy direction rotation (1.0 = full circle). Note: 90° offset vs Glossy BSDF; add 0.25 to correct.
- **Normal** — Shading normal. Defaults to standard when unconnected.
- **Tangent** — Shading tangent. Defaults to standard when unconnected.

### Properties

**Distribution** — Microfacet model.

- **GGX** — GGX distribution.
- **Multiscatter GGX** — Multiple microfacet scattering; more energy-conservative.
- **Beckmann** *(Cycles Only)* — Beckmann distribution.

**Fresnel Type** — Models for material appearance via color or physical IOR.

- **F82 Tint** — Adobe F82-Tint formula for edge color via complex IOR simulation.
- **Physical Conductor** — Complex IOR from real-world metals. Sources: Physically Based database and Refractive Index nk database.

### Outputs

- **BSDF** — Standard shader output.

### Examples

### F82 Tint

| Material | Titanium (Default) | Aluminum | Copper | Gold |
| --- | --- | --- | --- | --- |
| Base Color | 0.617, 0.576, 0.540 | 0.911, 0.912, 0.917 | 0.972, 0.694, 0.486 | 1.000, 0.735, 0.353 |
| Edge Tint | 0.695, 0.726, 0.770 | 0.848, 0.877, 0.916 | 0.961, 0.969, 0.942 | 0.993, 1.000, 1.000 |

### Physical Conductor

| Material | Titanium (Default) | Aluminum | Copper | Gold |
| --- | --- | --- | --- | --- |
| IOR | 2.757, 2.512, 2.231 | 1.333, 0.945, 0.582 | 0.235, 0.729, 1.369 | 0.000, 0.470, 1.439 |
| Extinction | 3.867, 3.404, 3.009 | 7.434, 6.340, 5.181 | 5.666, 2.562, 2.227 | 182.6, 2.189, 1.660 |

[Related references](INDEX.md).
