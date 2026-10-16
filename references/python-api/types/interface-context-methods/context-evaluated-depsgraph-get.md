# bpy.types.Context: Methods: Methods, evaluated_depsgraph_get

Methods
evaluated_depsgraph_get ( )

Retrieve the dependency graph tied to the current scene and view layer; through it you reach data-blocks that already have their animation and modifiers resolved. Pending edits to any data-block trigger a rebuild of the graph, and doing so makes every existing reference to its evaluated data-blocks stale.

Returns :

Evaluated dependency graph

Return type :

Depsgraph

[Related references](INDEX.md).
