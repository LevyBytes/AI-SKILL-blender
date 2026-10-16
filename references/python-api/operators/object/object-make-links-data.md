# bpy.ops.object.make_links_data

bpy.ops.object. make_links_data ( * , type = 'OBDATA' ) 

Duplicate properties from the active object to selected targets

Parameters :

type ( Literal [ 'OBDATA' , 'MATERIAL' , 'ANIMATION' , 'GROUPS' , 'DUPLICOLLECTION' , 'FONTS' , 'MODIFIERS' , 'EFFECTS' ] ) – Type, (optional)

- OBDATA
Link Object Data – Swap the assigned data reference.

- MATERIAL
Link Materials – Swap the assigned materials.

- ANIMATION
Link Animation Data – Swap the assigned animation track.

- GROUPS
Link Collections – Swap the assigned groups.

- DUPLICOLLECTION
Link Instance Collection – Swap the assigned collection instance.

- FONTS
Link Fonts to Text – Swap typeface assignments.

- MODIFIERS
Copy Modifiers – Swap modifier stacks.

- EFFECTS
Copy Grease Pencil Effects – Swap Grease Pencil effect configurations.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
