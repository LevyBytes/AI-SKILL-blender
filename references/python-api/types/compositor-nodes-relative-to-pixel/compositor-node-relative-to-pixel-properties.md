# bpy.types.CompositorNodeRelativeToPixel: properties

## CompositorNodeRelativeToPixel(CompositorNode)

### CompositorNodeRelativeToPixel(CompositorNode)

base classes — bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeRelativeToPixel ( CompositorNode )

Translates quantities expressed as a fraction of the image dimensions into actual pixel counts.
data_type

The type of data (default 'FLOAT' )

- FLOAT
Float – Float value.

- VECTOR
Vector – Vector value.

Type :

Literal[‘FLOAT’, ‘VECTOR’]
reference_dimension

Picks which image dimension the relative value is measured against (default 'X' )

- `PER_DIMENSION`
Per Dimension – The value is relative to each of the dimensions of the image independently.

- X
X – The value is relative to the X dimension of the image.

- Y
Y – The value is relative to the Y dimension of the image.

- Greater
Greater – The value is relative to the greater dimension of the image.

- Smaller
Smaller – The value is relative to the smaller dimension of the image.

- Diagonal
Diagonal – The value is relative to the diagonal of the image.

Type :

Literal[‘`PER_DIMENSION`’, ‘X’, ‘Y’, ‘Greater’, ‘Smaller’, ‘Diagonal’]

[Related references](INDEX.md).
