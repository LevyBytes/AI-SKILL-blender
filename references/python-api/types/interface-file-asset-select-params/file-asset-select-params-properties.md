# bpy.types.FileAssetSelectParams: properties

## FileAssetSelectParams(FileSelectParams)

### FileAssetSelectParams(FileSelectParams)

base classes: bpy_struct, FileSelectParams
class bpy.types. FileAssetSelectParams ( FileSelectParams )

The file-selection settings used while the browser is in Asset Browser mode.
asset_library_reference

(default 'ALL' )

- ALL
All Libraries – Pull in assets from every asset library that is listed.

- LOCAL
Current File – Show only the assets present in this Blender session right now.

- ESSENTIALS
Essentials – Show the core building blocks and utilities shipped with Blender.

- CUSTOM
Custom – Show assets from the asset libraries set up in the Preferences.

Type :

Literal[‘ALL’, ‘LOCAL’, ‘ESSENTIALS’, ‘CUSTOM’]
catalog_id

UUID of the catalog currently displayed in the browser (default “”, never None)

Type :

str
filter_asset_id

Controls which asset types appear or stay hidden while an asset library is being browsed (readonly, never None)

Type :

FileAssetSelectIDFilter
import_method

Decides the way the asset gets imported (default 'LINK' )

- `FOLLOW_PREFS`
Follow Preferences – Adopt the import method set in the Preferences for this asset library rather than overriding it here in the Asset Browser.

- LINK
Link – Bring the asset in as a linked data-block.

- APPEND
Append – Bring the asset in as a copied data-block that keeps no tie to the original asset data-block.

- `APPEND_REUSE`
Append (Reuse Data) – Bring the asset in as a copied data-block while sidestepping duplicate copies of nested, usually heavy data. A material asset's textures, say, or an object asset's mesh, need not be duplicated on each import; the asset's instances share that underlying data instead.

- PACK
Pack – Bring the asset in as a linked data-block and pack it into the current file (so it stays intact even if the library data changes, goes missing, and so on).

Type :

Literal[‘`FOLLOW_PREFS`’, ‘LINK’, ‘APPEND’, ‘`APPEND_REUSE`’, ‘PACK’]
instance_collections_on_append

On append, spawn instances for collections rather than dropping them straight into the scene (default False)

Type :

bool
instance_collections_on_link

On link, spawn instances for collections rather than dropping them straight into the scene (default False)

Type :

bool

[Related references](INDEX.md).
