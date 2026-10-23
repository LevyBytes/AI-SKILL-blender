# Object Properties

## Object Properties

Object Properties: Display Control

### Shading

Reference
Panel: Properties ‣ Object Properties ‣ Shading

### Light Linking

Govern which objects receive light from a given source using Light Linking.

Receiver Collection
Objects in this collection will receive light emitted from the current object.

### Shadow Linking

Control shadow interaction via Light Linking.

Shadow Blocker Collection
Objects in this collection act as shadow blockers for the light emitted from the current object.

### Shadow Terminator

Shadow Terminator mitigates edge artifacts on low-poly or smooth-shaded geometry, especially with bump maps. Artifacts arise when shading normals diverge from geometry, creating visible shadow discontinuities.

Normal Offset
Shift shadow position along the shading normal to suppress artifacts. Offset is in object space and peaks at glancing light angles. Zero disables the bias. Increase if shadow breaks appear, but excessive values risk light leaks. The Geometry Offset controls how many faces the bias touches:

Geometry Offset
Adjust how many faces receive normal offset. Zero affects only grazing faces; 1.0 affects all faces. Higher values help if artifacts persist, though excessive offset distorts shadows, especially with bump mapping.

### Visibility

Reference
Panel: Object Properties ‣ Visibility

### Ray Visibility

Set objects invisible to particular ray types. Example: make emissive mesh invisible to camera rays. For instanced objects, visibility inherits from parents; hidden parent types hide children.

Using these options outperforms shader setups achieving the same result.

Camera
Object appears to the Camera, including viewport perspective in viewport rendering.

Shadow
Object casts shadows; it does not appear inside shadow maps.

### Light Probes

Control whether objects appear in light probe captures. Example: exclude animated objects from static probes. Instanced objects inherit parent visibility.

Volume
Object is visible during light probe volume baking.

Sphere
Object is visible during light probe sphere capture.

Plane
Object is visible during light probe plane capture.

[Related references](INDEX.md).
