# bpy.types.Object: select_get, select_set

select_get ( * , view_layer = None ) 

Report whether the object is selected; selection is tracked per view layer.

Parameters :

view_layer (ViewLayer) – Use this instead of the active view layer (optional)

Returns :

Object selected

Return type :

bool
select_set ( state , * , view_layer = None ) 

Mark the object as selected or deselected; selection is tracked per view layer.

Parameters :

- state ( bool ) – Selection state to define

- view_layer (ViewLayer) – Use this instead of the active view layer (optional)

[Related references](INDEX.md).
