# bpy.types.VolumeDisplay: properties

density

How thick the volume looks when drawn in the viewport (in [1e-05, inf], default 1.0)

Type :

float
interpolation_method

Which interpolation is applied to volumes in solid mode (default 'LINEAR' )

- LINEAR
Linear – A solid balance of smoothness and speed.

- CUBIC
Cubic – Higher-quality smoothed result, at a slower pace.

- CLOSEST
Closest – Skip interpolation entirely.

Type :

Literal['LINEAR', 'CUBIC', 'CLOSEST']
slice_axis

(default 'AUTO' )

- AUTO
Auto – Pick the slice direction from the current view angle.

- X
X – Cut along the X axis.

- Y
Y – Cut along the Y axis.

- Z
Z – Cut along the Z axis.

Type :

Literal['AUTO', 'X', 'Y', 'Z']
slice_depth

Where along the axis the slice sits (in [0, 1], default 0.5)

Type :

float
use_slice

Take a single slice through the domain object (default False)

Type :

bool
wireframe_detail

How much detail the wireframe display shows (default 'COARSE' )

- COARSE
Coarse – Draw one box or point per intermediate tree node.

- FINE
Fine – Draw a box for every leaf node holding 8×8 voxels.

Type :

Literal['COARSE', 'FINE']
wireframe_type

Which wireframe style is drawn (default 'BOXES' )

- NONE
None – Skip drawing the volume in wireframe mode.

- BOUNDS
Bounds – Draw a single bounding box around the whole grid.

- BOXES
Boxes – Draw bounding boxes for the nodes in the volume tree.

- POINTS
Points – Draw points for the nodes in the volume tree.

Type :

Literal['NONE', 'BOUNDS', 'BOXES', 'POINTS']

[Related references](INDEX.md).
