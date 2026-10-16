# Scatter surface density and instances

## Scatter on Surface Modifier

This node scatters points or instances across mesh surfaces with flexible density and randomization control, useful for procedural placement of grass, rocks, debris, or other scattered elements.

Selection determines which faces participate in scattering; unselected areas receive no scatters.

Density Method: Density bases scatters on per-unit-area density, Amount sets a total fixed count.

Distribution Method with Density: Random places points without order, Poisson Disk spaces points evenly using minimum separation.

Distribution Mask limits scattering to masked regions (1.0 enables, 0.0 excludes).

Minimum Distance Poisson Disk defines minimum spacing between points in Poisson mode; higher values create fewer, more evenly distributed points.

Keep Surface preserves the original surface geometry alongside instances.

Scatter on Instances enables scattering directly on existing instances.

Seed varies the distribution pattern.

Instance Input Type: Data-Block sources instances from an object or collection, Geometry uses input geometry directly.

When using Data-Block, Instance Type selects Object or Collection.

Viewport Visibility controls the percentage of instances shown in the viewport.

Realize Instances converts all instances to real geometry, necessary for some downstream operations.

Pick Instance (collection mode): Choose randomly or with control which member object gets instanced at each scattered location.

Reset Transform clears instance transforms before applying scattering transforms.

Instance Seed controls randomization per instance.

Surface Offset moves instances along the element normal away from the surface.

Align Rotation aligns instance orientation to the surface element orientation.

Randomize offsets (maximum translation per axis), rotations (maximum per axis), and scales (uniform or per-axis). Flipping randomly mirrors instances along selected axes. Seed initializes the random generator.

Image Mask uses a texture to control density via UV mapping.

UV Map specifies the mapping used for the image mask.

[Related references](INDEX.md).
