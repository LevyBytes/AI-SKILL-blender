# bpy.types.BlendData: orphans_purge

orphans_purge ( ) 

Erase all IDs that have no references.

Parameters :

- do_local_ids ( bool , optional ) – Include unused local IDs in the deletion, defaults to True

- do_linked_ids ( bool , optional ) – Include unused linked IDs in the deletion, defaults to True

- do_recursive ( bool , optional ) – Recursively check for unused IDs, ensuring no orphaned one remain after a single run of that function, defaults to False

Returns :

The number of deleted IDs.

Return type :

int

[Related references](INDEX.md).
