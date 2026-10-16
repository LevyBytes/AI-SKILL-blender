# bpy.types.WaveModifier: texture, texture_coords, texture_coords_bone, texture_coords_object

texture

Type :

Texture
texture_coords

(default 'LOCAL' )

- LOCAL
Local – Read texture coordinates from the local coordinate system.

- GLOBAL
Global – Read texture coordinates from the global coordinate system.

- OBJECT
Object – Read texture coordinates from a linked object's local coordinate system.

- UV
UV – Read texture coordinates from the UV layer.

Type :

Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']
texture_coords_bone

Bone supplying the texture coordinates (default "", never None)

Type :

str
texture_coords_object

Object supplying the texture coordinates

Type :

Object

[Related references](INDEX.md).
