# bpy.types.UIList: draw_item, draw_filter

draw_item ( context , layout , data , item , icon , active_data , active_property , index , flt_flag )

Draw an item in the list (NOTE: when you define your own draw_item function, you may want to check given ‘item’ is of the right type…)

Parameters :

- layout (UILayout) – Layout to draw the item (never None)

- data (AnyType) – Data from which to take Collection property

- item (AnyType) – Item of the collection property

- icon ( int ) – Icon of the item in the collection (in [0, inf])

- active_data (AnyType) – Data from which to take property for the active element (never None)

- active_property ( str ) – Identifier of property in active_data, for the active element (optional for registration, never None)

- index ( int ) – Index of the item in the collection (in [0, inf])

- flt_flag ( int ) – The filter-flag result for this item (in [0, inf])
draw_filter ( context , layout )

Draw filtering options

Parameters :

layout (UILayout) – Layout to draw the item (never None)

[Related references](INDEX.md).
