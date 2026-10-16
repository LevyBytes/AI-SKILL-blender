# bpy.types.bpy_struct: path_from_id, path_from_module, path_resolve

path_from_id ( property = '' , / )

Hands back the data path leading from the ID down to this object (as a string).

Parameters :

property ( str ) – Optional property name which can be used if the path is
to a property of this object.

Returns :

The path from bpy.types.bpy_struct.id_data
to this struct and property (when given).

Return type :

str
path_from_module ( property = '' , index = -1 , / )

Builds the complete data path to this struct, expressed as a string starting at the bpy module.

Parameters :

- property ( str ) – Optional property name to get the full path from

- index ( int ) – Optional index of the property.
"-1" means that the property has no indices.

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
path_resolve ( path , coerce = True , / )

Looks up the property at the given path, raising an exception if it cannot be found.

Parameters :

- path ( str ) – path which this property resolves.

- coerce ( bool ) – optional argument, when True, the property will be converted
into its Python representation.

Returns :

Property value or property object.

Return type :

Any | bpy.types.bpy_prop

[Related references](INDEX.md).
