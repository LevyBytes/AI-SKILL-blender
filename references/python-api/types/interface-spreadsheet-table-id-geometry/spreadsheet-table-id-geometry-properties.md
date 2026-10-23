# bpy.types.SpreadsheetTableIDGeometry: properties

## SpreadsheetTableIDGeometry(SpreadsheetTableID)

### SpreadsheetTableIDGeometry(SpreadsheetTableID)

base classes: bpy_struct, SpreadsheetTableID
class bpy.types. SpreadsheetTableIDGeometry ( SpreadsheetTableID )
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)
attribute_domain

The attribute domain that is shown (default 'POINT' , readonly)

Type :

Literal[Attribute Domain Items]
geometry_component_type

Which portion of the geometry supplies the displayed data (default 'MESH' , readonly)

Type :

Literal[Geometry Component Type Items]
geometry_item_type

Item Type (default 'DOMAIN' , readonly)

- DOMAIN
Domain – Data on a domain.

- BUNDLE
Bundle – Data on a bundle.

Type :

Literal[‘DOMAIN’, ‘BUNDLE’]
layer_index

Which Grease Pencil layer this indexes (in [-inf, inf], default 0, readonly)

Type :

int
object_eval_state

(default 'EVALUATED' , readonly)

- EVALUATED
Evaluated – Pull data from an object that is fully or partially evaluated.

- ORIGINAL
Original – Pull data from the original object, with no modifiers in effect.

- `VIEWER_NODE`
Viewer Node – Pull intermediate data from the viewer node.

Type :

Literal[‘EVALUATED’, ‘ORIGINAL’, ‘`VIEWER_NODE`’]
viewer_path

Path leading to the data being shown (readonly)

Type :

ViewerPath

[Related references](INDEX.md).
