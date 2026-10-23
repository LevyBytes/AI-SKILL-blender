# bpy.types.ShaderNodeTexEnvironment: properties

## ShaderNodeTexEnvironment(ShaderNode)

### ShaderNodeTexEnvironment(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexEnvironment ( ShaderNode )

Reads an image file as an environment texture, most often paired with the Background node to light a scene.
color_mapping

Color mapping settings (readonly, never None)

Type :

ColorMapping
image

Type :

Image
image_user

Parameters defining which layer, pass and frame of the image is displayed (readonly, never None)

Type :

ImageUser
interpolation

Texture interpolation (default 'Linear' )

- Linear
Linear – Linear interpolation.

- Closest
Closest – No interpolation (sample closest texel).

- Cubic
Cubic – Cubic interpolation.

- Smart
Smart – Bicubic when magnifying, else bilinear (OSL only).

Type :

Literal[‘Linear’, ‘Closest’, ‘Cubic’, ‘Smart’]
projection

Projection of the input image (default 'EQUIRECTANGULAR' )

- EQUIRECTANGULAR
Equirectangular – Equirectangular or latitude-longitude projection.

- `MIRROR_BALL`
Mirror Ball – Projection from an orthographic photo of a mirror ball.

Type :

Literal[‘EQUIRECTANGULAR’, ‘`MIRROR_BALL`’]
texture_mapping

Texture coordinate mapping settings (readonly, never None)

Type :

TexMapping

[Related references](INDEX.md).
