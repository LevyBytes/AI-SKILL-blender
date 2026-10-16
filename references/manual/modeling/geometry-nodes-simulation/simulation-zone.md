# Simulation Zone

## Simulation Zone

Simulation Zone

Allow one frame's result to influence the next. Simple rules create complex results over time. Physics simulation is the most common type.

Two nodes define the "Simulation Zone" between them.

Inputs to Simulation Input evaluate once at start, pass to the next state and output. Other nodes link from outside, re-evaluating per frame.

No outbound links allowed. Results exit only via Simulation Output, enabling sub-frame interpolation for motion blur.

Note: Tool context not supported—Modifier context only.

Note: Anonymous attributes don't propagate unless stored in the simulation state. Detecting required anonymous attributes needs to look ahead.

Clock: The simulation ties to the animation system with sub-step support. Evaluates only on frame changes and caches like Blender's physics simulations.

Properties: Rename, shuffle, and remove inputs in the Node Editor. Sub-steps are configured here.

Inputs
Geometry: Default input for geometry into the zone. Add more items by dragging sockets into the blank or via Simulation State panel. Rename via Ctrl+LMB on the name or in Properties.
Delta Time: Time between frames in seconds (inverse of Frame Rate). Drives the simulation through rate-dependent node setups. Keeps playback consistent when frame rate changes.
Skip: Bypass the simulation zone, passing input directly to output.

Baking: Auto-caches during playback. Valid cache shows as a yellow line in the timeline, letting animators review all prior frames.

Users can opt out of "Cache" to save memory when only the current frame matters.

To render on a render-farm, bake to disk for non-sequential rendering. Note: Baking all modifiers on selected objects.

Examples: Combine with Index of Nearest to create sphere-based simulations.

[Related references](INDEX.md).
