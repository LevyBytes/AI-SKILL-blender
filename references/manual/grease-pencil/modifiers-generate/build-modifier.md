# Build Modifier

## Build Modifier

The Build Modifier animates strokes to appear or vanish across a frame range, producing the illusion of lines being drawn or erased.

Note: This documentation addresses Build Modifier for Grease Pencil. Refer to the general Build Modifier for other object types.

Mode: Sequential—one stroke changes at a time. Concurrent—multiple strokes change together. Additive—only newly added strokes animate compared to the prior keyframe, assuming Additive Drawing was used and shared strokes remain identical.

Transition (Sequential/Concurrent): Grow reveals points in order, simulating drawing. Shrink hides points backward, simulating erasure. Vanish conceals points forward, simulating fading ink.

Timing: Natural Drawing Speed uses recorded stylus speed (Sequential/Additive only); Speed Factor multiplies recorded velocity. Maximum Gap sets longest gap in seconds. Number of Frames: Fixed frame count for animation. Frames: Maximum frame count used. Delay: Frames to wait after each keyframe before the modifier activates. Percentage Factor: Manual visibility percentage (0–1 range). Factor: Visibility percentage. Time Alignment (Concurrent only): Align Start means all strokes begin together. Align End means all strokes finish together. Object: Stroke appearance order based on distance to a reference object.

Custom Range: If enabled, affects only the specified frame interval. Start/End: Range frame values.

Fade: Factor defines fade strength. Thickness: Fade applied to thickness. Opacity: Fade applied to opacity. Weight Output: Assigns weight values to points finishing/beginning fade.

Influence Filters: See Influence Filters.

This modifier sequences the appearance or disappearance of object faces over a time interval, advancing by default in creation order (changeable via Sort Mesh Elements in Edit Mode).

Start Frame marks when the building process begins.

Length specifies the number of frames for the build sequence.

Reversed inverts the effect, causing a deconstruction where faces progressively vanish; useful for gradually hiding sets of instanced objects.

Randomize shuffles the order in which faces build.

Seed controls the randomization pattern; the same seed always produces the same sequence for a given mesh.

Common use: instancing vertices from a vertex-only mesh with the Build modifier creates a workaround for semi-random item layouts (leaves, balls on a surface) without particle system limitations like clustering and gaps.

[Related references](INDEX.md).
