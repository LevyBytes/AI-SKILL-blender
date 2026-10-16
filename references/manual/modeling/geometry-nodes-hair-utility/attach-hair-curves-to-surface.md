# Attach Hair Curves to Surface

## Attach Hair Curves to Surface

### Attach Hair Curves to Surface

Attach Hair Curves to Surface ties hair curves to a surface mesh, fixing their attachment positions and, if you want, aligning them to the surface orientation. It is a backbone of hair generation and grooming, holding curves anchored where they belong on the base mesh through later deforms or topology edits.

Note

This node or modifier only works given valid Surface geometry or object inputs together with a Surface UV Map .

### Inputs

Geometry
Geometry — the hair-curve geometry fed in for attaching to the surface.

Surface Input Type
How the surface geometry arrives for attachment. With both wired, the geometry input wins.

Object :

Use an object reference as the target surface.

Geometry :

Wire a geometry input straight to the surface mesh.

Surface
Whatever object or geometry serves as the attachment target. For clean alignment, its transforms must match the modifier object.

Surface UV Map
A UV map that nails down attachment points across the surface; the resulting coordinates are kept per curve so attachment stays steady.

Surface Rest Position
On, the surface mesh drops to its rest pose ahead of attachment, keeping results consistent when curves later deform along that same surface.

Tip

Run this alongside Deform Curves on Surface and turn on Surface Rest Position when that step comes after, so attachment coordinates are logged in the pre-deformed state.

Sample Attachment UV
Reads the Surface UV Map at the attachment point and banks those UV coordinates per curve, leaving the attachment data on hand for later nodes.

Snap to Surface
Drops each curve's root onto the closest spot on the surface mesh, planting every root right on the surface.

Align to Surface Normal
Spins each curve so its root direction meets the surface normal. Stable output here usually wants guide data or consistent curve orientation.

Blend along Curve
Brings the deform or alignment in by degrees from root to tip, rather than slapping it on uniformly.

### Outputs

Geometry
Output geometry with refreshed curve attachments.

Surface UV Coordinate
Per curve, the matching UV coordinate on the surface mesh at its attachment point.

Surface Normal
The surface mesh's normal vector taken at each curve's attachment point.

[Related references](INDEX.md).
