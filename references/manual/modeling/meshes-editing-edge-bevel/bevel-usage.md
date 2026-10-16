# Bevel: Usage

## Bevel

Smooths out corners and edges to create realism—physical objects lack infinite sharpness. The Bevel Modifier performs this non-destructively.

Reference — Mode: Edit Mode | Menu: Vertex ‣ Bevel Vertices, Edge ‣ Bevel Edges | Shortcut: Shift - Ctrl - B (vertices), Ctrl - B (edges)

Usage: Select vertices, edges, or faces; press Ctrl - B (edges and corners) or Shift - Ctrl - B (corners only). Move mouse to increase radius; scroll wheel adjusts segment density. Confirm with LMB/Return; cancel with RMB/Esc.

While active, settings display at viewport top. Keyboard shortcuts (status bar) select settings; mouse or numeric input changes values. Hold Shift for slower precision; Ctrl snaps to coarse increments. After LMB confirmation, Adjust Last Operation panel retains setting access.

Affect — Target selection:
- Vertices: Bevel selected vertices, leaving edges unchanged
- Edges: Bevel selected edges plus vertices where 3+ edges meet

Width Type (M) — Width meaning (examples below use 50% for Percent, 1.0 for others): Offset, Width, Depth, Percent, Absolute

Width (A): Bevel size/radius (meaning depends on Width Type)

Note: Multi-edge beveling sometimes prevents simultaneous width matching; Bevel compromises. Disabling Loop Slide (below) can ease this.

Segments (S): Density of new geometry; higher = smoother result; adjustable with Wheel while active

Profile Shape (P): Number 0–1 controlling bevel profile shape (side view). For Miter Outer/Inner set to Arc, also controls miter shape.

Material Index: 0-based material slot for new faces; -1 inherits neighbors' materials

Harden Normals (H): Custom split normals on new faces for smooth shading without affecting rest of mesh

Clamp Overlap (C): Prevents beveled edges overshooting past neighboring face ends

Loop Slide: Whether new inner edges align perpendicular to beveled edge (off) or match existing inner edge direction (on)

Mark section:

Seams (U): When beveling 3+ edges sharing a vertex with 2 marked UV Seams, new edges between them also mark as Seams

Sharp (K): Like Mark Seams, but for Sharp edges

Miter Outer (O): For 3+ edges at one vertex forming 180°+ corner on face side, Outer Miter determines extra geometry creation to prevent pinching

Miter Inner (I): For 2+ edges at one vertex forming <180° corner on face side, Inner Miter determines extra geometry creation

Spread: Inner Miter arc size; also affects Outer Miter

Intersection Type (N) — Multi-edge intersection geometry:
- Grid Fill: Smoothly connect edges with geometry
- Cutoff: Cap each edge with flat face

Face Strength — Face strength application for bevel faces (works with Weight Normals Modifier, Face Influence checked):
- None: No face strength set
- New: New edge faces = Medium strength; new vertex faces = Weak
- Affected: New case + adjacent faces = Strong
- All: Affected case + remaining faces = Strong

Profile Type (Z) — Generated-edge flow along beveled edge:
- Superellipse: Auto profile from Profile Shape setting
- Custom: Custom profile from Curve Widget in Adjust Last Operation panel; side view of bevel between 90° faces; darkened area = mesh interior

Presets: Support Loops and Steps presets auto-generate based on Segments count; if segments change, reapply preset.

Sample Straight Edges: Whether to sample profile mid-segment on perfectly straight curve segments (Vector-handle lines). Disabled by default; control-point sampling usually sufficient.

Sample Even Lengths: By default, each profile segment (control-point pieces) gets equal sample points. Enable to distribute samples evenly along full profile length instead.

### Bevel

Reference

Mode:

Edit Mode

Menu:

Vertex → Bevel Vertices , Edge → Bevel Edges

Shortcut:

Shift - Ctrl - B (Bevel Vertices), Ctrl - B (Bevel Edges)

Bevel rounds corners and edges. This aids realism – in the real world, nothing stays infinitely sharp.

Cubes without and with bevel.

See also

The Bevel Modifier performs rounding non-destructively.

### Usage

Pick one or more vertices, edges, or faces, then press Ctrl - B to smooth both edges and corners, or Shift - Ctrl - B for corners alone. Drag to increase bevel radius and scroll to adjust geometry density.
Finally, press LMB / Return to apply or RMB / Esc to cancel.

| Description | Description | Description |
| --- | --- | --- |
| Before beveling. | Increased bevel width. | Increased bevel segments. |

[Related references](INDEX.md).
