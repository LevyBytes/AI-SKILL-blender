# bpy.ops.poselib.blend_pose_asset

bpy.ops.poselib. blend_pose_asset ( * , asset_library_type = 'LOCAL' , asset_library_identifier = '' , relative_asset_identifier = '' , blend_factor = 0.0 , flipped = False , release_confirm = False ) 

Mix the provided Pose Action with the rig's current configuration

Parameters :

- asset_library_type (Literal[Asset Library Type Items]) – Asset Library Type, (optional)

- asset_library_identifier ( str ) – Asset Library Identifier, (optional, never None)

- relative_asset_identifier ( str ) – Relative Asset Identifier, (optional, never None)

- blend_factor ( float ) – Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it (in [-inf, inf], optional)

- flipped ( bool ) – Apply Flipped, When enabled, applies the pose flipped over the X-axis (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
