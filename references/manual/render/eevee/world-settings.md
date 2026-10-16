# World Settings

## World Settings

World Settings — Environment and Global Light

The world environment can emit light, ranging from solid color to complex textures.

EEVEE stores world lighting in an internal Light Probe, making it less precise than Cycles.

EEVEE classifies world lighting as indirect lighting, whereas Cycles treats it as direct.

### Mist Pass

Reference
Panel: World ‣ Mist Pass

Note
The mist pass must be activated in the View Layer tab of the Properties Editor before these settings appear in the World tab.

Mist strengthens depth perception by generating a render layer with a 0.0 to 1.0 depth map usable in the Compositor for mist effects.

Start
Camera distance where mist begins fading.

Depth
Distance from Start over which mist fades. Objects beyond Start + Depth are completely obscured.

Falloff
Curve function governing mist strength progression with distance.

Quadratic:
Uses light falloff calculation (1/x²) for smooth 0.0 to 1.0 transition.

Linear:
Steeper start than quadratic (1/x).

Inverse Quadratic:
Steepest start (1/√x) and approaches 1.0 faster than others.

Tip
Activate visualization in the Camera ‣ Viewport Display panel.

Mist example
(blend-file).

### Settings

Reference
Panel: World ‣ Light Probe

### Light Probe

Resolution
Storage resolution for world light. Equivalent to light probe sphere resolution.

See also
Light Probe Sphere.

### Sun

EEVEE can isolate light from intense sources (e.g., sun from HDRI) and replace with a sun light. Increases illumination quality since light probes alone cannot match this precision.

Threshold
Maximum world contribution recorded in the light probe when nonzero. Excess becomes a sun light. Reduces light bleeding from very bright sources. Zero disables the feature; all lighting stores in light probes.

Angle
Angular diameter of the extracted sun light as viewed from Earth.

Use Shadow
Enable shadow casting on the extracted sun.

See also
Shadow properties match sun light settings exactly.
See Light Properties.

[Related references](INDEX.md).
