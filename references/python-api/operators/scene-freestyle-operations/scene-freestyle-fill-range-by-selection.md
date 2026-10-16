# bpy.ops.scene.freestyle_fill_range_by_selection

bpy.ops.scene. freestyle_fill_range_by_selection ( * , type = 'COLOR' , name = '' )

Set Range Min/Max by computing the distance span between chosen mesh objects and the source (either user-specified or the active camera)

Parameters :

- type ( Literal [ 'COLOR' , 'ALPHA' , 'THICKNESS' ] ) – Type, Specifies which modifier category to affect (optional)

- COLOR
Color – Color modifier type.

- ALPHA
Alpha – Alpha modifier type.

- THICKNESS
Thickness – Thickness modifier type.

- name ( str ) – Name, ID of the modifier to work on (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/freestyle.py:45

[Related references](INDEX.md).
