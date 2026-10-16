# bpy.ops.object.select_grouped

bpy.ops.object. select_grouped ( * , extend = False , type = '`CHILDREN_RECURSIVE`' ) 

Highlight all objects associated via many criteria

Parameters :

- extend ( bool ) – Extend, Add to the existing selection instead of replacing it (optional)

- type ( Literal [ '`CHILDREN_RECURSIVE`' , 'CHILDREN' , 'PARENT' , 'SIBLINGS' , 'TYPE' , 'COLLECTION' , 'HOOK' , 'PASS' , 'COLOR' , 'KEYINGSET' , '`LIGHT_TYPE`' ] ) – Type, (optional)

- `CHILDREN_RECURSIVE`
Children.

- CHILDREN
Immediate Children.

- PARENT
Parent.

- SIBLINGS
Siblings – Shared parent.

- TYPE
Type – Shared object type.

- COLLECTION
Collection – Shared collection.

- HOOK
Hook.

- PASS
Pass – Render pass index.

- COLOR
Color – Object color.

- KEYINGSET
Keying Set – Objects included in active Keying Set.

- `LIGHT_TYPE`
Light Type – Matching light types.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
