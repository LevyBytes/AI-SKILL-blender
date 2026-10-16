# bpy.types.IntProperty: properties

## IntProperty(Property)

### IntProperty(Property)

base classes — bpy_struct, Property
class bpy.types. IntProperty ( Property )

The RNA definition of an integer-number property.
array_dimensions

The size of every dimension of the array (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
array_length

The array's maximum length, where 0 means no limit (in [0, inf], default 0, readonly)

Type :

int
default

This number's default value (in [-inf, inf], default 0, readonly)

Type :

int
default_array

This array's default value (array of 3 items, in [-inf, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
hard_max

The buttons' upper limit (in [-inf, inf], default 0, readonly)

Type :

int
hard_min

The buttons' lower limit (in [-inf, inf], default 0, readonly)

Type :

int
is_array

(default False, readonly)

Type :

bool
soft_max

The buttons' upper limit (in [-inf, inf], default 0, readonly)

Type :

int
soft_min

The buttons' lower limit (in [-inf, inf], default 0, readonly)

Type :

int
step

The increment used by number buttons; for floats this is 1/100th of it (in [0, inf], default 0, readonly)

Type :

int

[Related references](INDEX.md).
