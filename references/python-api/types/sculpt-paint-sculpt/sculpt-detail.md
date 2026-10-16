# bpy.types.Sculpt: detail_percent, detail_refine_method, detail_size, detail_type_method

detail_percent

Longest edge allowed in dynamic-topology sculpting, given as a percentage of brush size (in [0.5, 100], default 25.0)

Type :

float
detail_refine_method

Within dynamic-topology mode, the way mesh detail gets added or stripped away (default '`SUBDIVIDE_COLLAPSE`' )

- SUBDIVIDE
Subdivide Edges – Split long edges so extra detail appears wherever it is required.

- COLLAPSE
Collapse Edges – Merge short edges to strip out detail wherever that is feasible.

- `SUBDIVIDE_COLLAPSE`
Subdivide Collapse – Combine both: split long edges and merge short ones to refine the detail.

Type :

Literal[‘SUBDIVIDE’, ‘COLLAPSE’, ‘`SUBDIVIDE_COLLAPSE`’]
detail_size

Longest edge allowed in dynamic-topology sculpting, measured in pixels (in [0.5, 40], default 12.0)

Type :

float
detail_type_method

Within dynamic-topology mode, the basis on which detail size is figured (default 'RELATIVE' )

- RELATIVE
Relative Detail – Detail is gauged against both brush size and the detail-size setting.

- CONSTANT
Constant Detail – Detail stays fixed in world space at the chosen detail size.

- BRUSH
Brush Detail – Detail scales with brush size alone.

- MANUAL
Manual Detail – Detail holds steady across strokes and only updates on a Flood Fill.

Type :

Literal[‘RELATIVE’, ‘CONSTANT’, ‘BRUSH’, ‘MANUAL’]

[Related references](INDEX.md).
