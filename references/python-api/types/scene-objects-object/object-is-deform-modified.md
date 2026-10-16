# bpy.types.Object: is_deform_modified

is_deform_modified ( scene , settings ) 

Report whether a deformation moves this object away from its base mesh data

Parameters :

- scene (Scene) – Scene in which to check the object (never None)

- settings ( Literal [ 'PREVIEW' , 'RENDER' ] ) – Modifier settings to apply

- PREVIEW
Preview – Apply modifier preview settings.

- RENDER
Render – Apply modifier render settings.

Returns :

Whether the object is deform-modified

Return type :

bool

[Related references](INDEX.md).
