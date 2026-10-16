# Materials: Thickness

Materials — Configuration

See also
EEVEE uses the same material node system as Cycles but with feature gaps.
See Shader nodes limitations.

### Thickness

Reference
Panel: Properties ‣ Material ‣ Thickness

Thickness approximates inner structure without heavy calculation. Used for Subsurface Scattering, Translucent BSDF, Refraction BSDF, and related nodes.

When the output node receives no thickness input, object dimensions determine a default value. Connected values represent object space thickness (scaled by object transform). Zero disables thickness approximation and treats geometry as single-sided.

This output is exclusive to EEVEE.

Note
- Thickness excludes the object's interior from computation.
- Refraction does not refract objects within the thickness distance.
- Shadow casting objects do not cast shadows within the thickness distance.

Tip
- For large or composite meshes (e.g., plants), set thickness to individual component thickness (e.g., leaf or grass blade width).
- Bake thickness to textures or attributes for improved accuracy.

See also
Thickness Mode controls thickness interpretation.

[Related references](INDEX.md).
