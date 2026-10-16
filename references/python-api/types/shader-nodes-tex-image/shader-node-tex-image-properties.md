# bpy.types.ShaderNodeTexImage: properties

color_mapping

Color mapping settings (readonly, never None)

Type :

ColorMapping
extension

How the image is extrapolated past its original bounds (default 'REPEAT' )

- REPEAT
Repeat – Cause the image to repeat horizontally and vertically.

- EXTEND
Extend – Extend by repeating edge pixels of the image.

- CLIP
Clip – Clip to image size and set exterior pixels as transparent.

- MIRROR
Mirror – Repeatedly flip the image horizontally and vertically.

Type :

Literal[‘REPEAT’, ‘EXTEND’, ‘CLIP’, ‘MIRROR’]
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

Method to project 2D image on object with a 3D texture vector (default 'FLAT' )

- FLAT
Flat – Image is projected flat using the X and Y coordinates of the texture vector.

- BOX
Box – Image is projected using different components for each side of the object space bounding box.

- SPHERE
Sphere – Image is projected spherically using the Z axis as central.

- TUBE
Tube – Image is projected from the tube using the Z axis as central.

Type :

Literal[‘FLAT’, ‘BOX’, ‘SPHERE’, ‘TUBE’]
projection_blend

For box projection, amount of blend to use between sides (in [0, 1], default 0.0)

Type :

float
texture_mapping

Texture coordinate mapping settings (readonly, never None)

Type :

TexMapping

[Related references](INDEX.md).
