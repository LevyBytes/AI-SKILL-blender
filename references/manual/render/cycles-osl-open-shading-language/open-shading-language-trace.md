# Open Shading Language: Trace

geom:is_curve
Curve object indicator.

geom:curve_intercept
0..1 coordinate along curve, root to tip.

geom:curve_thickness
Curve thickness in object space.

geom:curve_length
Curve span in object space.

geom:curve_tangent_normal
Tangent normal along the strand.

geom:is_point
Point cloud indicator.

geom:point_radius
Point cloud point radius.

geom:point_position
Point cloud point center.

geom:point_random
Unique random value per point cloud point.

path:ray_length
Distance traveled since the last intersection.

object:random
Unique random value per object instance.

object:index
Object instance index.

object:location
Object position.

material:index
Material unique index.

particle:index
Particle instance identifier.

particle:age
Particle age in frames.

particle:lifetime
Total particle lifespan in frames.

particle:location
Particle position.

particle:size
Particle size.

particle:velocity
Particle motion direction and speed.

particle:angular_velocity
Rotational velocity of the particle.

### Trace

CPU Only

The trace(point pos, vector dir, ...) function traces rays from OSL shaders. The "shade" parameter currently lacks support, though getmessage("trace", ..) retrieves attributes from struck geometry. Refer to OSL specification documentation for usage details.

This cannot substitute for traditional lighting; its main role is shader "probing" of nearby geometry—for example, applying textures blocked by surrounding objects, exaggerating wear on exposed areas, or creating ambient-occlusion-like effects.

[Related references](INDEX.md).
