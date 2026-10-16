# bpy.types.KeyMaps: find, find_match, find_modal

find ( name , * , space_type = 'EMPTY' , region_type = 'WINDOW' ) 

find

Parameters :

- name ( str ) – Name, (never None)

- space_type (Literal[Space Type Items]) – Space Type, (optional)

- region_type (Literal[Region Type Items]) – Region Type, (optional)

Returns :

Key Map, Corresponding key map

Return type :

KeyMap
find_match ( keymap ) 

find_match

Parameters :

keymap (KeyMap) – Key Map, The key map for comparison

Returns :

Key Map, Corresponding key map

Return type :

KeyMap
find_modal ( name ) 

find_modal

Parameters :

name ( str ) – Operator Name, (never None)

Returns :

Key Map, Corresponding key map

Return type :

KeyMap

[Related references](INDEX.md).
