# Mesh Plane: Texture, Transform

### Texture

Note

Each option is covered in depth under Image Texture Node.

Interpolation
How the picture is scaled as it's shown on the plane.

Extension
How the picture extends past its own edges.

Alpha
Turns on transparency from the image's alpha channel.

Auto Refresh
Refreshes viewport images as the frame advances.

### Transform

New planes appear at the 3D Cursor. When you bring in several, the Offset Planes option keeps them apart.

Size Mode
Determines how the plane's size is set:

Absolute :

You give the height in Height , and the width follows to keep the aspect ratio. Example: An image of 800 × 600 pixels with a height of 1 m results in a width of 1.33 m.

Height
Sets the plane's height.

Scale to Camera Frame :

The plane's size follows the active camera.

Scale
How the plane scales against the camera frame.

Fit :

Sizes the plane to sit inside the camera frame with its aspect ratio intact.

Fill :

Sizes the plane to cover the whole camera frame, which may crop parts of it.

Pixels per Inch :

Derives the plane's size from the Definition value, expressed in pixels per inch. Example: With a 600 DPI setting, an 800 × 600 px image results in a plane size of ~0.0339 × 0.0254 m.

Definition
The pixels-per-inch count.

Pixels per Blender Unit :

Takes Definition as pixels per Blender Unit. Example: With a setting of 600, an 800 × 600 px image results in a plane size of 1.33 × 1 BU.

Definition
The pixels-per-Blender-Unit count.

Align
How the plane is rotated as it comes in.

Z- (Down), Y-, X-, Z+ (Up), Y+, X+ :

Turns the plane to line up with the chosen axis.

Face Camera :

Points straight at the camera.

Camera's Main Axis :

Snaps the plane to a major axis pointed along the camera's view.

Track Camera Face Camera Camera's Main Axis
Adds a Locked Track constraint, so the plane stays turned toward the camera.

Offset Planes
Spreads multiple planes out rather than stacking them.

Offset Direction
The axis the planes are spaced along.

Distance
The gap between planes.

[Related references](INDEX.md).
