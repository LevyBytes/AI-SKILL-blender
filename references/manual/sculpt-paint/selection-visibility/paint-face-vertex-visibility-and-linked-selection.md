# Selection & Visibility: Hide/Unhide Faces, Hide/Unhide Vertices, The Clipping Region, Select Linked

### Hide/Unhide Faces

Hidden faces.

Conceal chosen faces as in Edit Mode using the H key, then paint the exposed areas, and finally reveal the hidden sections again with Alt - H.

### Hide/Unhide Vertices

You cannot independently hide selected faces in vertex mask selection mode. However, switching selection modes converts the selection state. A useful technique is:

- Switch to Face selection mask mode to convert to face selection.

- Refine the selection or conceal the faces.

- Switch back to Vertex Selection mask mode.

Hiding faces ensures exposed faces keep their vertices visible.

### The Clipping Region

Further constrain the paint region using the Clipping Region. Press Alt - B and drag LMB to mark a rectangular zone. The enclosed area becomes your primary region of interest, while the surrounding viewport is obscured.

The Clipping Region isolates important areas for localized work.

Restore full visibility by pressing Alt - B once more.

All paint operations respecting viewport orientation utilize this constraint, including box select and brush application.

Two visual indicators mark active clipping:

- The clipping region boundary displays as gray in the viewport

- The Info overlay indicates "Clipped" display mode

### Select Linked

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select Linked ‣ Linked

Shortcut :

Ctrl - L , Shift - L

Gather geometry connected to presently chosen elements. This proves invaluable when a mesh contains isolated, superimposed sections where standard isolation would be cumbersome. Press Shift - L to deselect linked elements.

Use L to pick linked geometry directly beneath the cursor.

[Related references](INDEX.md).
