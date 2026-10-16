# bpy.ops.object.make_single_user

bpy.ops.object. make_single_user ( * , type = '`SELECTED_OBJECTS`' , object = False , obdata = False , material = False , animation = False , obdata_animation = False ) 

Break shared references so each object owns its data independently

Parameters :

- type ( Literal [ '`SELECTED_OBJECTS`' , 'ALL' ] ) – Type, (optional)

- object ( bool ) – Object, Make individual object instances (optional)

- obdata ( bool ) – Object Data, Unshare geometry data across objects (optional)

- material ( bool ) – Materials, Unshare material slots per data record (optional)

- animation ( bool ) – Object Animation, Unshare animation tracks per object (optional)

- obdata_animation ( bool ) – Object Data Animation, Unshare animation tracks for geometry (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
