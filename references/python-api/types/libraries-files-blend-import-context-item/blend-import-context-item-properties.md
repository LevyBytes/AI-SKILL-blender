# bpy.types.BlendImportContextItem: properties

## BlendImportContextItem(bpy_struct)

### BlendImportContextItem(bpy_struct)

base class: bpy_struct
class bpy.types.BlendImportContextItem(bpy_struct)

Represents one data-block entry held inside a BlendImportContext. For now it is available solely as read-only information passed to the pre- and post-linking handlers.
append_action

Records the way the append operation treated this entry. Populated only when the data was in fact appended (default 'UNSET', readonly)

- UNSET
Not yet defined.

- `KEEP_LINKED`
ID has been kept linked.

- `REUSE_LOCAL`
An existing matching local ID has been re-used.

- `MAKE_LOCAL`
The newly linked ID has been made local.

- `COPY_LOCAL`
The linked ID had other unrelated usages, so it has been duplicated into a local copy.

Type:
Literal['UNSET', '`KEEP_LINKED`', '`REUSE_LOCAL`', '`MAKE_LOCAL`', '`COPY_LOCAL`']
id

The ID that was imported. Stays None until linking or appending occurs. When appended, it can be identical to reusable_local_id (readonly)

Type:
ID
id_type

Which ID category this entry belongs to (default 'ACTION', readonly)

Type:
Literal[Id Type Items]
import_info

Assorted status details describing an entry once its import has finished (default set(), readonly)

- `INDIRECT_USAGE`
That item was added for an indirectly imported ID, as a dependency of another data-block.

- `LIBOVERRIDE_DEPENDENCY`
That item represents an ID also used as liboverride dependency (either directly, as a liboverride reference, or indirectly, as data used by a liboverride reference). It should never be directly made local. Mutually exclusive with `LIBOVERRIDE_DEPENDENCY`.

- `LIBOVERRIDE_DEPENDENCY_ONLY`
That item represents an ID only used as liboverride dependency (either directly or indirectly, see `LIBOVERRIDE_DEPENDENCY` for precisions). It should not be considered during the 'make local' (append) process, and remain purely linked data. Mutually exclusive with `LIBOVERRIDE_DEPENDENCY`.

Type:
set[Literal['`INDIRECT_USAGE`', '`LIBOVERRIDE_DEPENDENCY`', '`LIBOVERRIDE_DEPENDENCY_ONLY`']]
library_override_id

The library override generated for the linked ID. Remains None until one is produced (readonly)

Type:
ID
name

ID name of the item (default "", readonly, never None)

Type:
str
reusable_local_id

A pre-existing local ID eligible for reuse in the append-and-reuse scenario. Stays None until such a match is located (readonly)

Type:
ID
source_libraries

The ordered set of libraries searched for this ID; it is pulled from the first file in the sequence that holds it (default None, readonly)

Type:
BlendImportContextLibraries[BlendImportContextLibrary]
source_library

The Library ID identifying the blendfile the ID came from. Remains None until the ID has been linked or appended (readonly)

Type:
Library

[Related references](INDEX.md).
