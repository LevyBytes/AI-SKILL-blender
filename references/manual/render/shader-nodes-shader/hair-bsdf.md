# Hair BSDF

## Hair BSDF

### Hair BSDF

*Cycles Only*

Add shading for hair.

### Inputs

- **Color** — Hair color.
- **Offset** — Angular light rotation for reflection/transmission.
- **Roughness U/V** — Roughness along light direction and perpendicular to it.
- **Tangent** — Input tangent.

### Properties

**Component** — Two selectable components (usually both via Mix Node).

- **Reflection** — Light bouncing off hair surface.
- **Transmission** — Light passing through and exiting the opposite side.

With Mix node: 0 = full Reflection, 1 = full Transmission.

### Outputs

- **BSDF** — Standard shader output.

[Related references](INDEX.md).
