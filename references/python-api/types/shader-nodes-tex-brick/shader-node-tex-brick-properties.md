# bpy.types.ShaderNodeTexBrick: properties

## ShaderNodeTexBrick(ShaderNode)

### ShaderNodeTexBrick(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexBrick ( ShaderNode )

A procedural texture that lays out a brick pattern.
color_mapping

Color mapping settings (readonly, never None)

Type :

ColorMapping
offset

Sets how far alternating rows of bricks are shifted sideways (in [0, 1], default 0.5)

Type :

float
offset_frequency

Controls the spacing of offset rows. Setting it to 2 produces an alternating even/uneven row pattern. (in [1, 99], default 2)

Type :

int
squash

Scales the brick width on the rows picked out by the Offset Frequency (in [0, 99], default 1.0)

Type :

float
squash_frequency

Controls how frequently rows are made up of “squished” bricks (in [1, 99], default 2)

Type :

int
texture_mapping

Texture coordinate mapping settings (readonly, never None)

Type :

TexMapping

[Related references](INDEX.md).
