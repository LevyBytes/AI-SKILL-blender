# bpy.ops.clip.detect_features

bpy.ops.clip. detect_features ( * , placement = 'FRAME' , margin = 16 , threshold = 0.5 , min_distance = 120 )

Locate salient points and insert markers for tracking purposes

Parameters :

- placement ( Literal [ 'FRAME' , '`INSIDE_GPENCIL`' , '`OUTSIDE_GPENCIL`' ] ) – Placement, Placement for detected features (optional)

- FRAME
Whole Frame – Place markers across the whole frame.

- `INSIDE_GPENCIL`
Inside Annotated Area – Place markers only inside areas outlined with the Annotation tool.

- `OUTSIDE_GPENCIL`
Outside Annotated Area – Place markers only outside areas outlined with the Annotation tool.

- margin ( int ) – Margin, Only features further than margin pixels from the image edges are considered (in [0, inf], optional)

- threshold ( float ) – Threshold, Threshold level to consider feature good enough for tracking (in [0.0001, inf], optional)

- min_distance ( int ) – Distance, Minimal distance accepted between two features (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
