# bpy.types.GreasePencilDrawing: properties

## GreasePencilDrawing(bpy_struct)

### GreasePencilDrawing(bpy_struct)

base class: bpy_struct
class bpy.types. GreasePencilDrawing ( bpy_struct )

A Grease Pencil drawing
attributes

Geometry attributes (default None, readonly)

Type :

AttributeGroupGreasePencilDrawing[Attribute]
color_attributes

Geometry color attributes (default None, readonly)

Type :

AttributeGroupGreasePencilDrawing[Attribute]
curve_offsets

Offset indices of the first point of each curve (default None, readonly)

Type :

bpy_prop_collection[IntAttributeValue]
type

Drawing type (default 'DRAWING' , readonly)

Type :

Literal[‘DRAWING’, ‘REFERENCE’]
user_count

Count of keyframes that make use of this drawing (in [-inf, inf], default 0, readonly)

Type :

int

strokes

Return a collection of all the Grease Pencil strokes in this drawing.

Note

This API should not be used for performance critical operations.
Use the GreasePencilDrawing.attributes API instead.

Note

When point/curves count of a drawing is changed, the slice returned by this
call prior to the change is no longer valid. You need to get the new stroke
slice via drawing.strokes[n] .

(readonly)

[Related references](INDEX.md).
