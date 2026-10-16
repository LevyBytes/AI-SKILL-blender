# Environment Texture Node

## Environment Texture Node

### Environment Texture Node

The Environment Texture node lights your scene from an environment-map image used as a texture.

### Inputs

Vector
Coordinate for the texture look-up. Left unconnected, the image wraps as an environment with the Z axis pointing up.

### Properties

Image
Image data-block serving as the image source. More settings sit in Sidebar ‣ Item ‣ Properties : these cover the alpha channel along with extra colour-space options. Those extra options are written up alongside the rest of
Common Image Settings.

Color Space
What kind of data the image holds, either Color or Non-Color Data. Most colour textures want the Color default, but for something like a bump or alpha map the pixels should read as Non-Color Data so no unwanted colour-space conversion creeps in.

Which colour spaces are listed depends on the active OCIO config. The defaults are spelled out here:
Default OpenColorIO Configuration

Texture Interpolation
Which interpolation the environment texture is sampled with. The available options:

Linear :

Regular quality interpolation.

Closest :

No interpolation, use closest pixel.

Cubic :

Smoother, better quality interpolation.

Smart :

Bicubic when magnifying, otherwise Bilinear is used.
This is only available for OSL.

Projection Method
Lets you pick among different kinds of environment map. The supported choices:

Equirectangular :

Projection from an Equirectangular photo.

Mirror Ball :

Projection from an orthographic photo or mirror ball.

### Outputs

Color
RGB color from the image.

### Examples

HDR image from OpenFootage.net.

[Related references](INDEX.md).
