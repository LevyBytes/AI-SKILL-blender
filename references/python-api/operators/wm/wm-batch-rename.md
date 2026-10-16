# bpy.ops.wm.batch_rename

bpy.ops.wm. batch_rename ( * , data_type = 'OBJECT' , data_source = 'SELECT' , actions = None ) 

Changes names of multiple components concurrently

Parameters :

- data_type ( Literal [ 'OBJECT' , 'COLLECTION' , 'MATERIAL' , 'MESH' , 'CURVE' , 'META' , 'VOLUME' , 'GREASEPENCIL' , 'ARMATURE' , 'LATTICE' , 'LIGHT' , '`LIGHT_PROBE`' , 'CAMERA' , 'SPEAKER' , 'BONE' , 'NODE' , '`SEQUENCE_STRIP`' , '`ACTION_CLIP`' , 'SCENE' , 'BRUSH' ] ) - Type, Category of component to rename (optional)

- data_source ( Literal [ 'SELECT' , 'ALL' ] ) - Source, (optional)

- actions ( bpy_prop_collection [ BatchRenameAction ]) - actions, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:3283

[Related references](INDEX.md).
