# bpy.types.ToolSettings: annotation_stroke_placement_view2d, annotation_stroke_placement_view3d, annotation_thickness

annotation_stroke_placement_view2d 

(default 'IMAGE' )

- IMAGE
Image – Stick stroke to the image.

- VIEW
View – Stick stroke to the view.

Type :

Literal[‘IMAGE’, ‘VIEW’]
annotation_stroke_placement_view3d 

The way annotation strokes are oriented within 3D space (default 'CURSOR' )

- CURSOR
3D Cursor – Draw stroke at 3D cursor location.

- VIEW
View – Stick stroke to the view.

- SURFACE
Surface – Stick stroke to surfaces.

Type :

Literal[‘CURSOR’, ‘VIEW’, ‘SURFACE’]
annotation_thickness 

Line thickness of annotation strokes (in [1, 10], default 3)

Type :

int

[Related references](INDEX.md).
