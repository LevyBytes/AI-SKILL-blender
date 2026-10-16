# bpy.utils: bpy.utils. resource_path ( type , * , major = bpy.app.version0 , minor = bpy.app.version1 )

bpy.utils. resource_path ( type , * , major = bpy.app.version[0] , minor = bpy.app.version[1] ) 

Give back the root path where system files are kept.

Parameters :

- type ( Literal [ 'USER' , 'LOCAL' , 'SYSTEM' ] ) – The resource type.

- major ( int ) – major version, defaults to current.

- minor ( int ) – minor version, defaults to current.

Returns :

the resource path (not necessarily existing).

Return type :

str

[Related references](INDEX.md).
