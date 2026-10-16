# bpy.types.ID: make_local

make_local ( * , clear_proxy = True , clear_liboverride = False , clear_asset_data = True )

Make this data-block local and hand it back; when the data also has indirect users the returned block may be a fresh copy.

Parameters :

- clear_proxy ( bool ) – Deprecated, has no effect (optional)

- clear_liboverride ( bool ) – Remove potential library override data from the newly made local data (optional)

- clear_asset_data ( bool ) – Remove potential asset metadata so the newly local data-block is not treated as asset data-block and won't show up in asset libraries (optional)

Returns :

This ID, or the new ID if it was copied

Return type :

ID

[Related references](INDEX.md).
