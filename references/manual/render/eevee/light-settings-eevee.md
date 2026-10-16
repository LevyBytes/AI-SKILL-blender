# Light Settings (EEVEE)

## Light Settings (EEVEE)

Light Settings (EEVEE) — Overview

Reference
Panel: Properties ‣ Object Data and Shader Editor ‣ Sidebar ‣ Options

In EEVEE, illumination originates from three sources: the world environment, materials that emit light, and light objects. Light objects provide targeted illumination control and appear as scene elements rather than contributing directly to the rendered output.

For settings shared across rendering engines, see Light settings.

### Shadow

EEVEE employs Virtual Shadow Mapping combined with Shadow Map Raytracing to produce shadow effects. This approach concentrates shadow detail where needed, achieving better accuracy than traditional shadow mapping and includes efficient caching.

Tip
- The error "Shadow buffer full" occurs when shadow memory allocation exceeds system capacity. Remedy: enlarge Shadow Pool Size or reduce Resolution Limit on individual lights. Alternatively, disable shadow casting on less critical light sources.
- Adjust Shadow Map Raytracing behavior through Render Settings.
- Enable Jitter to diminish light leaking artifacts caused by large light sources and Shadow Map Raytracing.

See also
Limitations.

Jitter
Enable jittered soft shadows to enhance shadow precision. Incurs significant performance overhead since the shadow map cannot be cached and recomputes for each render sample.

Note
Viewport display is off by default; check render settings to enable visibility.

Overblur
Apply shadow tracing to individual jittered samples to attenuate under-sampling noise.

Note
Values above zero produce softer shadows but sacrifice physical accuracy.

Filter
Reduce shadow aliasing via PCF with circular kernels. The filter's world-space scale depends on the shadowed pixel's shadow map resolution.

Note
Values larger than 1px raise light leaking risk.

Resolution Limit
Sets the minimum shadow map pixel size. Larger values conserve memory at the expense of shadow quality and also accelerate rendering of complex scenes. Shadows scale to match screen pixel position, enabling sharp precision but requiring substantial memory. This setting caps the detail level captured.

Note
Increasing shadow map coarseness elevates light leaking probability.

Absolute Resolution Limit
Fix resolution at 1 unit from the light source rather than relative to screen pixels. Transforms Resolution Limit to behave as a standard shadow map pixel size.

Hint
This formula calculates Resolution Limit for a target resolution:

[resolution_limit = 2 * sqrt(2) / resolution]

Here (2 * sqrt(2)) denotes the unit cube diagonal and (resolution) denotes target resolution (e.g., 1024px).

Note
This feature is unavailable for Sun Light.

### Influence

These multipliers control light contribution per shader type, intended for creative adjustment. Values differing from 1.0 deviate from physical accuracy.

Diffuse
Multiplier for diffuse reflection intensity.

Glossy
Multiplier for glossy reflection intensity.

Transmission
Multiplier for transmission intensity.

Volume Scatter
Multiplier for volume scattering intensity.

### Custom Distance

When enabled, uses Distance for custom attenuation instead of the global Light Threshold. The distance initializes automatically based on threshold, computed at the light origin using inverse-square falloff.

Distance
Specifies where light contribution decays to zero.

Note
Sun Light does not support this feature.

See also
Global Light Threshold.

[Related references](INDEX.md).
