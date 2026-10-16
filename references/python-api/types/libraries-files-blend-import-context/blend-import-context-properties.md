# bpy.types.BlendImportContext: properties

## BlendImportContext(bpy_struct)

### BlendImportContext(bpy_struct)

base class — bpy_struct
class bpy.types.BlendImportContext(bpy_struct)

Carries contextual state for an operation involving a blendfile's libraries or linked data. At present it is surfaced only as read-only information for the handlers that run before and after a blend import.
import_items

(default None, readonly)

Type:
BlendImportContextItems[BlendImportContextItem]
options

Flags governing how this blendfile import is carried out (default set(), readonly)

- LINK
Only link data, instead of appending it.

- `MAKE_PATHS_RELATIVE`
Make paths of used library blendfiles relative to current blendfile.

- `USE_PLACEHOLDERS`
Generate a placeholder (empty ID) if not found in any library files.

- `FORCE_INDIRECT`
Force loaded ID to be tagged as indirectly linked (used in reload context only).

- `APPEND_SET_FAKEUSER`
Set fake user on appended IDs.

- `APPEND_RECURSIVE`
Append (make local) also indirect dependencies of appended IDs coming from other libraries. NOTE: All IDs (including indirectly linked ones) coming from the same initial library are always made local.

- `APPEND_LOCAL_ID_REUSE`
Try to re-use previously appended matching IDs when appending them again, instead of creating local duplicates.

- `APPEND_ASSET_DATA_CLEAR`
Clear the asset data on append (it is always kept for linked data).

- `SELECT_OBJECTS`
Automatically select imported objects.

- `USE_ACTIVE_COLLECTION`
Use the active Collection of the current View Layer to instantiate imported collections and objects.

- `OBDATA_INSTANCE`
Instantiate object data IDs (i.e. create objects for them if needed).

- `COLLECTION_INSTANCE`
Instantiate collections as empties, instead of linking them into the current view layer.

Type:
set[Literal['LINK', '`MAKE_PATHS_RELATIVE`', '`USE_PLACEHOLDERS`', '`FORCE_INDIRECT`', '`APPEND_SET_FAKEUSER`', '`APPEND_RECURSIVE`', '`APPEND_LOCAL_ID_REUSE`', '`APPEND_ASSET_DATA_CLEAR`', '`SELECT_OBJECTS`', '`USE_ACTIVE_COLLECTION`', '`OBDATA_INSTANCE`', '`COLLECTION_INSTANCE`']]
process_stage

Which phase the import has reached at present (default 'INIT', readonly)

- INIT
Blendfile import context has been initialized and filled with a list of items to import, no data has been linked or appended yet.

- DONE
All data has been imported and is available in the list of "import_items".

Type:
Literal['INIT', 'DONE']

[Related references](INDEX.md).
