# Weight paint and sculpt brush settings

Direction Ctrl Sculpt Mode
Brush direction toggle, Add raises geometry towards the brush, Subtract lowers geometry away from the brush. This setting can be toggled with Ctrl while sculpting.

Normal Radius Sculpt Mode
Determines the ratio of how much the brush radius is used to sample the normal direction of the sculpt plane of the brush. For example, a smaller Normal Radius will lead to drastic changes in the brush orientation, like for following the contours of hard surface meshes more closely. A large Normal Radius will lead to smoother changes in orientation, like for building overall forms on organic sculptures.

Area Radius
The ratio between the brush radius and the radius that is going to be used to sample the area plane depth.

Tilt Strength Sculpt Mode
Determines how much the tilt of the user's tablet pen affects the brush normal. Negative values correspond to inverting the direction of the tilt.

Hardness Sculpt Mode
How close the brush falloff starts from the edge of the brush.

Tip Roundness
The factor to control how round the brush is. A value of zero will make the brush square. Note, the Brush Falloff is only applied to the rounded portions of the brush.

Auto-smooth Sculpt Mode
Sets the amount of smoothing to be applied to each stroke.

Topology Rake Sculpt Mode
The higher this setting is set, the more Dyntopo aligns mesh edges to the brush direction while tessellating the surface. This generates cleaner edge flow to help define sharp features. Topology Rake can have a severe performance impact so it works best on low-poly meshes.

Normal Weight Ctrl Sculpt Mode
Constrains brush movement along the surface normal. Especially useful with the Grab brush, can be temporarily enabled by holding Ctrl . E.g. Grab brush can be used to push a depression (hole) into the mesh when Normal Weight is set.

Applies to Grab and Snake Hook brushes.

Plane Offset Sculpt Mode
Offset for planar brushes (Clay, Fill, Flatten, Scrape), shifts the plane that is found by averaging the faces above or below.

Plane Trim Sculpt Mode
Ability to limit the distance that planar brushes act. If trim is enabled vertices that are further away from the offset plane than the trim distance are ignored during sculpting.

Pinch/Magnify Sculpt Mode
Pushes the mesh towards/away from the brush center during the stroke.

Deformation Target
How the deformation of the brush will affect the object.

Geometry :

Deform the geometry directly.

Cloth Simulation :

Deform the mesh while a cloth simulation is applied to it at the same time.

[Related references](INDEX.md).
