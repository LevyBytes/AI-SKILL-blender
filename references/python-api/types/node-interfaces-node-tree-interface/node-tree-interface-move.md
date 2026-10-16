# bpy.types.NodeTreeInterface: move, move_to_parent

move ( item , to_position ) 

Reposition an item.

Parameters :

- item (NodeTreeInterfaceItem) – Item, The item to move (never None)

- to_position ( int ) – To Position, Target position for the item in its current panel (in [0, inf])
move_to_parent ( item , parent , to_position ) 

Relocate an item to a different panel, a different position, or both.

Parameters :

- item (NodeTreeInterfaceItem) – Item, The item to move (never None)

- parent (NodeTreeInterfacePanel) – Parent, New parent of the item

- to_position ( int ) – To Position, Target position for the item in the new parent panel (in [0, inf])

[Related references](INDEX.md).
