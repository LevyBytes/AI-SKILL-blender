# Lattice

## Lattice

A Lattice — often called a deformation cage outside Blender — is a non-renderable 3D grid of vertices whose main use is deforming the object it controls via a Lattice Modifier (parenting with Lattice Deform applies one automatically). Editing: Flip (Distortion Free) mirrors the vertices' displacement from their base position along U, V, or W; Make Regular resets the whole lattice to a regular grid with cells scaled to one cubic unit. Properties — Lattice (a data-block menu): Points sets the subdivision rate on each of U, V, W; Interpolation Type is a per-axis selector (Linear, Cardinal, Catmull-Rom, B-Spline); Outside considers only the lattice's surface vertices; and Vertex Group assigns the influence strength as a weight to the chosen vertex group's vertices. Usage: scale and move the lattice to fit around your object in Object Mode — any scaling applied in Edit Mode deforms the object, including applying its scale with Ctrl-A, which has the same effect as scaling the lattice in Edit Mode (and thus the object).

[Related references](INDEX.md).
