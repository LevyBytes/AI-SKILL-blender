# bpy.types.Collection: children, children_recursive

children

The collections nested one level directly beneath this one (default None, readonly)

Type :

CollectionChildren[Collection]
children_recursive

Every descendant collection beneath this one, returned as a list.

Type :

list[Collection]

Note

Runs in O(n), with n counting every descendant collection beneath this one.

(readonly)

[Related references](INDEX.md).
