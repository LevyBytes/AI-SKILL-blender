# bpy.utils: bpy.utils. user_resource ( resource_type , * , path = '' , create = False )

bpy.utils. user_resource ( resource_type , * , path = '' , create = False ) 

Give back a user resource path (usually under the user's home directory).

Parameters :

- resource_type ( Literal [ 'DATAFILES' , 'CONFIG' , 'SCRIPTS' , 'EXTENSIONS' ] ) – The resource type.

- path ( str ) – Optional subdirectory.

- create ( bool ) – Treat the path as a directory and create it if its not existing.

Returns :

a path.

Return type :

str

[Related references](INDEX.md).
