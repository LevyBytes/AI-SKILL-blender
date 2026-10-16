# Face Sets: Initialize Face Sets, Grow/Shrink Face Sets, Expand Face Set, Extract Face Set

### Initialize Face Sets

Reference

Mode:
Sculpt Mode

Menu:
Face Sets ‣ Initialize Face Sets

Prepares all Face Sets at once leveraging one of multiple connectivity characteristics.

Mode
The connectivity characteristic defining Face Set divisions.

By Loose Parts:
One Face Set per unconnected component.

By Face Set Boundaries:
One Face Set per separated Face Set.
Good for dividing Face Set Expand
design into distinct Face Sets for modification.

By Materials:
One Face Set per Material assignment.

By Normals:
Face Sets matching comparable surface angles.

By UV Seams:
Face Sets utilizing UV divisions as splits.

By Edge Creases:
Face Sets utilizing Edge Crease marks as divisions.

By Edge Bevel Weight:
Face Sets utilizing Bevel marks as divisions.

By Sharp Edges:
Face Sets utilizing Sharpness marks as divisions.

Threshold
Baseline value for designating a characteristic as a split in Face Set generation.

### Grow/Shrink Face Sets

Reference

Mode:
Sculpt Mode

Menu:
Face Sets ‣ Grow/Shrink Face Sets

Tool:
Edit Face Set

Shortcut:
Ctrl - W , Ctrl - Alt - W

Enlarges or diminishes the Face Set under the cursor by introducing or eliminating neighboring polygons.

### Expand Face Set

Note

Further data on Face Set Expand at the Expand section.

### Extract Face Set

Reference

Mode:
Sculpt Mode

Menu:
Face Sets ‣ Extract Face Set

Constructs a separate mesh from the chosen Face Set.
Post-initiation, position over the target Face Set and LMB to build the fresh mesh.
Upon finishing the fresh mesh gets picked in Object Mode.

[Related references](INDEX.md).
