# Shrinkwrap Hair Curves

## Shrinkwrap Hair Curves

### Shrinkwrap Hair Curves

Shrinkwrap Hair Curves casts strands onto a target surface, nudging them to ride a mesh's shape. Use it to conform hair to a scalp or underlying geometry, holding curves correctly placed against the surface.

### Inputs

Geometry
Geometry — the hair-curve geometry fed in for shrinkwrapping.

Surface Input Type
Picks how surface data is supplied for the shrinkwrap. A connected geometry input wins over an object input.

Object :

Sample the target surface through an object reference.

Geometry :

Read the surface straight from a geometry input.

Surface
The surface object or geometry that the projection targets.

Factor
How much the shrinkwrap pulls overall. At 0.0 the hair is untouched; at 1.0 it fully conforms to the surface.

Offset Distance
A standoff distance from the target surface. Positive pushes curves off the surface; negative draws them inward.

Above Surface
Blends the shrinkwrap for points starting above the surface, easing the transition when only parts of a strand should stick to the mesh.

Smoothing Steps
How many smoothing passes run after the shrinkwrap. More passes cut artifacts and smooth the outcome.

Lock Roots
On, each strand's root is held in place through the shrinkwrap, keeping roots pinned where they started — say, fixed to a scalp.

### Outputs

Geometry
Output geometry with curves conformed to the target surface.

[Related references](INDEX.md).
