# Materials: Surface, Volume

### Surface

Backface Culling
Hide back-facing surfaces. Enable whenever possible for performance benefit.

Camera
Apply back face culling in camera view.

Shadow
Apply back face culling during shadow casting.

Light Probe Volume
Apply back face culling during Light Probe Volume baking. Helps reject capture points inside objects to prevent light leaking.

Displacement
Governs how shader node tree displacement output affects rendering.

Bump Only:
Simulate displacement via bump mapping. Shading normals change only; vertex positions remain unaffected.

Displacement Only:
Unsupported; falls back to Displacement and Bump.

Displacement and Bump:
Combines true vertex displacement with bump mapping for fine detail. Vertex position changes.

Note
This is not precomputed and scales with render sample count. Evaluation is faster than geometry nodes or modifiers.

Note
Displacing flat shaded geometry splits adjacent faces. Supply vertex normals as a custom attribute to work around this.

Max Distance
Maximum distance a vertex can displace. Displacements beyond this threshold create visibility artifacts. Edge-of-screen geometry may disappear due to camera culling. Shadow updates may lag.

Transparent shadows
Apply transparency shadows if the material contains Transparent BSDF. Disabled rendering is faster but produces inaccurate shadows.

Render Method
Controls blending behavior and feature compatibility.

Dithered:
Enables grayscale hashed transparency, compatible with render passes and raytracing. Known as deferred rendering.

In Dithered mode, materials render in layers. Each layer can only transmit light from prior layers. If no intersection with lower layers exists, transmissive BSDFs fall back to light probes.

Raytraced Transmission
Use raytracing to compute transmitted color rather than relying solely on light probes. Prevents the surface from contributing to lighting of surfaces without this setting.

Blended:
Permits colored transparency but incompatible with render passes and raytracing. Known as forward rendering.

Sorting Problem

Blended rendering order affects final output since color blending is order-dependent. EEVEE lacks per-pixel or per-triangle sorting and uses only per-object sorting based on origin. Opaque surfaces maintain correct sorting regardless of render method.

Tip
Adjust face order in edit mode via sort element or geometry nodes.

Note
Per-object sorting costs performance; thousands of transparent objects degrade framerate significantly.

Transparency Overlap
Render all transparent fragments when enabled. When disabled, only the frontmost surface renders. Disabling fixes sorting-induced artifacts.
Blended render method only.

Thickness
Choose the model for approximating object geometry.

Sphere:
Approximate as a sphere with diameter equal to the node tree thickness value. Better for rounded objects (e.g., monkey head) and perfect for spheres.

Slab:
Approximate as an infinite slab with defined thickness. Suited to flat or thin objects (e.g., glass panels, grass blades).

From Shadow
Refine thickness using shadow maps from casting lights, taking the minimum value between shadow maps and material node tree thickness. Beneficial for objects where pre-computation is difficult (complex geometry), impossible (procedural displacement), or impractical. Incurs performance cost scaling with render samples.

### Volume

Intersection
Governs which inner mesh portion produces volumetric effects.

Intersection (continued)

Fast:
Each face acts as a medium boundary. Produces correct results for manifold geometry with no internal structure.

Accurate:
Faces act as boundaries only when consecutive faces point in opposite directions. Produces correct results as long as max ray depth is not exceeded. Requires significant additional memory compared to fast mode.

[Related references](INDEX.md).
