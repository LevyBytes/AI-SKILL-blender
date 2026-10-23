# bpy.types.Stereo3dFormat: properties

## Stereo3dFormat(bpy_struct)

### Stereo3dFormat(bpy_struct)

base class: bpy_struct
class bpy.types. Stereo3dFormat ( bpy_struct )

Configuration for stereo output
anaglyph_type

(default '`RED_CYAN`' )

Type :

Literal[Stereo3D Anaglyph Type Items]
display_mode

(default 'ANAGLYPH' )

- ANAGLYPH
Anaglyph – Output the left and right eye views as two color-filtered layers within one image (you need anaglyph glasses).

- INTERLACE
Interlace – Output the left and right eye views interlaced inside one image (you need a 3D-ready monitor).

- SIDEBYSIDE
Side-by-Side – Place the left and right eye views next to each other.

- TOPBOTTOM
Top-Bottom – Stack the left and right eye views, one above the other.

Type :

Literal[‘ANAGLYPH’, ‘INTERLACE’, ‘SIDEBYSIDE’, ‘TOPBOTTOM’]
interlace_type

(default '`ROW_INTERLEAVED`' )

Type :

Literal[Stereo3D Interlace Type Items]
use_interlace_swap

Exchange the left and right stereo channels (default False)

Type :

bool
use_sidebyside_crosseyed

Have the right eye view the left image and the other way around (default False)

Type :

bool
use_squeezed_frame

Merge the two views into one squeezed image (default False)

Type :

bool

[Related references](INDEX.md).
