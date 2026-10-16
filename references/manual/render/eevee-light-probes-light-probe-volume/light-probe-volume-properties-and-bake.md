# Light Probe Volume: Properties, Bake

## Light Probe Volume

### Light Probe Volume

A volumetric probe captures light from all directions across numerous interior positions.

Captured light filters to diffuse only. Capture point positions appear as an overlay when Irradiance Volume selection is active.

Objects outside any Irradiance Volume, or where indirect light hasn't baked, receive world diffuse lighting.

Tip

- Indoor lighting: align grids with room geometry.

- Exclude empty regions and low-variation areas from high resolution allocation.

- Problem zones get fixed via smaller grids nearby.

- Large environments may require many volumes at varying detail levels.

### Properties

Reference

Panel :

Object Data ‣ Probe

Intensity
Recorded lighting intensity. Anything besides 1.0 lacks physical basis. Reserve for artistic tweaking, animation, or adjustment.

Sampling Bias

Normal Bias
Offset irradiance grid samples along surface normal to curtail light seepage. Excessive values impart specular appearance to diffuse surfaces.

View Bias
Offset irradiance grid samples toward the viewer, reducing seepage. Excessive values introduce viewing artifacts. Prefer when the camera is fixed.

Facing Bias
Zero prevents capturing points behind shaded surfaces, yielding non-smooth interpolation at high resolution. Higher bias smooths interpolation but permits some seepage.

Validity & Dilation

During baking, each capture point receives a validity score from back-face strikes during lighting capture. Lone materials with Single Sided for Light Probe Volumes lower the score.

Validity Threshold
Disregard capture points below this validity score during lighting calculation. Suppresses trapped geometry artifacts.

Dilation Threshold
Points below this threshold get data replaced from valid neighbors.

Radius
Neighbor search distance in capture points.

### Bake

Light probe volume data remains static, requiring manual baking. Once baked, data belongs to the object and can move, animate, and transfer between files.

Note

Rendering uses object visibility during baking.

Scene conversion into an accelerated format during baking consumes substantial GPU memory, potentially blocking baking. Approaches to remedy:

- Segment large scenes into smaller zones or variable detail.

- Reduce Surfel Resolution .

- Deactivate light probe visibility on minor-impact objects.

Tip

Debug Value 3, 4, 5 expose the internal representation.

[Related references](INDEX.md).
