# Diffuse BSDF

## Diffuse BSDF

### Diffuse BSDF

Add Lambertian and Oren-Nayar diffuse reflection.

### Inputs

- **Color** - Surface color (physically: light reflection/transmission probability per wavelength).
- **Roughness** *(Cycles Only)* — Surface roughness. 0.0 gives Lambertian reflection; higher values activate Oren-Nayar.
- **Normal**: Shading normal. Defaults to standard shading normal when unconnected.

### Properties

None.

### Outputs

- **BSDF**: Standard shader output.

### Examples

Lambertian reflection. / Diffuse shader behavior. / Oren-Nayar reflection.

[Related references](INDEX.md).
