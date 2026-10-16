# bpy.types.CompositorNodeCombineColor: properties

## CompositorNodeCombineColor(CompositorNode)

### CompositorNodeCombineColor(CompositorNode)

base classes — bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeCombineColor ( CompositorNode )

Assemble an image back together from its component color channels
mode

Which color-processing mode to use (default 'RGB' )

- RGB
RGB – Process colors with RGB (Red, Green, Blue).

- HSV
HSV – Process colors with HSV (Hue, Saturation, Value).

- HSL
HSL – Process colors with HSL (Hue, Saturation, Lightness).

- YCC
YCbCr – Process colors with YCbCr (Y - luma, Cb - blue-difference chroma, Cr - red-difference chroma).

- YUV
YUV – Process colors with YUV (Y - luma, U V - chroma).

Type :

Literal[‘RGB’, ‘HSV’, ‘HSL’, ‘YCC’, ‘YUV’]
ycc_mode

Which color space drives YCbCrA processing (default 'ITUBT601' )

Type :

Literal[‘ITUBT601’, ‘ITUBT709’, ‘JFIF’]

[Related references](INDEX.md).
