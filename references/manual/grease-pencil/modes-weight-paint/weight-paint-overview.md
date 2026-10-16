# Introduction

Vertex weight assignment chiefly supports rigging strokes in cut-out animation, where vertex groups encode relative bone influences; see Using Vertex Group for guidance.

Note: a vertex in Grease Pencil is termed a point; the names interchange.

Weight Painting codifies weight data intuitively. The picked Grease Pencil object renders with subtle shading across a spectrum hue range, encoding each point's weight in the active vertex group. Conventionally, blue denotes unweighted and red denotes full weighting.

Weights are installed via painting with weight brushes; initiating paint automatically enrolls weights in the active group (generates one if absent).

**Weight Paint.**

Chosen from the Mode menu in the 3D Viewport header. Once enabled, the Toolbar reformats to Weight Paint Mode sections, and a red circle traces the cursor in the 3D Viewport.

**Weight Options.**

Multiframe — sometimes weight assignment must span multiple frames concurrently. Activate the Multiframe button next to the modes selector (faded lines icon); check Multiframe for guidance.

[Related references](INDEX.md).
