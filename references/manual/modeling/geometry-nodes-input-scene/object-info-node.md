# Object Info Node

## Object Info Node

### Object Info Node

The Object Info node retrieves object properties. Useful for linking geometry-node behavior to external objects—either directly via geometry or indirectly via transformation data.

Drag an object into the node editor to add this node quickly.

### Inputs

Object
The object to query.

As Instance
Output the object as a single instance rather than realized geometry. Allows instancing non-geometry types.

### Properties

Transform Space
Coordinate system for vector and geometry outputs.

Original:
Geometry relative to the input object; location, rotation, scale relative to world origin.

Relative:
Project input geometry, location, rotation, scale into the modified object, preserving scene relationships.

### Outputs

Transform
Matrix encoding object location, rotation, and scale.

Location
Object location in world space.

Rotation
Object rotation in world space.

Scale
Object scale in world space.

Geometry
Object geometry in world space with all modifiers applied.

[Related references](INDEX.md).
