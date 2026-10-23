# bpy.types.MaskLayer: properties

## MaskLayer(bpy_struct)

### MaskLayer(bpy_struct)

base class: bpy_struct
class bpy.types. MaskLayer ( bpy_struct )

One mask layer that controls which pixels are masked.
alpha

Render Opacity (in [-inf, inf], default 0.0)

Type :

float
blend

How this mask layer blends with the others (default 'ADD' )

Type :

Literal[‘`MERGE_ADD`’, ‘`MERGE_SUBTRACT`’, ‘ADD’, ‘SUBTRACT’, ‘LIGHTEN’, ‘DARKEN’, ‘MUL’, ‘REPLACE’, ‘DIFFERENCE’]
falloff

Falloff curve applied to the feather (default 'SMOOTH' )

Type :

Literal[Proportional Falloff Curve Only Items]
hide

Hide this layer from the viewport (default False)

Type :

bool
hide_render

Exclude this layer from rendering (default False)

Type :

bool
hide_select

Block this layer from being selected in the viewport (default False)

Type :

bool
invert

Swap the mask's black and white (default False)

Type :

bool
name

Unique name of layer (default “”, never None)

Type :

str
select

Whether the layer is picked for editing in the Dope Sheet (default False)

Type :

bool
splines

Set of splines that make up this layer (default None, readonly)

Type :

MaskSplines[MaskSpline]
use_fill_holes

Detect holes while filling overlapping curves (default True)

Type :

bool
use_fill_overlap

Resolve self-intersections and overlaps prior to filling (default False)

Type :

bool

[Related references](INDEX.md).
