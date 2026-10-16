# bpy.types.ShaderNodeTexIES: properties

## ShaderNodeTexIES(ShaderNode)

### ShaderNodeTexIES(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexIES ( ShaderNode )

Reproduces real-world fixtures from IES files, which record how a light source spreads its intensity in each direction.
filepath

IES light path (default “”, never None, blend relative // prefix supported)

Type :

str
ies

Internal IES file

Type :

Text
mode

Whether the IES file is loaded from disk or from a text data-block (default 'INTERNAL' )

- INTERNAL
Internal – Use internal text data-block.

- EXTERNAL
External – Use external .ies file.

Type :

Literal[‘INTERNAL’, ‘EXTERNAL’]

[Related references](INDEX.md).
