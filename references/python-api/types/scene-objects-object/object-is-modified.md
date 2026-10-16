# bpy.types.Object: is_modified

is_modified ( scene , settings ) 

Report whether this object differs from its base mesh data

Parameters :

- scene (Scene) – Scene in which to check the object (never None)

- settings ( Literal [ 'PREVIEW' , 'RENDER' ] ) – Modifier settings to apply

- PREVIEW
Preview – Apply modifier preview settings.

- RENDER
Render – Apply modifier render settings.

Returns :

Whether the object is modified

Return type :

bool

[Related references](INDEX.md).
