# bpy.types.GizmoGroup: methods

classmethod poll ( context )

Checks whether this gizmo group is allowed to run.

Parameters :

context (Context) – (never None)

Return type :

bool
classmethod setup_keymap ( keyconfig )

Sets up the keymaps for this gizmo group, falling back to the default keymap when none is supplied.

Parameters :

keyconfig (KeyConfig) – (never None)

Returns :

(never None)

Return type :

KeyMap
setup ( context )

The function that creates the group’s gizmos.

Parameters :

context (Context) – (never None)
refresh ( context )

Rebuilds the data; invoked when shared state such as the selection changes.

Parameters :

context (Context) – (never None)
draw_prepare ( context )

Runs ahead of every redraw.

Parameters :

context (Context) – (never None)
invoke_prepare ( context , gizmo )

Runs just before invoke.

Parameters :

- context (Context) – (never None)

- gizmo (Gizmo) – (never None)
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
