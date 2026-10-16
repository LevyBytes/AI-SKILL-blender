# bpy.ops.armature.collection_remove_unused

bpy.ops.armature. collection_remove_unused ( )

Discard all bone groups that lack both bones and offspring. Recursively applies, purging groups whose sole progeny are also unused.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/anim.py:619

[Related references](INDEX.md).
