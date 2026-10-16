# bpy.types.GPencilSculptGuide: properties

angle

The heading the guide lines follow (in [-6.28319, 6.28319], default 0.0)

Type :

float
angle_snap

Snapping applied to the angle (in [-6.28319, 6.28319], default 0.0)

Type :

float
location

A user-set reference point the guides use (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
reference_object

The object that supplies the reference point

Type :

Object
reference_point

Which speed-guide reference is in use (default 'CURSOR' )

- CURSOR
Cursor – Take the cursor as the reference point.

- CUSTOM
Custom – Take a custom reference point.

- OBJECT
Object – Take an object as the reference point.

Type :

Literal[‘CURSOR’, ‘CUSTOM’, ‘OBJECT’]
spacing

Gap left between guides (in [0, inf], default 20.0)

Type :

float
type

Which kind of speed guide to use (default 'CIRCULAR' )

- CIRCULAR
Circular – Build rings from one point.

- RADIAL
Radial – Use one point to set the direction.

- PARALLEL
Parallel – Parallel lines.

- GRID
Grid – Lay out horizontal and vertical lines.

- ISO
Isometric – Lay out isometric and vertical lines.

Type :

Literal[‘CIRCULAR’, ‘RADIAL’, ‘PARALLEL’, ‘GRID’, ‘ISO’]
use_guide

Enable speed guides (default False)

Type :

bool
use_snapping

Snap to the guide’s angle or spacing settings (default False)

Type :

bool

[Related references](INDEX.md).
