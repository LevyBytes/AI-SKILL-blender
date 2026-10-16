# bpy.types.ToolSettings: gpencil_interpolate, gpencil_paint, gpencil_sculpt, gpencil_sculpt_paint, gpencil_selectmode_edit, gpencil_stroke_placement_view3d, gpencil_stroke_snap_mode, gpencil_surface_offset, gpencil_vertex_paint, gpencil_weight_paint

gpencil_interpolate 

Configuration for the Grease Pencil interpolation tools (readonly)

Type :

GPencilInterpolateSettings
gpencil_paint 

(readonly)

Type :

GpPaint
gpencil_sculpt 

Configuration for the stroke sculpting tools and brushes (readonly)

Type :

GPencilSculptSettings
gpencil_sculpt_paint 

(readonly)

Type :

GpSculptPaint
gpencil_selectmode_edit 

(default 'POINT' )

Type :

Literal[Grease Pencil Selectmode Items]
gpencil_stroke_placement_view3d 

(default 'ORIGIN' )

- ORIGIN
Origin – Draw stroke at Object origin.

- CURSOR
3D Cursor – Draw stroke at 3D cursor location.

- SURFACE
Surface – Stick stroke to surfaces.

- STROKE
Stroke – Stick stroke to other strokes.

Type :

Literal[‘ORIGIN’, ‘CURSOR’, ‘SURFACE’, ‘STROKE’]
gpencil_stroke_snap_mode 

(default 'NONE' )

- NONE
All Points – Snap to all points.

- ENDS
End Points – Snap to first and last points and interpolate.

- FIRST
First Point – Snap to first point.

Type :

Literal[‘NONE’, ‘ENDS’, ‘FIRST’]
gpencil_surface_offset 

How far along the normal strokes sit when drawn on surfaces (in [-inf, inf], default 0.15)

Type :

float
gpencil_vertex_paint 

(readonly)

Type :

GpVertexPaint
gpencil_weight_paint 

(readonly)

Type :

GpWeightPaint

[Related references](INDEX.md).
