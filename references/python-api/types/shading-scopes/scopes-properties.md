# bpy.types.Scopes: properties

## Scopes(bpy_struct)

### Scopes(bpy_struct)

base class — bpy_struct
class bpy.types. Scopes ( bpy_struct )

Scopes giving a statistical view of an image
accuracy

Share of the source image's original pixel lines that get sampled (in [0, 100], default 0.0)

Type :

float
histogram

Histogram for viewing image statistics (readonly)

Type :

Histogram
use_full_resolution

Sample every single pixel of the image (default False)

Type :

bool
vectorscope_alpha

Opacity of the points (in [0, 1], default 0.0)

Type :

float
vectorscope_mode

(default 'RGB' )

Type :

Literal[‘LUMA’, ‘RGB’]
waveform_alpha

Opacity of the points (in [0, 1], default 0.0)

Type :

float
waveform_mode

(default 'LUMA' )

Type :

Literal[‘LUMA’, ‘PARADE’, ‘YCBCR601’, ‘YCBCR709’, ‘YCBCRJPG’, ‘RGB’]

[Related references](INDEX.md).
