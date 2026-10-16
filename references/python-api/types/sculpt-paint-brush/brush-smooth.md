# bpy.types.Brush: smooth_deform_type, smooth_stroke_factor, smooth_stroke_radius

smooth_deform_type

The kind of deformation the brush applies (default 'LAPLACIAN' )

- LAPLACIAN
Laplacian – Smooths both the surface and the volume.

- SURFACE
Surface – Smooths only the mesh surface, holding the volume in place.

Type :

Literal['LAPLACIAN', 'SURFACE']
smooth_stroke_factor

Larger values produce a smoother stroke (in [0.5, 0.99], default 0.9)

Type :

float
smooth_stroke_radius

How far the cursor must travel from the previous point before the stroke resumes (in [10, 200], default 75)

Type :

int

[Related references](INDEX.md).
