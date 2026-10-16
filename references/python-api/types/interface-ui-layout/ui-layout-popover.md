# bpy.types.UILayout: popover, popover_group

popover ( panel , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , icon_value = 0 , direction = 'VERTICAL' )

popover

Parameters :

- panel ( str ) – Identifier of the panel (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

- icon_value ( int ) – Icon Value, Override automatic icon of the item (in [0, inf], optional)

- direction ( Literal [ 'VERTICAL' , 'HORIZONTAL' ] ) – Popup Direction, Where the popup panel opens in relation to the button it springs from (optional)

- VERTICAL
Vertical – Draw popup panel above or below the button.

- HORIZONTAL
Horizontal – Draw popup panel to the side of the button.
popover_group ( space_type , region_type , context , category )

popover_group

Parameters :

- space_type (Literal[Space Type Items]) – Space Type

- region_type (Literal[Region Type Items]) – Region Type

- context ( str ) – panel type context (never None)

- category ( str ) – panel type category (never None)

[Related references](INDEX.md).
