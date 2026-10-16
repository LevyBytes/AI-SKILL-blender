# bpy.types.bpy_prop

as_bytes ( )

Hands back this string property encoded as bytes rather than as a Python str.

Returns :

The string as bytes.

Return type :

bytes
path_from_id ( )

Gives the data path that leads from the owning ID down to this property (as a string).

Returns :

The path from bpy.types.bpy_struct.id_data to this property.

Return type :

str
path_from_module ( )

Builds the complete data path to this struct, expressed as a string starting at the bpy module.

Returns :

The full path to the data.

Return type :

str

Raises :

ValueError – if the input data cannot be converted into a full data path.

Note

Even if all input data is correct, this function might
error out because Blender cannot derive a valid path.
The incomplete path will be printed in the error message.
update ( )

Fires the property's update callback.

Note

Assigning a property already triggers this, but on rare occasions
calling it directly is handy.
data

The bpy.types.bpy_struct that this property belongs to.
id_data

The bpy.types.ID object this data-block is from or None, (not available for all data types) (readonly)

Type :

bpy.types.ID
rna_type

Property type information exposed for introspection.
class bpy.types. bpy_prop

The built-in base from which every property class derives.
## bpy_prop

### bpy_prop

[Related references](INDEX.md).
