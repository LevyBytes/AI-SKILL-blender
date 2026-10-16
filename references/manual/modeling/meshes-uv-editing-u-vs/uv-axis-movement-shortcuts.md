# Editing UVs: Move on Axis, Use these shortcuts to move UVs directly

Move on Axis

Mode: Edit Mode
Menu: UV ‣ Move on Axis

Moves selected UV coordinates along a chosen axis by a specified distance. Designed for precise adjustments and supports multiple movement modes, especially useful with number pad keys.

Use these shortcuts to move UVs directly:

Numpad8 / Numpad2 — Move up or down.

Numpad4 / Numpad6 — Move left or right.

Type

Movement unit:

Dynamic — Move using active grid size. Ctrl + number pad activates this.

Pixel — Move by pixel increments. Shift + number pad activates this.

UDIM — Move by full UV tiles (1.0 unit). Number pad without modifiers uses this.

Axis

Direction to move:

X Axis — Move horizontally.

Y Axis — Move vertically.

Distance — The distance to move, in selected units.

Copy UVs

Mode: Edit Mode
Menu: UV ‣ Copy UVs
Shortcut: Ctrl - C

Copy UVs stores the topology and UV coordinates of selected islands into an internal clipboard for use with Paste UVs.

Note: The internal clipboard is not shared between Blender instances.

Paste UVs

Mode: Edit Mode
Menu: UV ‣ Paste UVs
Shortcut: Ctrl - V

Paste UVs matches the topology of a stored island to currently selected islands. If a match is found, the stored UVs paste onto the selection.

For example, if a triangle-quad-quad sequence is stored, selecting a different triangle-quad-quad elsewhere pastes the stored UVs onto the new selection.

For best results, use the Rip tool or UV ‣ Split ‣ Selection before pasting.

[Related references](INDEX.md).
