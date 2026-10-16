# Ambient Occlusion Node

## Ambient Occlusion Node

### Ambient Occlusion Node 

The Ambient Occlusion node measures hemisphere occlusion above the shading point. Applies include procedural texturing and effects like corner weathering.

In Cycles, this is a costly computation and can extend render duration substantially. For performance-critical projects, Pointiness from the Geometry node or pre-baked AO yield faster results.

Note

Cycles Only

The Ambient Occlusion node fails to give correct output when:

- The object functions as either Caustic caster or Caustic receiver while the scene contains an active Caustic caster, Caustic receiver, and Shadow Caustic Light.

- Open Shading Language is active under the OptiX backend.

See also

The Ambient Occlusion pass provides occlusion data across the full render for compositing work.

### Inputs 

Color
Tint applied to AO output.

Distance
The range for considering objects occluding the shading point.

Normal
The normal used for ambient occlusion computation; geometric normal is used if unconnected.

### Properties 

Samples
Ray-trace sample count for AO. Keep minimal for speed.

Inside
Detect bulges rather than hollows by computing occlusion within mesh.

Only Local Cycles Only
Restrict occlusion to the object itself, excluding other geometry.

### Outputs 

Color
Ambient occlusion with color tint.

AO
Occlusion factor without tint.

### Example 

White AO shader.

[Related references](INDEX.md).
