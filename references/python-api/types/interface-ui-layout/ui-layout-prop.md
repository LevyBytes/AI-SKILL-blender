# bpy.types.UILayout: prop ( data , property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , placeholder = '' , expand = False , slider = False , toggle = -1 , icon_only = False , event = False , full_event = False , emboss = True , index = -1 , icon_value = 0 , invert_checkbox = False )

prop ( data , property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , placeholder = '' , expand = False , slider = False , toggle = -1 , icon_only = False , event = False , full_event = False , emboss = True , index = -1 , icon_value = 0 , invert_checkbox = False )

Item. Surfaces a single RNA item as a control in the layout.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

- placeholder ( str ) – Hint describing the expected value when empty (optional)

- expand ( bool ) – Expand button to show more detail (optional)

- slider ( bool ) – Use slider widget for numeric values (optional)

- toggle ( int ) – Use toggle widget for boolean values, or a checkbox when disabled (the default is -1 which uses toggle only when an icon is displayed) (in [-1, 1], optional)

- icon_only ( bool ) – Draw only icons in buttons, no text (optional)

- event ( bool ) – Use button to input key events (optional)

- full_event ( bool ) – Use button to input full events including modifiers (optional)

- emboss ( bool ) – Draw the button itself, not just the icon/text. When false, corresponds to the ‘`NONE_OR_STATUS`’ layout emboss type. (optional)

- index ( int ) – The index of this button, when set a single member of an array can be accessed, when set to -1 all array members are used (in [-2, inf], optional)

- icon_value ( int ) – Icon Value, Override automatic icon of the item (in [0, inf], optional)

- invert_checkbox ( bool ) – Draw checkbox value inverted (optional)

[Related references](INDEX.md).
