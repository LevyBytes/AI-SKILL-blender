# bpy.types.UIList: filter_items

filter_items ( context , data , property )

Filter and/or re-order items of the collection (output filter results in filter_flags, and reorder results in filter_neworder arrays)

Parameters :

- data (AnyType) – Data from which to take Collection property

- property ( str ) – Identifier of property in data, for the collection (never None)

Returns :

filter_flags , An array of filter flags, one for each item in the collection (NOTE: The upper 16 bits, including `FILTER_ITEM`, are reserved, only use the lower 16 bits for custom usages), bpy_prop_array[int]

filter_neworder , An array of indices, one for each item in the collection, mapping the org index to the new one, bpy_prop_array[int]

Return type :

tuple[bpy_prop_array[int], bpy_prop_array[int]]

[Related references](INDEX.md).
