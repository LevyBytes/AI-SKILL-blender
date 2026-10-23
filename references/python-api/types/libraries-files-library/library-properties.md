# bpy.types.Library: properties

## Library(ID)

### Library(ID) 

base classes: bpy_struct, ID
class bpy.types. Library ( ID ) 

External .blend file from which data is linked
archive_libraries 

Archive libraries holding packed IDs, created and owned by this source library (default None, readonly)

Type :

bpy_prop_collection[Library]
archive_parent_library 

The source library that produced this archive of packed IDs (readonly)

Type :

Library
filepath 

Path to the library .blend file (default “”, never None, blend relative // prefix supported)

Type :

str
is_archive 

This library acts as an 'archive' store for packed linked IDs that were originally linked from its 'archive parent' library. (default False, readonly)

Type :

bool
is_editable 

Even though linked, this library's data-blocks may be edited. Used by brush assets along with what they depend on. (default False, readonly)

Type :

bool
needs_liboverride_resync 

True when this library holds library overrides linked into the current blendfile that needed a recursive resync at load time (opening and re-saving that library blendfile is advised) (default False)

Type :

bool
packed_file 

(readonly)

Type :

PackedFile
parent 

(readonly)

Type :

Library
version 

Blender version that wrote the library .blend (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
users_id 

The ID data-blocks that rely on this library

Type :

tuple[bpy.types.ID, …]

Note

Runs in O(n), with n being the count of every
linkable ID type found in bpy.data .

(readonly)

[Related references](INDEX.md).
