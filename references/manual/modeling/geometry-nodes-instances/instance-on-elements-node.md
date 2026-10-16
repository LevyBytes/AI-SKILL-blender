# Instance on Elements Node

## Instance on Elements Node

### Instance on Elements Node

The Instance on Elements node creates instances of objects, collections, or geometry on selected elements (points, edges, faces, or corners) of input geometry. Offers flexibility for varied instancing workflows.

### Inputs

Geometry
Base geometry for instancing.

Instance On
Target element type.

Points:
One instance per point location.

Edges:
Instances along edges.

Faces:
Instances on each face surface.

Corners:
One instance per face corner (vertex per face).

Mask
Boolean selection controlling which elements receive instances. Floating-point values (0–1) act as probabilistic selection, yielding a random subset.

Input Type
Source geometry specification mode.

Data-Block:
Instance from an object or collection data-block.

Geometry:
Instance from node input geometry.

Instance Type Data-Block
When Data-Block input: Object or Collection.

Object / Collection Data-Block
Which object or collection to instance (Data-Block mode).

Instance Geometry
Which geometry to instance (Geometry input mode).

Realize Instances
Convert all instances to real geometry for a single merged output. Required for some downstream operations.

Keep Surface
Retain the underlying surface used for instancing instead of outputting only instances.

Seed
Random-number seed for probabilistic selections or instance-index randomization.

### Pick Instance Data-Block Collection

When instancing from a collection, optionally select which child object to instance per element.

Instance Index
Selection method for children.

Random:
Pick a random collection object per element.

Sequence:
Cycle through collection objects in order.

Input:
Use Instance Index input socket.

Instance Index Input
Index value (for "Input" mode).

### Transform

Surface Offset
Displace instances along the element normal.

Align Rotation
Align instance rotation to element orientation (e.g., surface normal).

Scale
Per-axis or uniform instance scaling.

### Outputs

Geometry
Result geometry with instances on selected elements.

[Related references](INDEX.md).
