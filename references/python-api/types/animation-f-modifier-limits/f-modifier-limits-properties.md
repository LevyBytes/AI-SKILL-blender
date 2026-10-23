# bpy.types.FModifierLimits: properties

## FModifierLimits(FModifier)

### FModifierLimits(FModifier)

base classes: bpy_struct, FModifier
class bpy.types. FModifierLimits ( FModifier )

Clamps the time and value range of the F-Curve it modifies.
max_x

Upper cap permitted on X (in [-inf, inf], default 0.0)

Type :

float
max_y

Upper cap permitted on Y (in [-inf, inf], default 0.0)

Type :

float
min_x

Lower cap permitted on X (in [-inf, inf], default 0.0)

Type :

float
min_y

Lower cap permitted on Y (in [-inf, inf], default 0.0)

Type :

float
use_max_x

Apply the upper X cap (default False)

Type :

bool
use_max_y

Apply the upper Y cap (default False)

Type :

bool
use_min_x

Apply the lower X cap (default False)

Type :

bool
use_min_y

Apply the lower Y cap (default False)

Type :

bool

[Related references](INDEX.md).
