# bpy.types.SpaceOutliner: filter_id_type, filter_invert, filter_state, filter_text

filter_id_type

Which data-block type to show (default 'ACTION' )

Type :

Literal[Id Type Items]
filter_invert

Flip the object state filter (default False)

Type :

bool
filter_state

(default 'ALL' )

- ALL
All – Show all objects in the view layer.

- VISIBLE
Visible – Show visible objects.

- SELECTED
Selected – Show selected objects.

- ACTIVE
Active – Show only the active object.

- SELECTABLE
Selectable – Show only selectable objects.

Type :

Literal[‘ALL’, ‘VISIBLE’, ‘SELECTED’, ‘ACTIVE’, ‘SELECTABLE’]
filter_text

The string used for live search filtering (default “”, never None)

Type :

str

[Related references](INDEX.md).
