# Editing UVs: Pack Islands, Pinned islands can have additional restrictions applied.

Pack Islands

Mode: Edit Mode
Menu: UV ‣ Pack Islands

Pack Islands optimizes the UV layout by adjusting islands to fill the texture space efficiently. Based on options selected, the tool scales, translates, and rotates islands, ensuring specified margins exist between them to maximize UV space.

Pinned islands can have additional restrictions applied.

Shape Method

How to consider each island's shape:

Exact Shape (Concave) — Uses the island's complete shape, including holes and concave regions.

Boundary Shape (Convex) — Accounts for the boundary (Convex Hull), not placing islands inside holes.

Bounding Box — Uses the simple bounding box.

Scale — Scale islands to fill the unit square, or pack toward the lower left corner.

Rotate — Allows rotation alongside translation and scaling to optimize usage.

Rotation Method

Allowable rotations:

Any — Any rotation improving packing.

Axis-aligned — Islands rotate to fit the smallest rectangle, then only 90-degree turns.

Cardinal — Only 90-degree rotations (like compass directions).

Margin Method

How empty space is calculated:

Scaled — Multiply margin by the scale of existing UVs.

Add — Simple addition of margin.

Fraction — Precise fraction specification of the UV unit square (slower).

Margin — Scale for empty space between islands.

Lock Pinned Islands

Pinned Islands are those with any pinned UVs. When enabled, they stay in place while others pack around them.

Lock Method

How Pinned Islands are packed:

Scale — Pinned Island scale doesn't change.

Rotation — Pinned Islands don't rotate.

Rotation and Scale — Pinned Islands translate only.

Merge Overlapping

Detects and temporarily combines overlapping islands before packing, preserving their relative rotation and position.

Pack To

Where islands end up after packing:

Closest UDIM — Pack to the UDIM grid nearest the selection center.

Active UDIM — Pack to the active UDIM image tile or the UDIM grid at the 2D cursor.

Original bounding box — Find the original bounding box, pack islands, then move them back inside.

Custom Region — Pack into a user-defined custom region (requires Custom Region enabled). Allows packing into reserved atlas regions, trim sheet zones, or texture slot layouts.

Pack Islands performance depends heavily on selected options. Fastest results use "Bounding Box" shape method and "Add" margin method. Enabling "Rotate" slightly impacts performance but often improves efficiency. The "Fraction" margin method requires significantly more computation and may take 10 times longer. "Exact shape" and "Boundary shape" methods are much slower than "Bounding Box".

[Related references](INDEX.md).
