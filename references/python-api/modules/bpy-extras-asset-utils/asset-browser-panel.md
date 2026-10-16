# bpy_extras.asset_utils.AssetBrowserPanel

class bpy_extras.asset_utils. AssetBrowserPanel 

Mixin for panels meant to appear only within the asset browser.
classmethod asset_browser_panel_poll ( context ) 

Determine whether the panel ought to appear in the asset browser.

Parameters :

context (bpy.types.Context) – The context.

Returns :

True when the panel should be visible.

Return type :

bool
classmethod poll ( context ) 

Poll for asset browser visibility.

Parameters :

context (bpy.types.Context) – The context.

Returns :

True when the panel should be visible.

Return type :

bool

[Related references](INDEX.md).
