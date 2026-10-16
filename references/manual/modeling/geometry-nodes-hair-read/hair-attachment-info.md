# Hair Attachment Info

## Hair Attachment Info

### Hair Attachment Info

Hair Attachment Info reports how and where hair curves bind to a surface mesh — letting nodes pull stored attachment coordinates, check whether the attachment still holds, and read the surface normal there. Such data is vital for deforming, simulating, and reattaching hair when the mesh shifts.

### Inputs

Surface Geometry
Whatever surface geometry the hair curves are bound to — usually the very mesh that drove hair generation or interpolation.

Surface UV Map
A UV map across the surface mesh that pins down each curve's attachment point, so the node can pull back the stored coordinates per curve.

### Outputs

Attachment UV
Per-curve UV coordinates marking where on the surface a curve binds. Held per curve, they usually let the right attachment spot be found even after the surface topology shifts.

Attachment is Valid
A boolean output flagging whether each curve carries a valid stored attachment. Use it to catch invalid or missing attachment data after topology edits or a surface swap.

Surface Normal
The surface mesh's normal heading evaluated at the curve's attachment point. Use it to align hair roots, orient instances, or drive deformation by surface orientation.

[Related references](INDEX.md).
