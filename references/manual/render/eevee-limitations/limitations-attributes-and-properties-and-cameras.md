# Limitations: Attributes and Properties, Cameras, Lights, Light Probes, Indirect Lighting, Shadows, Volumetrics, Depth of Field, Screen Space Effects, Raytracing, Shader Nodes

## Limitations

Compositor limitations — Hardware limitations: the usual hardware limits apply to the GPU compositor (see Troubleshooting Graphics Hardware). Blender uses the same GPU resources for both the UI and the GPU compositor, with a few consequences. UI freezes: unlike Cycles rendering, the UI can become unresponsive with the GPU compositor on some slower GPUs. TDR on Windows: Timeout Detection Recovery (TDR) resets the GPU driver if a GPU compositing task exceeds the default 2-second limit — common on older GPUs with expensive nodes like the Bokeh Blur node — so to avoid unexpected resets, raise the TDR timeout.

Limitations — Known Constraints

EEVEE is designed as an interactive renderer. Some capabilities remain incomplete or fundamentally incompatible with its architecture without sacrificing speed.

This catalog covers the principal limitations encountered when working with EEVEE.

### Attributes and Properties

- Only 14 attributes from Geometry Nodes can be used in a single material.
- Up to 8 custom object attributes are accessible per material.

### Cameras

- Only perspective and orthographic camera types are currently available.

### Lights

- Lights use a single color and do not support node-based light definitions.
- Spot light Size does not affect cone softness, unlike Cycles.
- Area light Beam spread is unsupported.

### Light Probes

- Up to 128 light probe spheres may be active simultaneously.
- Up to 16 light probe planes can be active within the view frustum.
- Active light probe volumes must reside within Light Probes Volume Memory Pool.

### Indirect Lighting

- Light probe capture does not handle specular reflection; specular energy becomes diffuse.

### Shadows

- Shadow Map Raytracing may cause light leaks due to overlapping shadow sources. Reduce step count, enable jitter, or scale down light geometry to mitigate.
- Thin geometry (e.g., single-wall structures) leaks light on shadowed faces. Add thickness or lower Resolution Limit.

### Volumetrics

- Only single scattering is supported.
- Volumetric rendering affects camera rays only; reflections, refractions, and probes exclude volumetrics.
- Volumetric shadowing applies only to volumes and not to solid surfaces.
- Volumetric shadowing is restricted to the camera view frustum.

### Depth of Field

- Blended materials may exhibit artifacts with post-process blur but render correctly with sample-based methods. Disable post-process depth of field by setting Max Size to zero.

### Screen Space Effects

Scene representation relies on the depth buffer rather than ray-triangle intersection, which reduces complexity and increases performance but limits effect computation to visible areas. Only the nearest surface depth is recorded per pixel.

This architecture imposes constraints:

- Effects vanish past screen borders. The overscan feature partially alleviates this.
- Effects lack depth thickness information. Most provide a thickness parameter to govern pixel consideration.
- Occluded objects are excluded from calculations.
- Blended surfaces are invisible to these effects; they bypass the depth prepass.
- Objects in Holdout Collections do not render with screen space effects.

### Raytracing

- Blended and raytrace refraction materials do not appear in dithered material reflections.
- Blended materials are incompatible with raytracing.
- Only one refraction layer is correctly modeled. Secondary refraction can be approximated using the Thickness workflow.
- Only dithered materials without Raytrace Refractions can undergo refraction.

### Shader Nodes

- All BSDFs employ approximations for real-time performance, producing small visual differences from Cycles.
- Several utility nodes are incompatible with EEVEE.
- Certain BSDF combinations generate more noise than others, particularly Diffuse BSDF mixed with Refraction BSDF.
- Flat shaded displaced surfaces split into triangles.

See also
See Nodes Support for the complete unsupported node list.

[Related references](INDEX.md).
