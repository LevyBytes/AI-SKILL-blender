# Uv island scaling and alignment

Average Island Scale

Mode: Edit Mode
Menu: UV ‣ Average Island Scale

Scales each UV island so all approximate the same scale.

Non-Uniform: Reduces average texture stretching within islands by scaling U and V axes independently.

Shear: Reduces average texture shearing by shearing the U axis.

Arrange/Align Islands

Mode: Edit Mode
Menu: UV ‣ Arrange/Align Islands

Aligns selected UV islands along a straight line on the UV grid. Customizable starting positions, alignment reference, sorting order, and spacing allow organizing UV layouts and modular texture pieces consistently.

Initial Position

Reference point for calculating initial alignment:

Bounding Box: Uses the bounding boxes of selected islands.

UV Grid: Aligns relative to the UV grid origin (0-1 UV tile).

Active UDIM: Aligns based on the active UDIM tile.

2D Cursor: Uses the current 2D cursor position.

Axis

The axis along which to arrange islands:

X: Align horizontally.

Y: Align vertically.

Align

How islands align relative to each other:

Min: Aligns by minimum boundary.

Max: Aligns by maximum boundary.

Center: Aligns by the center of the largest island.

None: Keeps each island's original offset and alignment.

Order

How islands are ordered:

Largest to Smallest: Sorts by area, largest first.

Smallest to Largest: Sorts by area, smallest first.

Fixed: Keeps the current selection order.

Margin

Space between arranged islands, in UV units.

[Related references](INDEX.md).
