# bpy_extras.asset_utils.SpaceAssetInfo

class bpy_extras.asset_utils. SpaceAssetInfo 

Helper for testing whether a space happens to be an asset browser.
classmethod is_asset_browser ( space_data ) 

Determine whether the supplied space is an asset browser.

Parameters :

space_data (bpy.types.Space) – The space to check.

Returns :

True when the space is an asset browser.

Return type :

bool
classmethod is_asset_browser_poll ( context ) 

Poll whether the active space is an asset browser.

Parameters :

context (bpy.types.Context) – The context.

Returns :

True when the active space is an asset browser.

Return type :

bool

[Related references](INDEX.md).
