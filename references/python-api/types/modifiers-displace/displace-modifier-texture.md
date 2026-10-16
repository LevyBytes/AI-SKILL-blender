# bpy.types.DisplaceModifier: texture, texture_coords, texture_coords_bone, texture_coords_object

texture

Type :

Texture
texture_coords

(default 'LOCAL' )

- LOCAL
Local – Take texture coordinates from the local coordinate system.

- GLOBAL
Global – Take texture coordinates from the global coordinate system.

- OBJECT
Object – Take texture coordinates from the linked object’s local coordinate system.

- UV
UV – Take texture coordinates from the UVs.

Type :

Literal[‘LOCAL’, ‘GLOBAL’, ‘OBJECT’, ‘UV’]
texture_coords_bone

The bone that supplies the texture coordinates (default “”, never None)

Type :

str
texture_coords_object

The object that supplies the texture coordinates

Type :

Object

[Related references](INDEX.md).
