# Material Output Node

## Material Output Node

### Material Output Node

Output surface material information to a surface object.

### Inputs

- **Surface**: Surface shading.
- **Volume**: Interior shading.
- **Displacement**: Bump mapping or actual subdivided displacement.
- **Thickness** *(EEVEE)* — Approximate inner geometry structure without heavy computation. Used for Subsurface Scattering, Translucent BSDF, Refraction BSDF, and related effects. If unconnected, a default thickness based on the smallest object dimension applies. When connected, it's treated as object-space thickness (scaled by object transform). Zero disables thickness and treats the object as single-interface.

Used for: Subsurface Scattering, Translucent BSDF, Refraction BSDF effects.

Notes: Thickness skips the object interior; refraction won't refract objects within the thickness distance; shadow-casting objects won't cast shadows within the thickness distance.

Tips: For large/compound meshes (vegetation, hair), set thickness to individual part thickness (leaves, grass blades). Bake thickness to textures or custom attributes for accuracy.

See also: Thickness Mode controls thickness behavior.

### Properties

**Target**: Render engine for input shaders. Default: shaders shared between Cycles and EEVEE. Multiple output nodes enable engine-specific setups.

### Outputs

None.

[Related references](INDEX.md).
