# bpy.types.CompositorNodeImage: properties

## CompositorNodeImage(CompositorNode)

### CompositorNodeImage(CompositorNode)

base classes: bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeImage ( CompositorNode )

Feeds in a still image or a movie file.
frame_duration

How many frames of a movie to draw from (in [0, 1048574], default 0)

Type :

int
frame_offset

Shifts which frame of the animation is read (in [-1048574, 1048574], default 0)

Type :

int
frame_start

Frame at which the movie/sequence begins globally, treating the first picture as #1 (in [-1048574, 1048574], default 0)

Type :

int
has_layers

True if this image has any named layer (default False, readonly)

Type :

bool
has_views

True if this image has multiple views (default False, readonly)

Type :

bool
image

Type :

Image
layer

(default 'PLACEHOLDER' )

Type :

Literal[‘PLACEHOLDER’]
use_auto_refresh

Reload the image whenever the frame changes (default False)

Type :

bool
use_cyclic

Loop the movie's images repeatedly (default False)

Type :

bool
view

(default 'ALL' )

Type :

Literal[‘ALL’]

[Related references](INDEX.md).
