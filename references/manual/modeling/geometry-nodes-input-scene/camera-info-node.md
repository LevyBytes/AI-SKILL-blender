# Camera Info Node

## Camera Info Node

### Camera Info Node

The Camera Info node outputs camera object parameters.

Useful for customizing geometry based on camera settings—building camera-dependent visual effects, aligning geometry to camera view, or similar tasks.

### Inputs

Camera
The camera to query.

To retrieve the active camera, use Active Camera Node.

### Outputs

Projection Matrix
A 4×4 matrix combining focal length, sensor size, shift, and clipping range. Projects 3D coordinates to screen space.

Focal Length
Camera focal length in millimeters. Affects perspective field-of-view.

Sensor
Physical sensor dimensions in millimeters as a 2D vector (X, Y), influenced by sensor-fit settings.

Shift
Horizontal and vertical view shift as a 2D vector.

Clip Start
Near clipping distance.

Clip End
Far clipping distance.

Focus Distance
Distance from camera to focus plane, in Blender units. Typically for depth-of-field.

Is Orthographic
Boolean: true for orthographic, false for perspective.

Orthographic Scale
Orthographic-mode zoom factor. Controls view size instead of focal length.

[Related references](INDEX.md).
