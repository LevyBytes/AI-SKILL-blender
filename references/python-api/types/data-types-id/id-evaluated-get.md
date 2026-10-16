# bpy.types.ID: evaluated_get

evaluated_get ( depsgraph )

Fetch the matching evaluated ID out of the supplied dependency graph. This does not force the graph to be fully evaluated; you simply get back whatever the previous evaluation produced.

Parameters :

depsgraph (Depsgraph) – Dependency graph to perform lookup in (never None)

Returns :

New copy of the ID

Return type :

ID

[Related references](INDEX.md).
