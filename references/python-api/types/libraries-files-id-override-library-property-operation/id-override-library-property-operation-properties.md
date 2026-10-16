# bpy.types.IDOverrideLibraryPropertyOperation: properties

flag

Status flags (default set(), readonly)

- MANDATORY
Mandatory – On templates, stops the user deleting a predefined operation (NOT USED).

- LOCKED
Locked – Stops the user from changing this override operation (NOT USED).

- `IDPOINTER_MATCH_REFERENCE`
Match Reference – Whatever ID pointer this operation overrides should line up with the reference hierarchy.

- `IDPOINTER_ITEM_USE_ID`
ID Item Use ID Pointer – For RNA collections of IDs only, where the item is referenced by its ID pointer itself rather than just its name.

Type :

set[Literal['MANDATORY', 'LOCKED', '`IDPOINTER_MATCH_REFERENCE`', '`IDPOINTER_ITEM_USE_ID`']]
operation

What override operation is performed (default 'REPLACE' , readonly)

- NOOP
No-Op – A do-nothing entry that blocks real overrides from being added (NOT USED).

- REPLACE
Replace – Swap the reference value out for the overriding one.

- `DIFF_ADD`
Differential – Records and applies the difference between the reference and local value (NOT USED).

- `DIFF_SUB`
Differential – Records and applies the difference between the reference and local value (NOT USED).

- `FACT_MULTIPLY`
Factor – Records and applies a multiplication factor between the reference and local value (NOT USED).

- `INSERT_AFTER`
Insert After – Drop a fresh item into the collection just past the one named in subitem_reference_name/_id or _index.

- `INSERT_BEFORE`
Insert Before – Drop a fresh item into the collection just ahead of the one named in subitem_reference_name/_id or _index (NOT USED).

Type :

Literal['NOOP', 'REPLACE', '`DIFF_ADD`', '`DIFF_SUB`', '`FACT_MULTIPLY`', '`INSERT_AFTER`', '`INSERT_BEFORE`']
subitem_local_id

For ID collections only, this tells apart same-named IDs that come from separate libraries (readonly)

Type :

ID
subitem_local_index

Helps track edits made within the collection (in [-1, inf], default -1, readonly)

Type :

int
subitem_local_name

Helps track edits made within the collection (default "", readonly, never None)

Type :

str
subitem_reference_id

For ID collections only, this tells apart same-named IDs that come from separate libraries (readonly)

Type :

ID
subitem_reference_index

Helps track edits made within the collection (in [-1, inf], default -1, readonly)

Type :

int
subitem_reference_name

Helps track edits made within the collection (default "", readonly, never None)

Type :

str

[Related references](INDEX.md).
