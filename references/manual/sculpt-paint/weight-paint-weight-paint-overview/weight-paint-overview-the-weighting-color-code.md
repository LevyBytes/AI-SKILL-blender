# Introduction: The Weighting Color Code

### Introduction

Vertex Groups frequently contain enormous counts of associated vertices
and therefore enormous counts of weights (one per assigned vertex).
Weight Painting presents a method to organize vast weight information
in a highly intuitive manner.

Its principal application involves character setup, where groups determine
the relative bone effects on geometry. It also controls particle output, strands, numerous
modifiers, shape keys, and more.

Vertex group in Weight Paint Mode.

Access Weight Paint Mode via the Mode selector Ctrl - Tab .
The mesh appears softly colored using a rainbow gradient.
This coloring represents the weights assigned to each vertex in the current group.
Blue signals empty (0.0) and red signals full (1.0) by default.

By applying weight brushes to the surface, you assign weights to vertices.
Initial painting automatically generates weights in the active group
(creating it if nonexistent).

Vertex Groups appear in the list popover at the header center.

### The Weighting Color Code

A cold/hot gradient visualizes weights,
where minimal values (near 0.0) display blue (cold)
and maximal values (near 1.0) display red (hot).
Intermediate values show rainbow transitions (blue, green, yellow, orange, red).

The color spectrum and their respective weights.

Additionally, Blender offers a special visual marker
(toggleable) for vertices lacking reference: They render black.
Resulting display shows referenced sections (cold/hot tones) alongside
referenced-free sections (black) simultaneously.
Most helpful when diagnosing weight issues.
Check Viewport Overlays.

Unreferenced vertices example.

Note

Customize weight gradient hues via enabling
Custom Weight Paint Range within Editing preferences.

[Related references](INDEX.md).
