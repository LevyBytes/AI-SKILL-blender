# Grease Pencil Material Properties: Fill, Settings

### Fill

The Fill component takes care of rendering closed stroke regions.

Style
Sets the fill's shading.

Solid :

One flat base color.

Gradient :

A blend running between two colors.

Gradient Type

Linear :

Blends along one axis.

Radial :

Blends outward from a center point.

Texture :

An image texture.

Image
The image data-block feeding the fill texture.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Solid  | Gradient (Linear)  | Gradient (Radial)  | Texture  |

Base Color
Primary fill color.

Secondary Color Gradient
Secondary color used for gradients.

Holdout
Turns the fill into a mask that strips color from the strokes beneath it.

Blend Gradient / Texture
Controls mixing between Base Color and the gradient or texture.

Flip Colors Gradient
Swaps Base and Secondary colors.

Location X, Y Gradient / Texture
Offsets gradient or texture coordinates.

Rotation Gradient / Texture
Rotates the gradient or texture mapping.

Scale X, Y Gradient / Texture
Scales the gradient or texture mapping.

Clip Image Texture
Prevents texture tiling when enabled.

### Settings

Pass Index
A custom integer ID you can feed into modifiers and compositing. It lets you single out specific materials within Grease Pencil Modifiers.

[Related references](INDEX.md).
