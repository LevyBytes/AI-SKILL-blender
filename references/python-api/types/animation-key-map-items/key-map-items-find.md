# bpy.types.KeyMapItems: find_from_operator, find_match

find_from_operator ( idname , * , properties = None , include = {'ACTIONZONE', 'KEYBOARD', 'MOUSE', 'NDOF'} , exclude = set() ) 

find_from_operator

Parameters :

- idname ( str ) – Operator Identifier, (never None)

- properties (OperatorProperties) – (optional)

- include (set[Literal[Event Type Mask Items]]) – Include, (optional)

- exclude (set[Literal[Event Type Mask Items]]) – Exclude, (optional)

Return type :

KeyMapItem
find_match ( keymap , item ) 

find_match

Parameters :

- keymap (KeyMap) – The matching keymap

- item (KeyMapItem) – The matching keymap item

Returns :

The keymap item from this keymap which matches the keymap item from the arguments passed in

Return type :

KeyMapItem

[Related references](INDEX.md).
