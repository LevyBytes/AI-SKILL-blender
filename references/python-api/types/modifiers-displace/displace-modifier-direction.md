# bpy.types.DisplaceModifier: direction

direction

(default 'NORMAL' )

- X
X – Drive displacement along X using the texture’s intensity.

- Y
Y – Drive displacement along Y using the texture’s intensity.

- Z
Z – Drive displacement along Z using the texture’s intensity.

- NORMAL
Normal – Drive displacement along the vertex normal using the texture’s intensity.

- `CUSTOM_NORMAL`
Custom Normal – Drive displacement along the (averaged) custom normal using the texture’s intensity, dropping back to the vertex normal when unavailable.

- `RGB_TO_XYZ`
RGB to XYZ – Map the texture’s RGB channels onto XYZ to displace the mesh.

Type :

Literal[‘X’, ‘Y’, ‘Z’, ‘NORMAL’, ‘`CUSTOM_NORMAL`’, ‘`RGB_TO_XYZ`’]

[Related references](INDEX.md).
