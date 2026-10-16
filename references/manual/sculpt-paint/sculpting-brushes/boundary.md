# Boundary

## Boundary

### Boundary

Reference

Mode :

Sculpt Mode

Brush :

Sidebar ‣ Tool ‣ Brush Settings ‣ Advanced ‣ Brush Type

Similar to the Pose brush but deforms the open boundaries of a mesh. The tool detects the mesh boundary closest to the active vertex and propagates the deformation using the brush Falloff into the mesh.

The main use cases of this brush are the Bend and Expand geometry, which leads to the best results on evenly distributed quad based topology. Use the Inflate , Grab , Twist , and Smooth deformation modes, to further adjustments and tweaks to the result (which do not depend that much on a clean topology).

Tip

Boundaries to hidden geometry will also be counted as an open boundary.

The boundary origin is displayed via a white line, which indicates the reach of the deformation. The targeted boundary that will be deformed is highlighted in the brush cursor color.

If the Deformation Target is changed, the brush can also be used for cloth sculpting.

Note

Evenly distributed and quad based topology will lead to much better results. Triangles and N-gons are also supported but may lead to unpredictable outcomes.

### Brush Settings

### General

Note

More info at General brush settings and on Advanced brush settings.

### Unique

Deformation
Deformation type that is used by the brush.

Bend :

Rotates the boundary around the local Y axis. Useful for creating folding shapes, like sleeves.

Expand :

Moves/extends the mesh boundary in the local X direction. Useful for extending the boundaries along the surface.

Inflate :

Works similar to the Inflate tool but, the vertices that are inflated are constrained to the mesh boundary.

Grab :

Works similar to the Grab tool but, the vertices that are grabbed are constrained to the mesh boundary.

Twist :

Rotates the active boundary around the local Z axis. Useful for creating folds like on a skirt.

Smooth :

Works similar to the Grab tool but, the vertices that are smoothed are constrained to the mesh boundary.

Boundary Falloff
How the brush Falloff is applied across the boundary.

Constant :

Applies the same deformation in the entire boundary.

Brush Radius :

Applies the deformation only within the brush radius.

Loop :

Applies the brush falloff in a loop pattern along the boundary.

Loop and Invert :

Applies the falloff radius in a loop pattern, inverting the direction back & forth.

Boundary Origin Offset
Offset of the boundary origin in relation to the brush radius.

[Related references](INDEX.md).
