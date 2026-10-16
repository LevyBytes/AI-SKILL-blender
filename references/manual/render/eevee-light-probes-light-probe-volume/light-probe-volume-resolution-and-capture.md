# Light Probe Volume: Resolution, Capture, Clamping, Offset, Viewport Display

### Resolution

Resolution X, Y, Z
Volumetric probe spatial resolution. The local volume subdivides into a grid of specified dimensions. Each grid cell captures lighting.

Bake Samples
Light direction count during baking. Proportionally extends baking duration to scene size.

Surfel Resolution
Surfel spawning per local unit. Higher yields better quality but severe memory increases.

Tip

Optimal: double the maximum Resolution .

### Capture

Capture Distance
Bake distance around the light probe volume. Zero captures only interior.

Contributions – World
Bake world light for precision versus correct multi-volume blending.

Contributions – Indirect Light
Capture post-source light bounces.

Contributions – Emission
Capture emissive surfaces during baking.

#### Clamping

Direct Light
Clamp direct light entry. 0.0 deactivates. Direct light: single-bounce light or emissive first-bounce light.

Indirect Light
Clamp indirect light entry. 0.0 deactivates. Indirect light: post-first-bounce light from sources or emissive surfaces.

Tip

Tiny non-zero Clamp Indirect captures first-bounce light only.

#### Offset

Baking adjusts capture point placement to lower artifacts. Points shift away from surfaces and relocate from interiors when not too deep.

Surface Offset
Surface distance for point displacement.

Search Distance
Search span for positions near single-sided object back-faces.

Note

Lone materials with Single Sided for Light Probe Volumes move capture point position.

### Viewport Display

Data
Show captured light as diffuse spheres at given size.

Clipping
Show capture clip extent.

Influence
Show influence area. Inner sphere marks falloff start.

[Related references](INDEX.md).
