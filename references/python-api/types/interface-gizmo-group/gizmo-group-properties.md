# bpy.types.GizmoGroup: properties

## GizmoGroup(bpy_struct)

### GizmoGroup(bpy_struct)

base class: bpy_struct
class bpy.types. GizmoGroup ( bpy_struct )

Holds an operator that is mid-execution, or one registered once it has finished running.
bl_idname

(default “”, never None)

Type :

str
bl_label

(default “”, never None)

Type :

str
bl_options

Options for this operator type (default set())

- 3D
3D – Use in 3D viewport.

- SCALE
Scale – Scale to respect zoom (otherwise zoom independent display size).

- `DEPTH_3D`
Depth 3D – Supports culled depth by other objects in the view.

- SELECT
Select – Supports selection.

- PERSISTENT
Persistent.

- `SHOW_MODAL_ALL`
Show Modal All – Keep everything visible during interaction, including this group when a different one is being interacted with.

- `EXCLUDE_MODAL`
Exclude Modal – Keep everything except this group visible during interaction.

- `TOOL_INIT`
Tool Init – Hold off running until the tool operator runs (when paired with a tool).

- `TOOL_FALLBACK_KEYMAP`
Use fallback tools keymap – Attach the fallback tools keymap to this gizmo type.

- `VR_REDRAWS`
VR Redraws – These gizmos target virtual-reality sessions and need their redraws handled specially.

Type :

set[Literal[‘3D’, ‘SCALE’, ‘`DEPTH_3D`’, ‘SELECT’, ‘PERSISTENT’, ‘`SHOW_MODAL_ALL`’, ‘`EXCLUDE_MODAL`’, ‘`TOOL_INIT`’, ‘`TOOL_FALLBACK_KEYMAP`’, ‘`VR_REDRAWS`’]]
bl_owner_id

(default “”, never None)

Type :

str
bl_region_type

The region where the panel is going to be used in (default 'WINDOW' )

Type :

Literal[Region Type Items]
bl_space_type

The space where the panel is going to be used in (default 'EMPTY' )

Type :

Literal[Space Type Items]
gizmos

List of gizmos in the Gizmo Map (default None, readonly)

Type :

Gizmos[Gizmo]
name

(default “”, readonly, never None)

Type :

str

[Related references](INDEX.md).
