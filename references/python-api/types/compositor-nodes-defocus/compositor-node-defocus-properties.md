# bpy.types.CompositorNodeDefocus: properties

## CompositorNodeDefocus(CompositorNode)

### CompositorNodeDefocus(CompositorNode)

base classes: bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeDefocus ( CompositorNode )

Adds 2D depth-of-field blur, driven by a Z depth map or a mask.
angle

Rotation offset applied to the bokeh shape (in [0, 1.5708], default 0.0)

Type :

float
blur_max

Cap on the blur, the largest allowed CoC radius (in [0, 10000], default 0.0)

Type :

float
bokeh

(default 'CIRCLE' )

- OCTAGON
Octagonal – 8 sides.

- HEPTAGON
Heptagonal – 7 sides.

- HEXAGON
Hexagonal – 6 sides.

- PENTAGON
Pentagonal – 5 sides.

- SQUARE
Square – 4 sides.

- TRIANGLE
Triangular – 3 sides.

- CIRCLE
Circular.

Type :

Literal[‘OCTAGON’, ‘HEPTAGON’, ‘HEXAGON’, ‘PENTAGON’, ‘SQUARE’, ‘TRIANGLE’, ‘CIRCLE’]
f_stop

Strength of the focal blur; 128 (infinity) gives sharp focus, and halving it doubles the blur radius (in [0, 128], default 0.0)

Type :

float
scene

Scene whose active camera is used (falls back to the render scene when left unset)

Type :

Scene
use_zbuffer

Turn off when feeding an image in place of a real z-buffer (switched on automatically for non-image-based nodes such as a time node) (default True)

Type :

bool
z_scale

Scales the Z input when no z-buffer is used, setting the cap on blur marked by white or an input value of 1 (in [0, 1000], default 0.0)

Type :

float

[Related references](INDEX.md).
