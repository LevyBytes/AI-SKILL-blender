# Edge Split Modifier

## Edge Split Modifier

This modifier duplicates edges within a mesh, severing connectivity between faces and affecting normal generation at the split location, producing sharp-appearing edges. Manual shading control is possible by selecting which edges appear smooth or sharp; see Mesh Smoothing for alternatives.

Modern projects often use custom normals for the same result without topology changes; edge-splitting is kept for compatibility.

Edge Angle enabling splits edges when the angle between adjacent faces exceeds the Split Angle threshold; 0 splits all, 180 splits none.

Sharp Edges splits edges marked as sharp.

Non-manifold edges always split regardless of settings.

[Related references](INDEX.md).
