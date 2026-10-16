# Raytracing

## Raytracing

Raytracing — Indirect Surface Detail

Reference
Panel: Render ‣ Raytracing

Ray-tracing increases indirect surface lighting precision by generating rays from each BSDF and locating intersections individually.

When disabled, pre-filtered light-probes replace it, providing a faster, visually stable option when accuracy is secondary.

See also
Limitations.

Method
Select the intersection discovery technique.

Light Probe:
Use light-probe spheres and planes. Lowest tracing cost but requires manual probe placement.

Screen-Trace:
Trace rays against the screen depth buffer, falling back to light-probes if rays exit view.

Resolution
Ray-tracing resolution. Lower choices are faster, use less memory, but produce softer results.

### Screen Tracing

These settings govern screen-space ray behavior and only appear when Screen-Trace is active.

Precision
Higher values improve screen ray-tracing precision but reduce maximum trace distance. Increased precision raises performance cost.

Thickness
Pixel depth buffer thickness during tracing. Higher values stretch reflections and flicker. Lower values may cause rays to miss surfaces.

### Denoising

Enable denoising to reduce ray-traced output noise, improving stability but over-blurring output.

Spatial Reuse
Reuse neighbor pixel rays. May introduce light leaks across boundaries.

Temporal Accumulation
Re-project and accumulate prior ray tracing results. Removes fireflies but introduces color shift. Useful for viewport temporal stability or faster render convergence.

Bilateral Filter
Apply bilateral filtering to ray-traced output.

### Fast GI Approximation

Fast GI Approximation replaces ray-tracing for high-roughness BSDFs. Produces cleaner output and captures bounce lighting more efficiently than per-ray tracing.

This screen space effect inherits associated limitations.

Threshold
Highest BSDF roughness eligible for ray-tracing. Higher-roughness BSDFs progressively use Fast GI. A value of 1 ray-traces all surfaces, disabling Fast GI.

Method
Select the fast GI computation approach.

Ambient Occlusion:
Compute scene intersections to shadow distant light-probe lighting. Fastest option.

Global Illumination:
Calculate global illumination with light bouncing from surroundings.

Resolution
Fast GI computation resolution. Lower choices are faster, use less memory, but blur more.

Rays
GI rays per pixel at the chosen Resolution. Higher values reduce noise.

Steps
Screen samples per GI ray. Higher values reduce noise and boost quality.

Tip
Higher step counts decrease chances of missing light-bouncing surfaces. This allows Thickness parameters to use lower values without sacrificing light energy.

Precision
Higher values increase GI ray scene intersection precision. Increased precision raises performance cost.

Distance
If nonzero, the ceiling distance at which other surfaces contribute to fast GI. Objects farther away do not contribute.

Thickness Near
Geometric surface thickness for fast GI and ambient occlusion. Reduces light leaking and missing contact shadows. Effectiveness diminishes with distance, following inverse square rules.

Far
Angular surface thickness for fast GI and ambient occlusion. Reduces energy loss and missing occlusion of distant geometry. Higher values cause thin objects to block or reflect excess light.

Bias
Adjust shading normal to mitigate self-intersection artifacts.

[Related references](INDEX.md).
