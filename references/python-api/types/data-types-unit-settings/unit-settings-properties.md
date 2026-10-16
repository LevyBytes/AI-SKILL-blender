# bpy.types.UnitSettings: properties

## UnitSettings(bpy_struct)

### UnitSettings(bpy_struct)

base class — bpy_struct
class bpy.types. UnitSettings ( bpy_struct )
length_unit

Which unit length values are shown in (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]
mass_unit

Which unit mass values are shown in (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]
scale_length

Conversion factor between Blender units and real dimensions. Picking a tiny or huge unit scale helps keep numerical precision usable when modeling at microscopic or astronomical sizes (in [1e-09, inf], default 0.0)

Type :

float
system

Which measurement system the interface controls follow (default 'NONE' )

Type :

Literal[‘NONE’, ‘METRIC’, ‘IMPERIAL’]
system_rotation

Which unit is applied when showing and editing rotations (default 'DEGREES' )

- DEGREES
Degrees – Use degrees for measuring angles and rotations.

- RADIANS
Radians.

Type :

Literal[‘DEGREES’, ‘RADIANS’]
temperature_unit

Which unit temperature values are shown in (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]
time_unit

Which unit time values are shown in (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]
use_separate

Break units into paired components when shown (e.g. 1m 0cm) (default False)

Type :

bool

[Related references](INDEX.md).
