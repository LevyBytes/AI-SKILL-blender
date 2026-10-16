# bpy.types.Object: children, children_recursive

children 

Every object parented under this one.

Type :

tuple[Object, …]

Note

Takes O(len(bpy.data.objects)) time.

(readonly)
children_recursive 

The complete descendant list under this object.

Type :

list[Object]

Note

Takes O(len(bpy.data.objects)) time.

(readonly)

[Related references](INDEX.md).
