# bpy.types.UILayout: enum_item_name, enum_item_description, enum_item_icon

classmethod enum_item_name ( data , property , identifier )

Fetch the display name shown in the UI for the given enum item.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- identifier ( str ) – Identifier of the enum item (never None)

Returns :

UI name of the enum item (never None)

Return type :

str
classmethod enum_item_description ( data , property , identifier )

Fetch the tooltip-style description shown in the UI for the given enum item.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- identifier ( str ) – Identifier of the enum item (never None)

Returns :

UI description of the enum item (never None)

Return type :

str
classmethod enum_item_icon ( data , property , identifier )

Fetch the icon associated with the given enum item.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- identifier ( str ) – Identifier of the enum item (never None)

Returns :

Icon identifier (in [0, inf])

Return type :

int

[Related references](INDEX.md).
