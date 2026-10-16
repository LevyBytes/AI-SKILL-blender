# bpy.types.TextureSlot: properties

## TextureSlot(bpy_struct)

### TextureSlot(bpy_struct)

base class — bpy_struct

subclasses —
BrushTextureSlot, LineStyleTextureSlot, ParticleSettingsTextureSlot
class bpy.types. TextureSlot ( bpy_struct )

A slot that maps a texture and sets how strongly it contributes
blend_type

How the texture gets blended in (default 'MIX' )

Type :

Literal[‘MIX’, ‘DARKEN’, ‘MULTIPLY’, ‘LIGHTEN’, ‘SCREEN’, ‘ADD’, ‘OVERLAY’, ‘`SOFT_LIGHT`’, ‘`LINEAR_LIGHT`’, ‘DIFFERENCE’, ‘SUBTRACT’, ‘DIVIDE’, ‘HUE’, ‘SATURATION’, ‘COLOR’, ‘VALUE’]
color

Fallback color used when a texture gives no RGB, or while RGB-to-intensity is on (array of 3 items, in [0, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Color
default_value

The value applied to Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard (in [-inf, inf], default 1.0)

Type :

float
name

Name of the texture slot (default “”, readonly, never None)

Type :

str
offset

Small adjustment to where the texture maps on X, Y and Z (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
output_node

For node-based textures, which output node feeds this slot (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]
scale

Sizing applied to the texture along X, Y and Z (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Vector
texture

The texture data-block this slot points at

Type :

Texture

[Related references](INDEX.md).
