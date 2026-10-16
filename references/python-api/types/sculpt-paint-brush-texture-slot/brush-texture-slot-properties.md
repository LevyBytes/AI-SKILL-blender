# bpy.types.BrushTextureSlot: properties

## BrushTextureSlot(TextureSlot)

### BrushTextureSlot(TextureSlot)

base classes — bpy_struct, TextureSlot
class bpy.types. BrushTextureSlot ( TextureSlot )

Texture slot configuration for textures in a Brush data-block
angle

Brush texture orientation (in [0, 6.28319], default 0.0)

Type :

float
has_random_texture_angle

(default False, readonly)

Type :

bool
has_texture_angle

(default False, readonly)

Type :

bool
has_texture_angle_source

(default False, readonly)

Type :

bool
map_mode

(default '`VIEW_PLANE`' )

Type :

Literal['`VIEW_PLANE`', '`AREA_PLANE`', 'TILED', '3D', 'RANDOM', 'STENCIL']
mask_map_mode

(default '`VIEW_PLANE`' )

Type :

Literal['`VIEW_PLANE`', 'TILED', 'RANDOM', 'STENCIL']
random_angle

Brush texture random angle (in [0, 6.28319], default 6.28319)

Type :

float
use_rake

(default False)

Type :

bool
use_random

(default False)

Type :

bool

[Related references](INDEX.md).
