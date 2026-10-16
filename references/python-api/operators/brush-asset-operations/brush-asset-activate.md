# bpy.ops.brush.asset_activate

bpy.ops.brush. asset_activate ( * , asset_library_type = 'LOCAL' , asset_library_identifier = '' , relative_asset_identifier = '' , use_toggle = False )

Make a brush asset the active sculpting or painting tool

Parameters :

- asset_library_type (Literal[Asset Library Type Items]) – Asset Library Type, (optional)

- asset_library_identifier ( str ) – Asset Library Identifier, (optional, never None)

- relative_asset_identifier ( str ) – Relative Asset Identifier, (optional, never None)

- use_toggle ( bool ) – Toggle, Alternate between the current and newly assigned brushes on successive clicks. (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
