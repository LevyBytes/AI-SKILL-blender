# Displace Modifier

## Displace Modifier

The Displace modifier shifts vertices based on a texture's brightness values. Procedural or image textures work equally well.

Displacement direction can be along a local axis, along vertex normals, or read as RGB values to displace simultaneously in X, Y, and Z (Vector Displacement).

Texture names the source texture. If empty, the default value is 1.0 (white).

Coordinates specifies the sampling method (see common masking options for full reference).

Direction selects the displacement axis:

X, Y, Z displaces along each axis.

Normal displaces along computed vertex normals.

Custom Normal displaces along averaged custom normals.

RGB to XYZ reads Red for X, Green for Y, Blue for Z displacement.

Space, when using X/Y/Z or XYZ direction, selects local or global axis alignment.

Strength scales the final displacement value. Negative values invert the effect.

Formula: vertex_offset = (texture_value - Midlevel) × Strength

Midlevel sets the texture value treated as zero displacement. Values below it displace negative; values above displace positive.

Formula: displacement = texture_value - Midlevel

Blender's color/luminosity values typically range 0.0–1.0, not 0–255.

Vertex Group controls the effect via group weights.

Invert reverses the group influence.

[Related references](INDEX.md).
