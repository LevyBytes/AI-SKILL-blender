# bpy.types.PreferencesEdit: grease_pencil_default_color, grease_pencil_eraser_radius, grease_pencil_euclidean_distance, grease_pencil_manhattan_distance

grease_pencil_default_color

The color given to newly created annotation layers (array of 4 items, in [0, inf], default (0.38, 0.61, 0.78, 0.9))

Type :

bpy_prop_array[float]
grease_pencil_eraser_radius

Size of the eraser ‘brush’ (in [1, 500], default 25)

Type :

int
grease_pencil_euclidean_distance

How far the mouse must travel while drawing for a stroke point to be kept (in [0, 100], default 2)

Type :

int
grease_pencil_manhattan_distance

Per-axis mouse travel needed before a stroke point is recorded (in [0, 100], default 1)

Type :

int

[Related references](INDEX.md).
