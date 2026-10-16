# bpy.types.UILayout: template_search ( data , property , search_data , search_property , * , new = '' , unlink = '' , text = '' , text_ctxt = '' , translate = True )

template_search ( data , property , search_data , search_property , * , new = '' , unlink = '' , text = '' , text_ctxt = '' , translate = True )

template_search

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- search_data (AnyType) – Data from which to take collection to search in (never None)

- search_property ( str ) – Identifier of search collection property (never None)

- new ( str ) – Operator identifier to create a new item for the collection (optional, never None)

- unlink ( str ) – Operator identifier to unlink or delete the active item from the collection (optional, never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

[Related references](INDEX.md).
