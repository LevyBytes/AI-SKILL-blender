# bpy.types.AssetShelf: bl_activate_operator, bl_default_preview_size, bl_drag_operator, bl_idname, bl_options, bl_space_type

bl_activate_operator

Operator to call when activating an item with asset reference properties (default "", never None)

Type :

str
bl_default_preview_size

Default size of the asset preview thumbnails in pixels (in [32, 256], default 0)

Type :

int
bl_drag_operator

Operator to call when dragging an item with asset reference properties (default "", never None)

Type :

str
bl_idname

If this is set, the asset gets a custom ID, otherwise it takes the name of the class used to define the asset (for example, if the class name is "`OBJECT_AST`_hello", and bl_idname is not set by the script, then bl_idname = "`OBJECT_AST`_hello") (default "", never None)

Type :

str
bl_options

Options for this asset shelf type (default set())

- `NO_ASSET_DRAG`
No Asset Dragging – Disable the default asset dragging on drag events. Useful for implementing custom dragging via custom key-map items..

- `DEFAULT_VISIBLE`
Visible by Default – Unhide the asset shelf when it's available for the first time, otherwise it will be hidden.

- `STORE_ENABLED_CATALOGS_IN_PREFERENCES`
Store Enabled Catalogs in Preferences – Store the shelf's enabled catalogs in the preferences rather than the local asset shelf settings.

- `ACTIVATE_FOR_CONTEXT_MENU`
When spawning a context menu for an asset, activate the asset and call `bl_activate_operator` if present, rather than just highlighting the asset.

Type :

set[Literal['`NO_ASSET_DRAG`', '`DEFAULT_VISIBLE`', '`STORE_ENABLED_CATALOGS_IN_PREFERENCES`', '`ACTIVATE_FOR_CONTEXT_MENU`']]
bl_space_type

The space where the asset shelf will show up in. Ignored for popup asset shelves which can be displayed in any space. (default 'EMPTY' )

Type :

Literal[Space Type Items]

[Related references](INDEX.md).
