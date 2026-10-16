# Curve to Mesh Node

## Curve to Mesh Node

The Curve to Mesh node transforms all splines into mesh geometry. Optionally, a profile curve shapes the output.

Attributes transfer to the result, including built-ins like sharp_face, positioned on the appropriate domain.

Tip: Output mesh edges are marked sharp based on the profile curve. If any profile Bézier splines use Free or Vector handles, matching output edges are shaded sharp.

Curve: Standard input (non-curve components ignored).
Profile Curve: If supplied, extruded along all splines; otherwise a chain of edges results.
Scale: Per-control-point profile scaling.
Fill Caps: For cyclic profiles, seal the ends with n-gons. The mesh is Manifold; new faces connect to existing edges.

Mesh: Standard output.

[Related references](INDEX.md).
