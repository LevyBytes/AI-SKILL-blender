# Selecting: Toolbar Selection Tools, Tweak, Select Box, Select Circle

## Selecting

### Selecting

Out of the box, LMB is what Blender selects with. Swap it to RMB in the Preferences if you prefer.

Across the various editors, Blender offers several selection tools.

Note

A few editors stray from the shortcuts listed below. Most, for example, add a single item with Shift - LMB, but the Outliner uses Ctrl - LMB. Likewise, a Lasso Select is Ctrl - RMB in most editors, yet node editors use Ctrl - Alt - LMB.

Most selection tools ship in two variants — one in the Toolbar, the other in the Select menu. The names sit almost on top of each other (Select Box in the Toolbar versus Box Select in the menu), but they work a bit differently. People arriving from other applications tend to find the Toolbar variants more familiar.

### Toolbar Selection Tools
Click an item and every Toolbar selection tool acts the same: it selects that item and drops any prior selection. Hold Shift as you click and the item joins the selection (if it wasn't selected) or leaves it (if it was).

Dragging is where the tools part ways.

### Tweak
Reference

Tool :

Toolbar ‣ Tweak

Shortcut :

W

Dragging an item will move it around.

### Select Box
Reference

Tool :

Toolbar ‣ Select Box

Shortcut :

W

Drag out a rectangle and, on release, every item partly or fully inside it gets selected. (Everything else is deselected.)

Drag with Shift held down to fold the items into the existing selection; hold Ctrl instead to take them out.

A Spacebar press mid-drag lets you reposition the rectangle with the mouse.

| Description | Description | Description |
| --- | --- | --- |
| Start. | Selecting vertices. | Complete. |

### Select Circle
Reference

Tool :

Toolbar ‣ Select Circle

Shortcut :

W

Drag and whatever the circle sweeps across gets selected. Anything it missed is deselected.

Drag with Shift held down to fold the items into the existing selection; hold Ctrl instead to take them out.

The circle's radius is adjustable in the tool settings (found in the area header, the Tool tab of the Sidebar N, or the Active Tool tab of the Properties editor).

Note

In Object Mode: where Select Box grabs an object the moment the box touches any part of its geometry, Select Circle only picks one up if the circle crosses its origin point. That origin shows as an orange dot on selected objects but stays invisible on unselected ones, unless "Origins (All)" is turned on in the Viewport Overlays.

Other modes — Edit Mode and Pose Mode among them — don't show this behavioural quirk.

| Description | Description | Description |
| --- | --- | --- |
| Start. | Selecting vertices. | Complete. |

[Related references](INDEX.md).
