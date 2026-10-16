# Relax

## Relax

Relax

Mode: Edit Mode
Toolbar: Relax

The Relax tool distributes UVs more evenly by pulling vertices along UV edges to balance the unwrap.

Relax works similarly to Minimize Stretch (which operates on faces to reduce distortion) but uses a different approach. Sometimes Minimize Stretch performs better, sometimes the unwrap tool, and sometimes Relax. A common workflow uses Unwrap first, then Minimize Stretch, then touches up with Relax. Undo can restore any earlier state.

Tool Settings

Size
Controls the brush radius in pixels. Press F to interactively adjust by dragging and LMB to confirm. Type a number then enter during F to set numerically.

Strength
Controls the brush intensity. Press Shift - F to interactively adjust strength, then LMB to confirm. You can also enter numerically while in Shift - F mode.

Falloff
Controls the Strength falloff from brush center to borders. Adjust the curve shape for softer or harder effects. See Curve Widget documentation.

Curve Preset

Custom — Manually adjust curve control points or select a preset as a starting point.

Smooth — Center, border, and transition strength are evenly distributed.

Smoother — Similar to Smooth with a wider center point before tapering.

Sphere — Strength concentrates at center with steep border falloff.

Root — Similar to Sphere with a more concentrated center.

Sharp — Strongest at center, exponentially tapering to a fine point.

Linear — Center is strongest; strength consistently weakens toward borders.

Sharper — Similar to Sharp with a more condensed center.

Inverse Square — Hybrid between Smooth and Sphere.

Constant — Strength unified across the entire brush, creating a sharp border edge.

Options

Lock Borders
Locks the UV island boundary from brush effects.

Sculpt All Islands
Edits all islands, not just the island nearest the brush center at stroke start.

Method

How edge weighting is determined:

Laplacian — The classic discrete Laplace operator on the UV graph. Each edge has equal weighting, producing triangles resembling a honeycomb or quads in a square grid.

HC — Similar to Laplacian with equal weighting while preserving gradients between dense and sparse mesh regions. Uses the Humphrey's Classes operator (from "Improved Laplacian Smoothing of Noisy Surface Meshes").

Geometry — Edges weight according to the discrete Laplace operator (cotangent formula) on 3D geometry. This brings UV edge lengths closer to 3D edge lengths, resulting in less distortion across boundaries.

[Related references](INDEX.md).
