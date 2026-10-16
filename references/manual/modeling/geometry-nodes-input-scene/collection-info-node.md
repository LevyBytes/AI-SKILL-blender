# Collection Info Node

## Collection Info Node

### Collection Info Node

The Collection Info node retrieves collection properties. Useful for parameterizing geometry-node trees via external collections.

Tip: Drag a collection into the node editor to quickly add this node.

### Inputs

Collection
The collection to query.

Separate Children
Output each child as a distinct instance, sorted alphabetically by object and collection. Use with the Pick Instance option in Instance on Points Node to vary instances per point.

Note: Renaming objects and collections does not trigger a modifier re-evaluation; manual updates are needed.

Reset Children
Remove each child's initial transform when converting to instances. Keeps children visually distinct in the viewport while centering them at the instancing point.

### Properties

Transform Space
The coordinate system for output instances (the instances are transformed, but not the geometry of the collection in them).

Original:
Instances relative to collection offset.

Relative:
Merge input collection instances with modified geometry, preserving scene-space relationships.

### Outputs

Instances
World-space collection instances with all modifiers applied, represented as geometry.

[Related references](INDEX.md).
