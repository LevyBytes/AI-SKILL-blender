# bpy.types.GreasePencilLineartModifier: shadow_camera_far, shadow_camera_near, shadow_camera_size, shadow_region_filtering

shadow_camera_far

Far clipping distance of shadow camera (in [0, 10000], default 200.0)

Type :

float
shadow_camera_near

Near clipping distance of shadow camera (in [0, 10000], default 0.1)

Type :

float
shadow_camera_size

Acts as the “Orthographic Scale” of an orthographic camera. Placing that camera at the light’s position with this scale defines how far the shadow “camera” reaches. (in [0, 10000], default 200.0)

Type :

float
shadow_region_filtering

Pick feature lines coming from lit or shaded areas. Cast shadow and light contour stay unaffected because they lie on the border. (default 'NONE' )

- NONE
None – Not filtering any lines based on illumination region.

- ILLUMINATED
Illuminated – Only selecting lines from illuminated regions.

- SHADED
Shaded – Only selecting lines from shaded regions.

- `ILLUMINATED_ENCLOSED`
Illuminated (Enclosed Shapes) – Selecting lines from lit regions, and make the combination of contour, light contour and shadow lines into enclosed shapes.

Type :

Literal[‘NONE’, ‘ILLUMINATED’, ‘SHADED’, ‘`ILLUMINATED_ENCLOSED`’]

[Related references](INDEX.md).
