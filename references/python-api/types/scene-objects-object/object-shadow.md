# bpy.types.Object: shadow_terminator_geometry_offset, shadow_terminator_normal_offset, shadow_terminator_shading_offset

shadow_terminator_geometry_offset 

Nudge rays away from the surface to cut down the shadow terminator artifact on low-poly meshes. Only triangles sitting at grazing angles to the light are affected (in [0, inf], default 0.1)

Type :

float
shadow_terminator_normal_offset 

Nudge rays away from the surface to cut down the shadow terminator artifact on low-poly meshes. Affects only the triangles touched by the geometry offset (in [0, inf], default 0.0)

Type :

float
shadow_terminator_shading_offset 

Shift the shadow terminator toward the light so artifacts on low-poly meshes are concealed (in [0, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
