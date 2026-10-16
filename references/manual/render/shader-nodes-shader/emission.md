# Emission

## Emission

### Emission

Add Lambertian emission for materials and light surfaces.

Light units: Point, spot, and area lights use Watts. Sun lights use Watts/m², requiring smaller values (e.g., 1 W/m²)—specifying Watts would be impractical (the sun is ~384.6×10²⁴ W). Mesh emissions also use Watts/m².

### Inputs

- **Color** — Emitted light color.
- **Strength** — Emitted light strength. For point/area lights: Watts. For materials: 1.0 makes the object display its exact Color input (shadeless).

### Properties

None.

### Outputs

- **Emission** — Can connect to Surface or Volume Input of Material Output node.

### Examples

Emission at strength 1.0. / Emission at strength 3.0.

[Related references](INDEX.md).
