# bpy_extras.io_utils: bpy_extras.io_utils. unique_name ( key , name , name_dict , name_max = -1 , clean_func = None , sep = '.' )

bpy_extras.io_utils. unique_name ( key , name , name_dict , name_max = -1 , clean_func = None , sep = '.' ) 

Helper for keeping unique names, which may have special characters
removed and be capped at a maximum length.

Parameters :

- key ( Any ) – Unique item this name belongs to, name_dict[key] will be reused
when available.
This can be the object, mesh, material, etc instance itself.
Any hashable object associated with the name .

- name ( str ) – The name used to create a unique value in name_dict .

- name_dict ( dict [ Any , str ] ) – This is used to cache namespace to ensure no collisions
occur, this should be an empty dict initially and only modified by this
function.

- name_max ( int ) – Maximum length of the name. When -1 the name is unlimited.

- clean_func ( Callable [ [ str ] , str ] | None ) – Function to call on name before creating a unique value.

- sep ( str ) – Separator to use when between the name and a number when a
duplicate name is found.

Returns :

A unique name.

Return type :

str

[Related references](INDEX.md).
