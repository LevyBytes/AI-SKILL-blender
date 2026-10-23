# Scatter on Surface Node: Scatter on Surface Node, Inputs

## Scatter on Surface Node

Scatter on Surface Node

Distributes points or instances across mesh surfaces using density control, random or Poisson disk sampling, and optional masking. Useful for procedural ground scatter (grass, rocks, debris).

Inputs:
Mesh: Target surface.
Selection: Face/area inclusion. Unselected regions skip distribution.

Density Method - Point-count control:
Density: Per-unit-area field.
Amount: Fixed total count.

Distribution Method Density - Density pattern:
Random: Uniform random placement.
Poisson Disk: Minimum-distance even spacing.

Density Density: Per-area point count.

Amount Amount: Total point count.

Distribution Mask: Limiting field (1.0 allows, 0.0 blocks).

Minimum Distance Poisson Disk: Minimum inter-point spacing.

Keep Surface: Retain original surface in output (vs. instances-only).

Scatter on Instances: Scatter on existing instances rather than a single mesh.

Seed: Random generator initialization.

Instancing:
Input Type - Source:
Data-Block: Object or collection.
Geometry: Input geometry.
Instance Type Data-Block: Object or Collection.
Object / Collection Data-Block: Target object or collection.
Instance Geometry: Geometry input.
Viewport Visibility: Visible instance percentage.
Realize Instances: Convert instances to real geometry.

Pick Instance Data-Block Collection: Random or directed child object selection:
Reset Transform: Restore instance transform before applying scatter.
Instance Seed: Randomization per element.

Transform:
Surface Offset: Normal-direction offset.
Align Rotation: Element orientation alignment.
Alignment Axis: Alignment direction.
Scale: Uniform or per-axis scaling.

Randomize (toggleable in panel header):
Offset: Maximum translation per axis.
Rotation: Maximum rotation per axis.
Scale Axes - Scaling application:
Uniform: Single factor.
Axes: Independent factors.
Scale: Maximum scale factor.
Flipping: Random per-axis mirroring.
Seed: Random number initialization.

Masking:
Image Mask: Scattering density controller via UV-mapped image.
UV Map: UV channel for mask interpretation.

Outputs:
Instances: Scattered instances per method and parameters.

[Related references](INDEX.md).
