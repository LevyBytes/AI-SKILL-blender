# Alpha Convert Node

## Alpha Convert Node

The Alpha Convert node changes an image's alpha-channel format. In Blender, Premultiplied Alpha is the standard for compositing and rendering — render layers are premultiplied, and images loaded for rendering or compositing are converted to it. To do a compositing operation with straight alpha (typically a color-correction step that works better on RGB without alpha), use this node, and convert back to premultiplied before the Group Output node to avoid artifacts. Inputs: Image (standard color input) and Type, the conversion direction (see Alpha Channel for the difference) — To Premultiplied (Straight → Premultiplied) or To Straight (Premultiplied → Straight). Output: Image (standard color output).

[Related references](INDEX.md).
