# Random Rotation Node

## Random Rotation Node

Generates random rotation values within a zenith (vertical) range.
Useful for randomizing object orientation in instances, particles, or geometry.

**Inputs**

Min Zenith
Lower angle limit for vertical rotation.

Max Zenith
Upper angle limit for vertical rotation.

ID
Seed ID for the random generator. Defaults to the ID Node's value—the `id` attribute if present, otherwise the index.

Tip: By default, each element gets a unique random rotation (keyed by ID).
To use the same rotation for the entire geometry, feed a constant value (e.g., Integer Node) to ID.

Seed
Field to vary the random sequence even when ID is unchanged.

**Outputs**

Rotation
The output rotation. Can be applied directly to instances or chained into other transformations.

[Related references](INDEX.md).
