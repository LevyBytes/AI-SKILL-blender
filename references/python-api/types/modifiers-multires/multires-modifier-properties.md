# bpy.types.MultiresModifier: properties

boundary_smooth

Sets the way smoothing is handled along open boundaries (default 'ALL' )

Type :

Literal[Subdivision Boundary Smooth Items]
filepath

Location of the external file holding displacement data (default “”, never None, blend relative // prefix supported)

Type :

str
is_external

When set, the multires displacements live in a separate file rather than the .blend, which reduces memory use (default False, readonly)

Type :

bool
levels

How many subdivision steps are shown in the viewport (in [0, 255], default 0)

Type :

int
quality

How precisely vertex positions are computed; lower numbers run quicker at the cost of exactness (in [1, 10], default 4)

Type :

int
render_levels

Subdivision level applied when rendering (in [0, 255], default 0)

Type :

int
sculpt_levels

How many subdivision steps apply while in sculpt mode (in [0, 255], default 0)

Type :

int
show_only_control_edges

Avoid drawing or rendering the inner subdivided edges (default True)

Type :

bool
total_levels

How many subdivision steps have displacement data retained for them (in [0, 255], default 0, readonly)

Type :

int
use_creases

Take mesh crease data into account to harden edges and corners (default True)

Type :

bool
use_custom_normals

Carry over any existing custom normals onto the resulting mesh (default False)

Type :

bool
use_sculpt_base_mesh

Have Sculpt Mode tools act on the base mesh while still previewing higher-level displacement (default False)

Type :

bool
uv_smooth

Sets how UVs get smoothed (default '`PRESERVE_BOUNDARIES`' )

Type :

Literal[Subdivision Uv Smooth Items]

[Related references](INDEX.md).
