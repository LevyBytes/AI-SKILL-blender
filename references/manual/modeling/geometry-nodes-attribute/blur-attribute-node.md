# Blur Attribute Node

## Blur Attribute Node

The Blur Attribute node softens attribute values by mixing them with neighboring geometry parts.

Each step blends a component's value with those of its neighbors, weighted by a factor applied to the neighbors before accumulation.

Blurring functions only on Meshes and Curves with domains having explicit neighbor definitions (vertices, edges, faces of meshes; curve control points). Face corner attributes are not supported, as ideal blending behavior is undefined. All data types work except boolean.

Value: Each element's starting attribute value.
Iterations: How many times to repeat mixing. Each iteration uses previous results independently.
Weight: Multiplier for each element.

Data Type: The data representation used.

Value: The mixed values after blurring.

Input: A subdivided plane with random color. The second Subdivide adds density. Blur Attribute mixes all colors for each face, smoothing the result.

[Related references](INDEX.md).
