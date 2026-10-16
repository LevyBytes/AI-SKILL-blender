# bpy.types.PreferencesInput: view_rotate_method, view_rotate_sensitivity_trackball, view_rotate_sensitivity_turntable, view_zoom_axis, view_zoom_method

view_rotate_method

The orbit technique used in the viewport (default 'TURNTABLE' )

- TURNTABLE
Turntable – Holds the Z-axis upright as you orbit.

- TRACKBALL
Trackball – Lets you tumble the view to any angle.

Type :

Literal[‘TURNTABLE’, ‘TRACKBALL’]
view_rotate_sensitivity_trackball

Scale the sensitivity of trackball orbiting (in [0.1, 10], default 1.0)

Type :

float
view_rotate_sensitivity_turntable

Rotation per pixel that sets how quickly the viewport orbits (in [1.74533e-05, 0.261799], default 0.00698132)

Type :

float
view_zoom_axis

Which axis of mouse motion zooms the view (default 'VERTICAL' )

- VERTICAL
Vertical – Drive zoom from vertical mouse motion.

- HORIZONTAL
Horizontal – Drive zoom from horizontal mouse motion.

Type :

Literal[‘VERTICAL’, ‘HORIZONTAL’]
view_zoom_method

The style used for viewport scaling (default 'DOLLY' )

- CONTINUE
Continue – Zoom continuously, with direction and speed set by how far the mouse has traveled along the chosen Zoom Axis..

- DOLLY
Dolly – Zoom by moving the mouse along the chosen Zoom Axis.

- SCALE
Scale – Zoom as though scaling the view, with mouse motion measured from center.

Type :

Literal[‘CONTINUE’, ‘DOLLY’, ‘SCALE’]

[Related references](INDEX.md).
