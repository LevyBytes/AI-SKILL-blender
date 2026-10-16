# Fill Curve Node

## Fill Curve Node

The Fill Curve node creates a mesh from curves via constrained Delaunay triangulation. Output lies flat on local Z = 0.

Curve: Standard input (curve component).
Group ID: Grouping value. Different IDs treat curves separately.
Mode: Output geometry type (Triangles or N-gons).

Mesh: Filled output.

Single-point splines customize the triangulation.

Default Fill Curve applied to a star. 

Star with one point added for triangulation. 

Star with 300 points for dense triangulation. 

Group ID examples:

Four curves, one Group ID → one mesh island. 

Four curves, different Group IDs → four islands. 

Four curves split into two groups by position → two islands.

[Related references](INDEX.md).
