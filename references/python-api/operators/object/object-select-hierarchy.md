# bpy.ops.object.select_hierarchy

bpy.ops.object. select_hierarchy ( * , direction = 'PARENT' , extend = False ) 

Highlight object family members relative to the active object

Parameters :

- direction ( Literal [ 'PARENT' , 'CHILD' ] ) – Direction, Family line direction to highlight (optional)

- extend ( bool ) – Extend, Add to the existing selection instead of replacing it (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object.py:174

[Related references](INDEX.md).
