# bpy.types.Modifier: properties

execution_time

How many seconds the modifier needed to evaluate. Populated only on evaluated objects, and unreliable when several modifiers evaluate concurrently. (in [-inf, inf], default 0.0, readonly)

Type :

float
is_active

Whether this is the currently active entry in the modifier list (default False)

Type :

bool
is_override_data

On a local override object, indicates whether the modifier originates from the linked reference or was added locally to the override (default True, readonly)

Type :

bool
name

Name given to the modifier (default “”, never None)

Type :

str
persistent_uid

Identifier that stays unique for the modifier inside its containing stack (in [-inf, inf], default 0, readonly)

Type :

int
show_expanded

Whether the modifier panel is unfolded in the interface (default False)

Type :

bool
show_in_editmode

Keep the modifier visible while in Edit mode (default False)

Type :

bool
show_on_cage

Make the edit cage follow the modifier output (default False)

Type :

bool
show_render

Apply the modifier when rendering (default False)

Type :

bool
show_viewport

Show the modifier result in the viewport (default False)

Type :

bool
type

(default '`GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY`' , readonly)

Type :

Literal[Object Modifier Type Items]
use_apply_on_spline

Run this modifier and every deform modifier before it on the control points of splines rather than on the tessellated curve/surface (default False)

Type :

bool
use_pin_to_last

Force the modifier to stay pinned to the bottom of the stack (default False)

Type :

bool

[Related references](INDEX.md).
