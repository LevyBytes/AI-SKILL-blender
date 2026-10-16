# bpy.ops.uv.lightmap_pack

bpy.ops.uv. lightmap_pack ( * , `PREF_CONTEXT` = '`SEL_FACES`' , `PREF_PACK_IN_ONE` = True , `PREF_NEW_UVLAYER` = False , `PREF_BOX_DIV` = 12 , `PREF_MARGIN_DIV` = 0.1 ) 

Fits the UVs of each face inside the UV bounds

Parameters :

- `PREF_CONTEXT` ( Literal [ '`SEL_FACES`' , '`ALL_FACES`' ] ) – Selection, (optional)

- `SEL_FACES`
Selected Faces – Restrict packing to the selected faces.

- `ALL_FACES`
All Faces – Pack every face the mesh contains.

- `PREF_PACK_IN_ONE` ( bool ) – Share Texture Space, Objects share texture space, map all objects into a single UV map (optional)

- `PREF_NEW_UVLAYER` ( bool ) – New UV Map, Create a new UV map for every mesh packed (optional)

- `PREF_BOX_DIV` ( int ) – Pack Quality, Quality of the packing. Higher values will be slower but waste less space (in [1, 48], optional)

- `PREF_MARGIN_DIV` ( float ) – Margin, Size of the margin as a division of the UV (in [0.001, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/uvcalc_lightmap.py:664

[Related references](INDEX.md).
