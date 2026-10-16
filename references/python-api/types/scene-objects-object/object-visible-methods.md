# bpy.types.Object: visible_get, visible_in_viewport_get

visible_get ( * , view_layer = None , viewport = None ) 

Report whether the object shows in the 3D viewport once every visibility setting is accounted for

Parameters :

- view_layer (ViewLayer) – Use this instead of the active view layer (optional)

- viewport (SpaceView3D) – Use this instead of the active 3D viewport (optional)

Returns :

Object visible

Return type :

bool
visible_in_viewport_get ( viewport ) 

Evaluate local view and local collections for this viewport/object pair

Parameters :

viewport (SpaceView3D) – Viewport in local collections (never None)

Returns :

Object viewport visibility

Return type :

bool

[Related references](INDEX.md).
