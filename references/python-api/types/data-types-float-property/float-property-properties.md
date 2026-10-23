# bpy.types.FloatProperty: properties

## FloatProperty(Property)

### FloatProperty(Property)

base classes: bpy_struct, Property
class bpy.types. FloatProperty ( Property )

Definition of an RNA property holding a single-precision floating-point number.
array_dimensions

Length of each dimension of the array (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
array_length

Maximum length of the array, 0 means unlimited (in [0, inf], default 0, readonly)

Type :

int
default

Default value for this number (in [-inf, inf], default 0.0, readonly)

Type :

float
default_array

Default value for this array (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

bpy_prop_array[float]
hard_max

Maximum value used by buttons (in [-inf, inf], default 0.0, readonly)

Type :

float
hard_min

Minimum value used by buttons (in [-inf, inf], default 0.0, readonly)

Type :

float
is_array

(default False, readonly)

Type :

bool
precision

How many decimal places buttons display. For fields whose unit is 'NONE' or 'TIME' (frame count) and whose step divides evenly by 100, the fraction is dropped automatically once the value is a whole number. (in [0, inf], default 0, readonly)

Type :

int
soft_max

Maximum value used by buttons (in [-inf, inf], default 0.0, readonly)

Type :

float
soft_min

Minimum value used by buttons (in [-inf, inf], default 0.0, readonly)

Type :

float
step

Increment applied by the number buttons; for float fields this is one hundredth of the stated step size (in [0, inf], default 0.0, readonly)

Type :

float

[Related references](INDEX.md).
