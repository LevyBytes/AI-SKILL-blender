# Cameras: Depth of Field, Aperture, Camera

### Depth of Field 

A real lens bends incoming light and brings it to a focus on the sensor.
The upshot: only subjects at one set distance read sharp, while everything closer or farther blurs.

Example of DOF bokeh effect. 

That sharp band is the focal point. Set it with a plain figure, or by the gap between the camera and an object you name:

Focus Object
Name the object that fixes the focal point. Linking one switches the distance parameter off.

Focal Distance
The focal-point distance used while no Focus Object is named.
Enable Limits in the camera's Viewport Display panel to picture this distance inside the 3D Viewport.

Hint

Either click the eyedropper or hover the Focal Distance field and press E to arm the Depth Picker .
Then LMB any point in the 3D Viewport to read its distance back to the camera.

#### Aperture 

F-Stop
This ratio governs the strength of the blur.
The lower you go, the heavier the depth of field.

Blades
How many polygonal blades reshape the blurred objects across the render and its preview. As in the viewport, the bokeh effect needs 3 blades at minimum, which gives a triangular blur.

Rotation
Turn the polygonal blades around the facing axis, either clockwise or the other way.

Ratio
Skew the distortion to mimic anamorphic bokeh.
1.0 leaves it undistorted; under 1.0 stretches the blur sideways, over 1.0 stretches it up and down.

### Camera 

The settings in this group echo what a physical camera body offers.
Reach for a Preset to line Blender up with a real-world camera.

Sensor Fit
Governs the way the sensor sits inside the output dimensions, and through that the angular field of view.

Auto :

Works out a square sensor from whichever of the Resolution dimensions is larger.

Horizontal :

Set the sensor Width yourself; the Height follows from the output Resolution aspect ratio.

Vertical :

Set the sensor Height yourself; the Width follows from the output Resolution aspect ratio.

Size / Width, Height
A second path to the field of view that leaves focal length alone.
Handy when pairing a Blender camera to a real lens-and-body combo, motion tracking being one case.

[Related references](INDEX.md).
