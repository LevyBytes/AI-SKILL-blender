# bpy.types.ObjectLineArt: properties

## ObjectLineArt(bpy_struct)

### ObjectLineArt(bpy_struct) 

base class: bpy_struct
class bpy.types. ObjectLineArt ( bpy_struct ) 

Per-object Line Art settings
crease_threshold 

Any angle below this is handled as a crease (in [0, 3.14159], default 2.44346)

Type :

float
intersection_priority 

When lines cross, the intersection joins whichever object carries the larger intersection priority (in [0, 255], default 0)

Type :

int
usage 

Determines how Line Art treats this object during calculation (default 'INHERIT' )

- INHERIT
Inherit – Adopt the settings of the parent collection.

- INCLUDE
Include – Produce feature lines from this object's data.

- `OCCLUSION_ONLY`
Occlusion Only – Let the object data contribute occlusion alone.

- EXCLUDE
Exclude – Leave this object out of Line Art rendering.

- `INTERSECTION_ONLY`
Intersection Only – Emit intersection lines for this collection and nothing else.

- `NO_INTERSECTION`
No Intersection – Keep this object in but skip generating intersection lines.

- `FORCE_INTERSECTION`
Force Intersection – Produce intersection lines even against objects that have intersection turned off.

Type :

Literal[‘INHERIT’, ‘INCLUDE’, ‘`OCCLUSION_ONLY`’, ‘EXCLUDE’, ‘`INTERSECTION_ONLY`’, ‘`NO_INTERSECTION`’, ‘`FORCE_INTERSECTION`’]
use_crease_override 

Let this object's crease value take precedence over the scene-wide one (default False)

Type :

bool
use_intersection_priority_override 

Let this object's intersection priority take precedence over the collection's (default False)

Type :

bool

[Related references](INDEX.md).
