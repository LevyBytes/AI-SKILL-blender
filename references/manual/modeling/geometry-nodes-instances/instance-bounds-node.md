# Instance Bounds Node

## Instance Bounds Node

### Instance Bounds Node

For every top-level instance, Instance Bounds returns its axis-aligned bounding box.

Useful for determining instance spatial extent—positioning or scaling based on size, etc.

Note: Only top-level instances are considered; nested instances inside instance geometry are not included (avoids realizing nested instances for performance).

See Nested Instancing.

### Inputs

Use Radius
For curves, point clouds, and Grease Pencil data, account for the radius attribute when computing bounds.

### Outputs

Min
Bounding-box minimum corner per instance, in local space.

Max
Bounding-box maximum corner per instance, in local space.

[Related references](INDEX.md).
