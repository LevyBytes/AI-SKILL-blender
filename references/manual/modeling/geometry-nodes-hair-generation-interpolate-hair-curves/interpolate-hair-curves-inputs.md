# Interpolate Hair Curves: Inputs

## Interpolate Hair Curves

### Interpolate Hair Curves

Interpolate Hair Curves grows new strands by blending existing guide curves across a surface mesh. A few guides set the broad shape; the node fills in interpolated curves for a dense, detailed hair system.

For lighter, duplication-style setups, the Duplicate Hair Curves node is a thinner alternative that may run faster.

Note

This node or modifier only works with valid Surface geometry or object inputs plus a Surface UV Map .

### Inputs

Geometry
Geometry: the hair-curve geometry fed in, holding the guide curves to interpolate.

Surface Input Type
Picks how surface data is supplied for interpolation.

Object :

Provide the surface through an object reference.

Geometry :

Wire a geometry input straight to the surface mesh.

Surface
The surface object the interpolated curves attach to. Its transforms have to match the modifier object's.

Surface UV Map
The UV map that locates attachment spots for the interpolated curves on the surface.

Surface Rest Position
On, the surface mesh drops to its rest pose before curves attach, holding root positions steady when deformation follows.

Tip

Pairing this with Deform Curves on Surface, enable Surface Rest Position when the deform node sits after this one, so pre-deformed coordinates feed consistent interpolation.

Follow Surface Normal
On, each interpolated curve orients to the surface normal sampled where its root attaches.

Part by Mesh Islands
On, distinct mesh islands count as separate interpolation zones, blocking guides from blending across disconnected patches.

Interpolation Guides
How many nearest guide curves shape each new strand. Higher values smooth transitions but may dent performance slightly.

Distance to Guides
The farthest a guide can sit and still join the interpolation. Guides past this range have no say.

[Related references](INDEX.md).
