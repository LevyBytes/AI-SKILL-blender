# SDF Fillet Node

## SDF Fillet Node

Smooths or rounds off concave internal corners in a Signed Distance Field grid. Modifies the field to soften transitions at sharp inward angles (similar to mesh fillet/bevel). Affects only negative-curvature regions (concave corners); preserves volume. Results in organic, continuous surfaces; useful after boolean operations.

Inputs:
- Grid: Input SDF to smooth (typically from boolean or mesh conversion)
- Iterations: Smoothing pass count; higher values produce larger, smoother fillet radius; increases computation time; single iteration = subtle rounding; multiple = progressively softer surfaces

Outputs:
- Grid: SDF with concave corners rounded; convertible to mesh via Grid to Mesh or usable in further volumetric work

[Related references](INDEX.md).
