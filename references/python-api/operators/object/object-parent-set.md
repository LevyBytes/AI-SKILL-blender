# bpy.ops.object.parent_set

bpy.ops.object. parent_set ( * , type = 'OBJECT' , xmirror = False , keep_transform = False ) 

Establish the object's parent connection

Parameters :

- type ( Literal [ 'OBJECT' , 'ARMATURE' , '`ARMATURE_NAME`' , '`ARMATURE_AUTO`' , '`ARMATURE_ENVELOPE`' , 'BONE' , '`BONE_RELATIVE`' , 'CURVE' , 'FOLLOW' , '`PATH_CONST`' , 'LATTICE' , 'VERTEX' , '`VERTEX_TRI`' ] ) – Type, (optional)

- xmirror ( bool ) – X Mirror, Duplicate weights symmetrically across the X axis, for Envelope/Automatic influence group assignment (optional)

- keep_transform ( bool ) – Keep Transform, Preserve the object's world position before establishing the link (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
