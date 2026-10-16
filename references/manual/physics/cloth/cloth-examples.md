# Examples

## Examples

Examples and workflows.

To begin cloth simulation, first add a plane and delete the default cube. Subdivide the plane several times (approximately eight subdivisions yield good fabric flexibility). Tab into Edit Mode and subdivide.

Activate cloth via the Physics tab: locate Cloth panel and click Cloth. Numerous settings appear; most are initially ignored.

Basic setup is complete. Playback shows modest results—the following sections cover pinning and collision for better dynamics.

Using Simulation to Shape/Sculpt a Mesh

Apply the Cloth Modifier at any frame to freeze the mesh at that point. Re-enable cloth with adjusted start/end frames to continue simulation.

Example: define a flag as a grid and pin its edge to a pole. Simulate 50+ frames until the flag settles. Apply the Cloth Modifier. For flapping animation, re-enable cloth during in-camera frames.

Smoothing of Cloth

Post-simulation, cloth often appears blocky. Apply Smooth and/or Subdivision Surface Modifier via the Modifiers tab. In the Toolbar, find Edit panel and press Smooth.

Cloth on Armature

Pin clothing to bones (e.g., loose tunic to waist).

Workflow:
- Bind-pose armature.
- Model clothing (enclosing, non-penetrating).
- Parent to armature.
- Create pinned-vertex group per cloth object.
- Add vertices + weight (≥1). E.g., belt area, weight 1.
- Physics tab: mark cloth. Stack Cloth below Armature Modifier.
- Cloth Shape: select vertex group.
- Collision on character mesh.
- Unpinned → Cloth; pinned → Armature.

Note: animate from bind pose, moving gradually (multiple frames). Instant/teleport jumps break physics.

Regression blend-file.

Cloth with Animated Vertex Groups

Animated pinned-vertex cloth:
Regression blend-file.

Unsupported: Starting with goal = 0 and increasing (with vertex unpinned) fails; no on-the-fly goal springs.

Cloth with Dynamic Paint

Cloth + Dynamic Paint + animated vertex groups:
Regression blend-file.

Unsupported: Same as above—goal = 0 to 0.5 with unpinned vertex fails.

Using Cloth for Soft Bodies

Soft-body simulation via cloth.

Cloth simulates soft bodies (not its primary function, but functional). Example uses standard Rubber material, default settings, Alt - A playback.

Blend-file: Using Cloth for soft bodies.

Cloth with Wind

Flag with wind force applied.

Cloth wind/self-collision regression blend-file (includes image-above setup):
Cloth flag with wind and self-collisions.

[Related references](INDEX.md).
