# Light Probe Plane

## Light Probe Plane

### Light Probe Plane

A planar light probe captures incoming light from a single direction across all positions on a flat surface. Only the specular reflection pathway currently provides data.

Planar probes fit smooth flat surfaces well.

Each visible planar probe costs render duration—each requires scene recomputation.

Planar probes operate when ray tracing uses Screen-Trace . They quicken tracing and furnish screen-space ray tracing gaps.

Note

Volumetrics and reflections remain unhandled within Light probe planes.

### Placement

Without Backface Culling, positioning the light probe plane on the planar surface captures its underside.

Elevate the light probe plane above the surface to avoid self-inclusion. Or deactivate light probe visibility in object visibility panel.

### Properties

Reference

Panel :

Object Data ‣ Probe

Distance
A probe only alters lighting inside its influence area. Distance parameter and object scale define this zone.

For planar probes, influence distance measures from the plane. Surfaces aligned with the Reflection Plane get captured reflection contributions.

### Capture

Clipping Offset
Distance below the plane for near clip during capture. Increase to address reflection contact artifacts.

### Viewport Display

Reference

Panel :

Object Data ‣ Viewport Display

Arrow Size
Normal direction arrow scale.

Capture
Show captured reflection on a maximally reflective plane in the viewport.

Influence
Display influence area bounds in viewport.

[Related references](INDEX.md).
