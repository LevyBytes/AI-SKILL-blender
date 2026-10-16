# bpy.types.CompositorNodeSeparateColor: properties

## CompositorNodeSeparateColor(CompositorNode)

### CompositorNodeSeparateColor(CompositorNode)

base classes — bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeSeparateColor ( CompositorNode )

Breaks an image apart into the separate channels that make up its color.
mode

Mode of color processing (default 'RGB' )

- RGB
RGB – Use RGB (Red, Green, Blue) color processing.

- HSV
HSV – Use HSV (Hue, Saturation, Value) color processing.

- HSL
HSL – Use HSL (Hue, Saturation, Lightness) color processing.

- YCC
YCbCr – Use YCbCr (Y - luma, Cb - blue-difference chroma, Cr - red-difference chroma) color processing.

- YUV
YUV – Use YUV (Y - luma, U V - chroma) color processing.

Type :

Literal[‘RGB’, ‘HSV’, ‘HSL’, ‘YCC’, ‘YUV’]
ycc_mode

Color space used for YCbCrA processing (default 'ITUBT601' )

Type :

Literal[‘ITUBT601’, ‘ITUBT709’, ‘JFIF’]

[Related references](INDEX.md).
