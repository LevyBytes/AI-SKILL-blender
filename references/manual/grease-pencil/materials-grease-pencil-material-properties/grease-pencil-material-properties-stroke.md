# Grease Pencil Material Properties: Stroke

### Stroke

The Stroke component decides how the line itself is rendered.

Line Type
Picks the way stroke geometry is drawn.

Line :

A solid line links the stroke points together.

Dots :

Plants a circle at every stroke point, leaving them unjoined.

Squares :

Plants a square at every stroke point, leaving them unjoined.

Style
Sets the stroke's shading.

Solid :

A single flat base color.

Texture :

An image texture wrapped along the stroke.

Image
The image data-block feeding the texture.

Blend
Mix factor between the texture and the Base Color.

UV Factor
Scales the texture across the stroke's length.

Base Color
The stroke's main color.

Holdout
Makes the stroke behave as a mask, cutting color from any strokes and fills below.

Alignment
Sets how Dots and Squares are oriented.

Path :

Follows both the drawing direction and the object's rotation.

Object :

Follows the object's rotation alone.

Fixed :

Locks to screen space.

Rotation
Turns the Dots or Squares shapes, held within -90° to 90°.

Self Overlap
Decides how a stroke's own overlapping parts blend, an effect most visible on semi-transparent materials.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Line / Solid  | Line / Texture  | Dot / Solid  | Dot / Texture  |

[Related references](INDEX.md).
