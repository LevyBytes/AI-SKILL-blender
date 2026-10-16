# Displace Hair Curves

## Displace Hair Curves

### Displace Hair Curves

Displace Hair Curves shifts where strands sit or how they are shaped via a displacement vector — a procedural lever for movement, a directional push, or surface alignment. The offset resolves in object, world, or surface-normal space, per the setup.

### Inputs

Geometry
Geometry — the hair-curve geometry fed in for displacing.

Factor
How strongly the displacement reads overall. At 0.0 nothing moves; at 1.0 the displacement vector applies in full.

Shape
How the displacement factor varies from root to tip. At 0.0 the offset stays even along the strand; at 0.5 it ramps linearly from root to tip.

Object Space
The object whose transform supplies the offset's coordinate frame. Empty, and the modifier's own local space is used.

Displace Vector
Supplies both heading and length for the offset. Fields or other procedural sources can drive it.

### Surface Normal

Switch this on to push curves along a surface normal — handy for "lifting" or "pushing" strands off a mesh. The toggle sits in the header.

Surface Input Type
The route by which surface data arrives for normal sampling. A connected geometry input wins over an object input.

Object :

Sample surface normals through an object reference.

Geometry :

Read normals straight from a geometry input.

Surface
The surface object that normals are sampled from for the offset.

Surface UV Map
Which UV map gets used while reading surface normals for the offset.

Surface Normal Displacement
How far curves travel along the sampled surface normal. Sign sets direction — positive or negative.

### Outputs

Geometry
Output geometry, now carrying the displaced hair curves.

[Related references](INDEX.md).
