# Tips

## Tips

### Tips 

Monitor the Animated checkbox in Rigid Body properties closely.
A frequent mistake: applying keyframe animation to a Passive object without checking Animated. The object moves, but the physics engine treats the Passive as static, causing unexpected results.

### Animation 

A common technique animates location or rotation of an Active body together with toggling the Animated checkbox.
When Animated disables, the physics engine assumes control using the last known position, rotation, and velocities.

Animating other property strengths—Motor Target Velocity, Hinge limits, etc.—enables varied effects.

Enabling constraints mid-simulation often produces dramatic results as the physics engine reconciles misaligned objects, frequently building sufficient kinetic energy to propel them offscreen.

Bake rigid body dynamics to keyframes via Bake To Keyframes in Object ‣ Rigid Body.

### Simulation Stability 

Increasing steps per second offers the simplest stability improvement.
Excessive steps create problems and reduce stability (over 1000 steps suggests reconsidering the approach).

Higher solver iterations strengthen constraints and improve stacking stability.

Small objects remain unstable; objects should ideally exceed 20 cm diameter.
For smaller objects, setting collision margin to 0 can help (though generally inadvisable).

Fast-moving small objects may interpenetrate. Beyond steps-per-second adjustments, avoid mesh shapes here.
Mesh shapes consist of individual triangles lacking thickness, encouraging interpenetration.
Increase collision margins to add effective thickness.

### Combining Rigid Bodies with Other Simulations 

Since rigid body simulation integrates with the animation system, it influences other simulations just as animation does.

For this to work, the rigid body object requires a Collision Modifier—add it via Physics properties.

### Scaling Rigid Bodies 

Rigid bodies scale during or outside simulation.
Generally this works well, occasionally causing issues.

For non-dynamic scaling, apply the scale first using Apply Scale (Ctrl - A); avoid scaling during simulation if possible.

[Related references](INDEX.md).
