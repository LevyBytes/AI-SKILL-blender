# Editing UVs: Show/Hide Faces, Reveal Hidden - Alt - H

Show/Hide Faces

Mode: Edit Mode
Menu: UV ‣ Show/Hide Faces

Reveal Hidden: Alt - H

Hide Selected: H

Hide Unselected: Shift - H

Export UV Layout

Mode: Edit Mode
Menu: UV ‣ Export UV Layout

When using external applications, this exports the UV layout so you know where on the mesh you are painting.

Note: This is an add-on activated by default.

Proportional Editing

Mode: Edit Mode
Header: Proportional Editing
Menu: UV ‣ Proportional Editing
Shortcut: O

Proportional Editing works in UV editing with the same controls as in the 3D Viewport. See Proportional Editing in 3D for complete reference.

UV Options

Mode: Edit Mode
Menu: UVs

Live Unwrap
Continuously unwraps selected UV islands when transforming pinned vertices. This differs from the Live Unwrap option in the 3D Viewport.

Round to Pixels
During UV transforms, Round to Pixels helps match features in the image and ensures precise horizontal, vertical, or diagonal alignment.

Note: Round to Pixels applies after any snapping modes.

Disabled: UVs don't round.

Corner: UVs round to the nearest pixel corner.

Center: UVs round to the nearest pixel center.

Constraining to Image Bounds

For standard textures, this prevents UVs from moving outside the 0-1 range. For UDIM textures, this prevents UVs from moving outside the nearest UDIM tile.

3D Viewport UV Operations

Rotate UVs

Editor: 3D Viewport
Mode: Edit Mode
Menu: Face ‣ Face Data ‣ Rotate UVs

The UV orientation on each face is defined by that face. If an image appears upside down or sideways, use Face ‣ Rotate UVs in 3D Viewport Face Select mode to rotate UVs in 90-degree increments per face.

Reverse UVs

Editor: 3D Viewport
Mode: Edit Mode
Menu: Face ‣ Face Data ‣ Reverse UVs

Reverse UVs mirrors the UVs per face, flipping the image so it displays reversed.

[Related references](INDEX.md).
