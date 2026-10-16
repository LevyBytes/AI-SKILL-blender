# Smooth Laplacian Modifier

## Smooth Laplacian Modifier

The Smooth Laplacian modifier reduces noise on a mesh's surface with minimal change to its shape, and can also exaggerate the shape using a negative Factor. It's useful for objects reconstructed from the real world that contain undesirable noise — it removes the noise while preserving desirable geometry and the original model's shape. It's based on a curvature-flow Laplace Beltrami operator in a diffusion equation.
Hint: meshes with many vertices — more than ten thousand (10,000) — may take several minutes to process, so test on small portions of the mesh before running it on the entire model.

Options:
Repeat — repetitions run the smoothing more than once; each repetition recalculates the mesh's flow curvature and so removes more noise per iteration using a small Factor < 1.0. At 0, no smoothing is done.
Note: more repetitions take longer to calculate, so beware of doing so on meshes with a large number of vertices.
Axis — toggle buttons to enable/disable deforming vertices in the X, Y, and/or Z axis directions.
Lambda Factor — controls how far each vertex is displaced along the flow curvature: with a small Factor you remove noise without affecting desirable geometry; with a large Factor you get smoothed shapes at the cost of fine geometry details; with a negative Factor you enhance the shape while preserving desirable geometry; and when the Factor is negative, multiple iterations can magnify the noise.
Lambda Border — since curvature flow can't be calculated on border edges, they're handled separately by a much simpler method, with this property controlling its influence: positive values smooth the vertex positions, while negative values "enhance" them by transforming them in the opposite direction.
Preserve Volume — the smoothing can cause shrinkage, significant at large Factor or Repeat values; use this option to reduce that effect.
Normalized — when enabled, results depend on face sizes; when disabled, geometry spikes may occur.
Vertex Group — a vertex group name to constrain the effect to a group of vertices only, allowing selective, real-time smoothing or enhancing by painting vertex weights.
Invert — invert the influence of the selected vertex group, so the group now represents vertices that will not be deformed by the modifier; the setting reverses the group's weight values.

See also the Smooth Modifier.

[Related references](INDEX.md).
