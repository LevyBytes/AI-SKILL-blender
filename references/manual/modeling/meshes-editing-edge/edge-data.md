# Edge Data

## Edge Data

Operators below modify edge properties affecting certain tools or modifiers. Press Ctrl - E to open Edge menu popover at mouse cursor for quick operator access.

Edge Bevel Weight:
Reference — Mode: Edit Mode | Menu: Edge ‣ Edge Bevel Weight
Interactively changes selected edges' Bevel Weight. After menu item selection, move mouse to change or type number (positive/negative) to adjust. Value displays at viewport top. Confirm with LMB/Return; cancel with RMB/Esc. Sidebar shows/edits Bevel Weight.

Edge Crease:
Reference — Mode: Edit Mode | Menu: Edge ‣ Edge Crease | Shortcut: Shift - E
Interactively changes selected edges' Crease amount. After menu/shortcut, move mouse to change or type number (positive/negative) to adjust. Value displays at viewport top. Confirm with LMB/Return; cancel with RMB/Esc. Sidebar shows/edits Crease value.

Mark/Clear Seam:
Reference — Mode: Edit Mode | Menu: Edge ‣ Mark/Clear Seam
Mark/unmark selected edges as UV Seams.

Mark/Clear Sharp:
Reference — Mode: Edit Mode | Menu: Edge ‣ Mark/Clear Sharp
Mark/unmark selected edges as Sharp. Used for:
- Sharp edge rendering and flat face rendering in otherwise smooth-shaded meshes (via vertex normal adjustment on sharp-connected vertices)
- Edge Split Modifier edge specification
- Smooth By Angle and Weighted Normal Modifier edge exclusion
- External format smoothing group export (FBX, OBJ)
Internal storage: sharp_edge attribute
See also: Is Edge Smooth Node, Set Shade Smooth Node

Set Sharpness by Angle:
Reference — Mode: Edit Mode | Menu: Edge ‣ Set Sharpness by Angle
Sets sharp edge attribute based on neighboring face angle.

Angle: Maximum face-normal angle for smooth classification
Extend: Add new sharp edges without clearing existing

Mark/Clear Freestyle Edge:
Reference — Mode: Edit Mode | Menu: Edge ‣ Mark/Clear Freestyle Edge
Mark/unmark selected edges for Freestyle lines. See Edge Marks.

[Related references](INDEX.md).
