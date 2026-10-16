# bpy.types.Object: users_collection, users_scene

users_collection 

Which collections include this object.

Type :

tuple[Collection, …]

Note

Takes O(len(bpy.data.collections) + len(bpy.data.scenes)) time.

(readonly)
users_scene 

Which scenes include this object.

Type :

tuple[Scene, …]

Note

Takes O(len(bpy.data.scenes) * len(bpy.data.objects)) time.

(readonly)

[Related references](INDEX.md).
