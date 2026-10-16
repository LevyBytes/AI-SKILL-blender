# bpy.types.ImagePreview: properties

## ImagePreview(bpy_struct)

### ImagePreview(bpy_struct)

base class — bpy_struct
class bpy.types. ImagePreview ( bpy_struct )

A preview image alongside its icon.
icon_id

A unique integer that identifies this preview as an icon (zero meaning invalid) (in [-inf, inf], default 0, readonly)

Type :

int
icon_pixels

The icon's pixels, given as bytes (always 32-bit RGBA) (in [-inf, inf], default 0)

Type :

int
icon_pixels_float

The icon's pixel components, given as floats (RGBA concatenated values) (in [-inf, inf], default 0.0)

Type :

float
icon_size

Pixel width and height (array of 2 items, in [-inf, inf], default (0, 0))

Type :

bpy_prop_array[int]
image_pixels

The image's pixels, given as bytes (always 32-bit RGBA) (in [-inf, inf], default 0)

Type :

int
image_pixels_float

The image's pixel components, given as floats (RGBA concatenated values) (in [-inf, inf], default 0.0)

Type :

float
image_size

Pixel width and height (array of 2 items, in [-inf, inf], default (0, 0))

Type :

bpy_prop_array[int]
is_icon_custom

True when a py script has altered this preview icon, so Blender no longer auto-generates it (default False)

Type :

bool
is_image_custom

True when a py script has altered this preview image, so Blender no longer auto-generates it (default False)

Type :

bool

[Related references](INDEX.md).
