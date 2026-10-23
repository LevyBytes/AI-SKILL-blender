# bpy.types.ParticleBrush: properties

## ParticleBrush(bpy_struct)

### ParticleBrush(bpy_struct)

base class: bpy_struct
class bpy.types. ParticleBrush ( bpy_struct )

Brush used when editing particles
count

Particle count (in [1, 1000], default 10)

Type :

int
curve

(readonly)

Type :

CurveMapping
length_mode

(default 'GROW' )

- GROW
Grow – Lengthen the hairs.

- SHRINK
Shrink – Shorten the hairs.

Type :

Literal[‘GROW’, ‘SHRINK’]
puff_mode

(default 'ADD' )

- ADD
Add – Increase how puffy the hairs are.

- SUB
Sub – Decrease how puffy the hairs are.

Type :

Literal[‘ADD’, ‘SUB’]
size

Radius of the brush in pixels (in [1, 32767], default 50)

Type :

int
steps

Brush steps (in [1, 32767], default 10)

Type :

int
strength

Brush strength (in [0.001, 1], default 0.5)

Type :

float
use_puff_volume

Extend puffing to the unselected endpoints as well, which helps keep hair volume when the root is puffed (default False)

Type :

bool

[Related references](INDEX.md).
