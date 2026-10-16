# Smooth

## Smooth

### Smooth

Reference

Mode:
Sculpt Mode

Brush:
Sidebar ‣ Tool ‣ Brush Settings ‣ Advanced ‣ Brush Type

Polish surfaces or reduce volume. Always accessible via Shift.

Also provided as a Mesh Filter
for concurrent smoothing of unmasked zones.

Note

This named Smooth brush activates whenever Shift and sculpting occur.
Alter Smooth behavior or strength by selecting the Smooth
brush and tuning options.

### Brush Settings

### General

Strength
Smoothing magnitude scales with mesh density.
Finer resolution reduces strength; increase as needed.

Direction Ctrl

Smooth
Refines mesh surfaces.

Enhance Details
Amplifies surface features through reverse-direction smoothing.

Note

More info at General brush settings
and on Advanced brush settings.

### Unique

Deformation
Two methods available.

Laplacian:
Refines both surfaces and interiors. Default action.

Surface:
Refines only surfaces, conserving volume.

Shape Preservation
Extent the original form survives refining. Higher values
lower multi-iteration smoothing strength.

Per-Vertex Displacement
Degree each vertex affects the outcome.
Higher values reduce total smoothing magnitude.

Iterations
Count of refinement applications per brush action.

Note

This works by applying standard refinement, computing
the difference between the original (blended between starting point and fully original per Shape Preservation)
and the refined geometry, refining these differences, shifting vertices via refined differences,
and finally merging the original based on Per-Vertex Displacement.

[Related references](INDEX.md).
