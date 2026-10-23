# bpy.types.ThemeDopeSheet: properties

## ThemeDopeSheet(bpy_struct)

### ThemeDopeSheet(bpy_struct)

base class: bpy_struct
class bpy.types. ThemeDopeSheet ( bpy_struct )

Styling for the Dope Sheet
anim_interpolation_constant

Line color shown for constant-interpolation segments (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
anim_interpolation_linear

Line color shown for linear-interpolation segments (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
anim_interpolation_other

Line color shown for easing and dynamic interpolation segments (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
grid

(array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
keyframe_border

Color of keyframe border (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
keyframe_border_selected

Color of selected keyframe border (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
keyframe_scale_factor

Multiplier that controls how tall keyframes are drawn (in [0.8, 5], default 1.0)

Type :

float
simulated_frames

(array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
space

Styling for the space (readonly, never None)

Type :

ThemeSpaceGeneric
summary

Color of summary channel (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]

[Related references](INDEX.md).
