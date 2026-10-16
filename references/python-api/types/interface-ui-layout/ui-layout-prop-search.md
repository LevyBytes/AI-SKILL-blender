# bpy.types.UILayout: prop_search ( data , property , search_data , search_property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , results_are_suggestions = False , item_search_property = '' )

prop_search ( data , property , search_data , search_property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , results_are_suggestions = False , item_search_property = '' )

prop_search

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- search_data (AnyType) – Data from which to take collection to search in (never None)

- search_property ( str ) – Identifier of search collection property (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

- results_are_suggestions ( bool ) – Accept inputs that do not match any item (optional)

- item_search_property ( str ) – Identifier of the string property in each collection’s items to use for searching (defaults to the items’ type ‘name property’) (optional, never None)

[Related references](INDEX.md).
