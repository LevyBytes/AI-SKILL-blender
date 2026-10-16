# bpy.types.ColorManagedViewSettings: properties

curve_mapping

Curve-based color mapping run before the display transform (readonly)

Type :

CurveMapping
exposure

Exposure in stops applied ahead of the display transform, scaling by 2^exposure (in [-32, 32], default 0.0)

Type :

float
gamma

Extra gamma encoding applied after the display transform, for output needing custom gamma (in [0, 5], default 1.0)

Type :

float
is_hdr

Whether the display and view transform handle high dynamic range colors (default False, readonly)

Type :

bool
look

An extra transform run before the view transform to suit artistic preferences (default 'NONE' )

- NONE
None – Leave the image unaltered artistically.

Type :

Literal[‘NONE’]
support_emulation

Whether the display and view transform can automatically emulate a different display device using the display color spaces feature of OpenColorIO v2 configurations (default False, readonly)

Type :

bool
use_curve_mapping

Apply an RGB curve before the display transform (default False)

Type :

bool
use_white_balance

Run chromatic adaptation starting from a different white point (default False)

Type :

bool
view_transform

The view used when mapping an image into a display space (default 'NONE' )

- NONE
None – Skip any color transform on the display and fall back to the old non-color-managed display method.

Type :

Literal[‘NONE’]
white_balance_temperature

Color temperature of the white point in the scene (in [1800, 100000], default 6500.0)

Type :

float
white_balance_tint

Tint of the white point used by the scene; its default of 10 lines up with daylight (in [-500, 500], default 10.0)

Type :

float
white_balance_whitepoint

The color taken as white; temperature and tint are derived back and forth from it without manual steps (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color

[Related references](INDEX.md).
