# bpy.types.Gizmo: draw, draw_select, draw_preset_box, draw_preset_arrow, draw_preset_circle, draw_custom_shape

draw ( context )

Parameters :

context (Context) – (never None)
draw_select ( context , * , select_id = 0 )

Parameters :

- context (Context) – (never None)

- select_id ( int ) – (in [0, inf], optional)
draw_preset_box ( matrix , * , select_id = -1 )

Draw a box

Parameters :

- matrix (mathutils.Matrix) – The transform matrix to apply (multi-dimensional array of 4 * 4 items, in [-inf, inf])

- select_id ( int ) – The id for a selectable gizmo; pass -1 if it is not being selected., (in [-1, inf], optional)
draw_preset_arrow ( matrix , * , axis = '`POS_Z`' , select_id = -1 )

Draw a box

Parameters :

- matrix (mathutils.Matrix) – The transform matrix to apply (multi-dimensional array of 4 * 4 items, in [-inf, inf])

- axis (Literal[Object Axis Items]) – Arrow Orientation (optional)

- select_id ( int ) – The id for a selectable gizmo; pass -1 if it is not being selected., (in [-1, inf], optional)
draw_preset_circle ( matrix , * , axis = '`POS_Z`' , select_id = -1 )

Draw a box

Parameters :

- matrix (mathutils.Matrix) – The transform matrix to apply (multi-dimensional array of 4 * 4 items, in [-inf, inf])

- axis (Literal[Object Axis Items]) – Arrow Orientation (optional)

- select_id ( int ) – The id for a selectable gizmo; pass -1 if it is not being selected., (in [-1, inf], optional)
draw_custom_shape ( shape , * , matrix = None , select_id = None )

Renders a shape that was built by Gizmo.draw_custom_shape.

Parameters :

- shape ( Any ) – The previously cached shape that gets drawn.

- matrix (mathutils.Matrix | None) – A 4x4 matrix; if omitted, Gizmo.matrix_world stands in.

- select_id ( int | None ) – The selection id.
Only use when drawing within Gizmo.draw_select.

static new_custom_shape ( type , verts )

Builds a fresh shape suitable for handing to Gizmo.draw_custom_shape.

Parameters :

- type ( Literal [ 'POINTS' , 'LINES' , 'TRIS' , '`LINE_STRIP`' ] ) – The type of shape to create.

- verts ( Sequence [ Sequence [ float ] ] ) – Sequence of 2D or 3D coordinates.

Returns :

The freshly built shape (its return type may change later).

Return type :

Any

[Related references](INDEX.md).
