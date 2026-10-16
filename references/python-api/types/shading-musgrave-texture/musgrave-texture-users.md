# bpy.types.MusgraveTexture: users_material, users_object_modifier

users_material

The materials referencing this texture

Type :

tuple[Material, …]

Note

Takes O(len(bpy.data.materials) * len(material.texture_slots)) time.

(readonly)
users_object_modifier

The object modifiers referencing this texture

Type :

tuple[Object, …]

Note

Takes O(len(bpy.data.objects) * len(obj.modifiers)) time.

(readonly)

[Related references](INDEX.md).
