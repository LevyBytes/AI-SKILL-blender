# UV Unwrap Node

## UV Unwrap Node

UV Unwrap Node

Generates a UV map from islands based on a selection of seam edges. The node implicitly packs islands afterward, since results may not be generally useful otherwise.

See also: The UV editor's Unwrap operator does the same. This node skips aspect ratio correction—add it yourself with Vector Math Node if needed.

Inputs
Selection: Faces to participate in unwrap. UVs on any other face remain unaffected.
Seam: Edges marking where the mesh is "cut" for unwrapping.
Margin: Distance between UV islands.
Fill Holes: Temporarily plug the mesh's holes ahead of unwrapping, which helps dodge overlaps and keep symmetry intact.
Method:
  Angle Based: Produces a good 2D mesh representation.
  Conformal: Uses LSCM (Least Squares Conformal Mapping). Usually less accurate than Angle Based but works better for simpler objects.

Output
UV: Generated UV coordinates between 0 and 1 for each face corner in selected faces.

Note: To make Blender recognize it as a UV map, use Store Named Attribute Node on the Face Corner domain with 2D Vector data type (no 2D Vector socket exists).

[Related references](INDEX.md).
