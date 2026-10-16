# Remesh Modifier

## Remesh Modifier

This modifier regenerates mesh topology, outputting only quads that follow input surface curvature.

Mode offers three variants differing in smoothing: Blocks applies none, Smooth creates a smooth surface, Sharp preserves sharp edges like Smooth but also respects input corners.

Sharpness controls edge fidelity; higher values match input geometry more closely, lower values filter noise.

Voxel mode uses OpenVDB to generate a manifold mesh preserving the original volume.

Adaptivity reduces final face count by simplifying geometry where detail is unnecessary, introducing triangulation for flat regions.

Octree Depth sets resolution; low values create larger faces, high values create denser output.

Scale further tweaks output resolution; lower values reduce resolution.

Smooth Shading applies smooth shading to output faces instead of flat, independent of input shading.

Remove Disconnected filters out small isolated pieces; thin mesh sections can fragment. Threshold controls what counts as too small.

Important: the input mesh should have some thickness; completely flat input benefits from a preceding Solidify Modifier.

[Related references](INDEX.md).
