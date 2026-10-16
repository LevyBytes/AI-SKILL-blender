# Warp Modifier

## Warp Modifier

The Warp modifier warps mesh portions to new locations flexibly, using two objects to specify "from" and "to" regions.

Understanding requires knowledge of two points from the target objects' origins. The "from" point designates a region drawn toward the "to" point, analogous to Proportional Editing in Edit Mode.

Object From specifies the origin transformation for the warp source.

Object To specifies the origin transformation for the warp destination.

Preserve Volume, when active, prevents volume loss when rotating the transforms.

Strength sets effect intensity.

Vertex Group controls influence per vertex. When empty, all vertices are equally affected.

Invert reverses the group influence.

Falloff Type controls how strength changes from the transform center to the Radius—see Proportional Editing for descriptions.

Radius sets how far from the transform centers the effect reaches.

Texture enables fine per-vertex control of which vertices warp and by how much (see common masking options for reference).

Warp is sometimes awkward to use and has limited application, but it serves a few cases. For instance, it enables interactive Proportional Editing suitable for animation. It also resembles the Deform Modifier, enabling mesh warping without vertex groups.

[Related references](INDEX.md).
