# bpy.types.VertexWeightEditModifier: mask_constant, mask_tex_map_bone, mask_tex_map_object, mask_tex_mapping, mask_tex_use_channel, mask_tex_uv_layer, mask_texture, mask_vertex_group

mask_constant 

How strongly the current changes act on the vgroup overall (in [-inf, inf], default 1.0)

Type :

float
mask_tex_map_bone 

The bone supplying texture coordinates (default "", never None)

Type :

str
mask_tex_map_object 

The object supplying texture coordinates

Type :

Object
mask_tex_mapping 

The texture coordinates to drive the mapping (default 'LOCAL' )

- LOCAL
Local – Use local generated coordinates.

- GLOBAL
Global – Use global coordinates.

- OBJECT
Object – Use local generated coordinates of another object.

- UV
UV – Use coordinates from a UV layer.

Type :

Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']
mask_tex_use_channel 

The texture channel used for masking (default 'INT' )

Type :

Literal['INT', 'RED', 'GREEN', 'BLUE', 'HUE', 'SAT', 'VAL', 'ALPHA']
mask_tex_uv_layer 

UV map name (default "", never None)

Type :

str
mask_texture 

Masking texture

Type :

Texture
mask_vertex_group 

Masking vertex group name (default "", never None)

Type :

str

[Related references](INDEX.md).
