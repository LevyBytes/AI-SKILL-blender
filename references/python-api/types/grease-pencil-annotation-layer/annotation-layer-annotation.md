# bpy.types.AnnotationLayer: annotation_hide, annotation_onion_after_color, annotation_onion_after_range, annotation_onion_before_color, annotation_onion_before_range, annotation_onion_use_custom_color, annotation_opacity

annotation_hide

Set annotation Visibility (default False)

Type :

bool
annotation_onion_after_color

Base color for ghosts after the active frame (array of 3 items, in [0, 1], default (0.25, 0.1, 1.0))

Type :

mathutils.Color
annotation_onion_after_range

Maximum number of frames to show after current frame (in [-1, 120], default 0)

Type :

int
annotation_onion_before_color

Base color for ghosts before the active frame (array of 3 items, in [0, 1], default (0.302, 0.851, 0.302))

Type :

mathutils.Color
annotation_onion_before_range

Maximum number of frames to show before current frame (in [-1, 120], default 0)

Type :

int
annotation_onion_use_custom_color

Use custom colors for onion skinning instead of the theme (default False)

Type :

bool
annotation_opacity

Annotation Layer Opacity (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).
