# Ray Portal BSDF

## Ray Portal BSDF

### Ray Portal BSDF

Cycles Only

This node teleports any ray that strikes it to a separate spot in the scene. Artists reach for it when building portal effects and similar specialized rendering tricks.

Its behaviour echoes that of a Transparent BSDF: render passes carry through untouched, and the cap on transparent bounces in the light-path settings still governs it.

Note

- A single portal moves rays only one way. To let them travel back as well, drop a matching portal at the spot they arrive.

- Sampling lights across a portal is not efficient, so light coming from the far side tends to look noisy. Small lamps in particular can be extremely grainy, or may never come through.

### Inputs

Color
Tints whatever rays cross the portal.

Position
Where the ray restarts on the far side. Left alone, it stays at the current spot, which equals the Position output of the
Geometry node.

Direction
Which way the ray heads on the far side. Left alone, it keeps the current viewing line, equal to the negated Incoming output of the
Geometry node.

### Properties

This node has no properties.

### Outputs

BSDF
Standard shader output.

### Examples

A typical job for this node is stitching two areas together so you get a gateway into another dimension, or "impossible spaces" whose inside is larger or smaller than the outside suggests.

Wiring it up for a trick like that means reworking the Position and Incoming outputs of the
Geometry node so they set the exit point and heading of the ray as it leaves. A few setups follow:

### Simple Offset

A bare-bones graph that just nudges the exit position. Here the ray moves 0 units on X, 4 on Y, and 5 on Z.

### Portal

Here the Location of Portal Target and Rotation of Portal Target vectors come from a target portal object by way of
Drivers.

### Camera Feed

Beyond tweaking rays, you can swap the position and heading outright, which yields tricks such as a live camera image shown on a surface.

Using the Ray Portal BSDF to reproduce a camera-feed look on a screen.

Node setup for reproducing a camera-feed style effect on a screen.

[Related references](INDEX.md).
