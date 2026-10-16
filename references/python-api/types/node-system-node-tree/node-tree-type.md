# bpy.types.NodeTree: type

type 

Node Tree type (deprecated, bl_idname is the actual node tree type identifier) (default 'SHADER' , readonly)

- UNDEFINED
Undefined – Undefined type of nodes (can happen e.g. when a linked node tree goes missing).

- CUSTOM
Custom – Custom nodes.

- SHADER
Shader – Shader nodes.

- TEXTURE
Texture – Texture nodes.

- COMPOSITING
Compositing – Compositing nodes.

- GEOMETRY
Geometry – Geometry nodes.

Type :

Literal[‘UNDEFINED’, ‘CUSTOM’, ‘SHADER’, ‘TEXTURE’, ‘COMPOSITING’, ‘GEOMETRY’]

[Related references](INDEX.md).
