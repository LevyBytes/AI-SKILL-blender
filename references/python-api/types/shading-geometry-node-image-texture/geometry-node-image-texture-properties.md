# bpy.types.GeometryNodeImageTexture: properties

## GeometryNodeImageTexture(GeometryNode)

### GeometryNodeImageTexture(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeImageTexture ( GeometryNode )

Look up colors and values stored in an image texture.
extension

What happens to samples taken outside the image's native area (default 'REPEAT' )

- REPEAT
Repeat – Tile the image so it recurs across both axes.

- EXTEND
Extend – Stretch the outermost edge pixels outward.

- CLIP
Clip – Restrict to the image footprint, leaving anything outside it transparent.

- MIRROR
Mirror – Tile the image while alternately mirroring it on each axis.

Type :

Literal[‘REPEAT’, ‘EXTEND’, ‘CLIP’, ‘MIRROR’]
interpolation

How values get blended across neighboring pixels (default 'Linear' )

- Linear
Linear – Blend neighboring texels linearly.

- Closest
Closest – Snap to the nearest texel with no blending.

- Cubic
Cubic – Blend texels with a cubic curve.

Type :

Literal[‘Linear’, ‘Closest’, ‘Cubic’]

[Related references](INDEX.md).
