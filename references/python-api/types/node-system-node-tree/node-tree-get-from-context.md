# bpy.types.NodeTree: get_from_context

classmethod get_from_context ( context ) 

Retrieve a node tree from the current context.

Parameters :

context (Context) – (never None)

Returns :

result_1 , Active node tree from context, NodeTree

result_2 , ID data-block that owns the node tree, ID

result_3 , Original ID data-block selected from the context, ID

Return type :

tuple[NodeTree, ID, ID]

[Related references](INDEX.md).
