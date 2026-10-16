# bpy.types.StripTransform: properties

## StripTransform(bpy_struct)

### StripTransform(bpy_struct)

base class — bpy_struct
class bpy.types. StripTransform ( bpy_struct )

The transform controls belonging to a sequence strip.
filter

Type of filter to use for image transformation (default 'AUTO' )

- AUTO
Auto – Automatically choose filter based on scaling factor.

- NEAREST
Nearest – Use nearest sample.

- BILINEAR
Bilinear – Interpolate between 2×2 samples.

- `CUBIC_MITCHELL`
Cubic Mitchell – Cubic Mitchell filter on 4×4 samples.

- `CUBIC_BSPLINE`
Cubic B-Spline – Cubic B-Spline filter (blurry but no ringing) on 4×4 samples.

- BOX
Box – Averages source image samples that fall under destination pixel.

Type :

Literal[‘AUTO’, ‘NEAREST’, ‘BILINEAR’, ‘`CUBIC_MITCHELL`’, ‘`CUBIC_BSPLINE`’, ‘BOX’]
offset_x

Move along X axis (in [-inf, inf], default 0.0)

Type :

float
offset_y

Move along Y axis (in [-inf, inf], default 0.0)

Type :

float
origin

Origin of image for transformation (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

bpy_prop_array[float]
rotation

Rotate around image center (in [-inf, inf], default 0.0)

Type :

float
scale_x

Scale along X axis (in [0, inf], default 1.0)

Type :

float
scale_y

Scale along Y axis (in [0, inf], default 1.0)

Type :

float

[Related references](INDEX.md).
