# bpy.types.CurveProfile: properties

## CurveProfile(bpy_struct)

### CurveProfile(bpy_struct)

base class: bpy_struct
class bpy.types. CurveProfile ( bpy_struct )

The editor used to construct a profile path.
points

Profile control points (default None, readonly)

Type :

CurveProfilePoints[CurveProfilePoint]
preset

(default 'LINE' )

- LINE
Line – The default.

- SUPPORTS
Support Loops – A loop sitting on either side of the profile.

- CORNICE
Cornice Molding.

- CROWN
Crown Molding.

- STEPS
Steps – A run of steps, however many the segments call for.

Type :

Literal['LINE', 'SUPPORTS', 'CORNICE', 'CROWN', 'STEPS']
segments

Segments sampled from control points (default None, readonly)

Type :

bpy_prop_collection[CurveProfilePoint]
use_clip

Constrain the path view so it stays inside a set boundary (default False)

Type :

bool
use_sample_even_lengths

Sample edges with even lengths (default False)

Type :

bool
use_sample_straight_edges

Sample edges with vector handles (default False)

Type :

bool

[Related references](INDEX.md).
