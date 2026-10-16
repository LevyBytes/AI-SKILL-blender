# bpy.types.UILayout: menu_pie, menu, menu_contents

menu_pie ( )

A nested layout in which child items are arranged radially around the center of the menu.

Returns :

Sub-layout to put items in

Return type :

UILayout
menu ( menu , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , icon_value = 0 )

menu

Parameters :

- menu ( str ) – Identifier of the menu (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

- icon_value ( int ) – Icon Value, Override automatic icon of the item (in [0, inf], optional)
menu_contents ( menu )

menu_contents

Parameters :

menu ( str ) – Identifier of the menu (never None)

[Related references](INDEX.md).
