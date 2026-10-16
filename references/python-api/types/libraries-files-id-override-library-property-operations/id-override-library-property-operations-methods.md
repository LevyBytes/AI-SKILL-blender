# bpy.types.IDOverrideLibraryPropertyOperations: methods

add ( operation , * , use_id = False , subitem_reference_name = '' , subitem_local_name = '' , subitem_reference_id = None , subitem_local_id = None , subitem_reference_index = -1 , subitem_local_index = -1 )

Append a fresh operation.

Parameters :

- operation ( Literal [ 'NOOP' , 'REPLACE' , '`DIFF_ADD`' , '`DIFF_SUB`' , '`FACT_MULTIPLY`' , '`INSERT_AFTER`' , '`INSERT_BEFORE`' ] ) – Operation, Which override operation to carry out

- NOOP
No-Op – A placeholder that performs nothing and keeps real overrides from being added (NOT USED).

- REPLACE
Replace – Swap the reference value out for the overriding one.

- `DIFF_ADD`
Differential – Keeps, then reapplies, the gap between the reference and local value (NOT USED).

- `DIFF_SUB`
Differential – Keeps, then reapplies, the gap between the reference and local value (NOT USED).

- `FACT_MULTIPLY`
Factor – Keeps, then reapplies, a multiplier relating the reference and local value (NOT USED).

- `INSERT_AFTER`
Insert After – Place a new collection item just past the one named in subitem_reference_name/_id or _index.

- `INSERT_BEFORE`
Insert Before – Place a new collection item just ahead of the one named in subitem_reference_name/_id or _index (NOT USED).

- use_id ( bool ) – Use ID Pointer Subitem, Whether the matched or newly made liboverride operation relies on ID pointers (optional)

- subitem_reference_name ( str ) – Subitem Reference Name, Drives insertion or ID swapping within the collection (optional, never None)

- subitem_local_name ( str ) – Subitem Local Name, Drives insertion or ID swapping within the collection (optional, never None)

- subitem_reference_id (ID) – Subitem Reference ID, Drives ID swapping within the collection (optional)

- subitem_local_id (ID) – Subitem Local ID, Drives ID swapping within the collection (optional)

- subitem_reference_index ( int ) – Subitem Reference Index, Drives insertion or ID swapping within the collection (in [-1, inf], optional)

- subitem_local_index ( int ) – Subitem Local Index, Drives insertion or ID swapping within the collection (in [-1, inf], optional)

Returns :

New Operation, Created operation

Return type :

IDOverrideLibraryPropertyOperation
remove ( operation )

Delete a given operation and discard it.

Parameters :

operation (IDOverrideLibraryPropertyOperation) – Operation, Override operation to be deleted
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
