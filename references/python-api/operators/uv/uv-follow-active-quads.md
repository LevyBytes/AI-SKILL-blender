# bpy.ops.uv.follow_active_quads

bpy.ops.uv. follow_active_quads ( * , mode = '`LENGTH_AVERAGE`' ) 

Propagates UVs from the active quads through connected face loops

Parameters :

mode ( Literal [ 'EVEN' , 'LENGTH' , '`LENGTH_AVERAGE`' ] ) – Edge Length Mode, Method to space UV edge loops (optional)

- EVEN
Even – Give every UV the same spacing.

- LENGTH
Length – Space each loop's UVs by its average edge length.

- `LENGTH_AVERAGE`
Length Average – Space each loop's UVs by its average edge length.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/uvcalc_follow_active.py:302

[Related references](INDEX.md).
