# Introduction

The 3D Viewport is where you interact with the 3D scene for all sorts of work — modeling, animating, texture painting, and the like.

Header Region: the header carries menus and controls that vary by current mode, and its contents fall into three groups.

Mode & Menus:
Mode (Ctrl-Tab): the 3D Viewport provides multiple modes, each for editing a different kind of data; the default Object Mode lets you place a character in the scene, while Pose Mode lets you pose it. Ctrl-Tab raises a pie menu for quick mode switching, though with an Armature selected it instead toggles between Object Mode and Pose Mode. Tab flips between Object Mode and Edit Mode for objects that support it.
View: a menu of tools for moving around in 3D space.
The remaining menus depend on the mode; the Object Mode ones follow.
Select: tools for selecting objects.
Add (Shift-A): a list of object types you can add to the scene.
Object: tools that act on objects, such as duplication; a subset is also reachable by right-clicking in the 3D Viewport.

Transform Controls:
Transform Orientation (Comma): changes the Transform Orientation, which sets the rotation of the transform gizmo.
Pivot Point (Period): changes the Pivot Point, which sets where the transform gizmo sits.
Snapping (Shift-Tab): options for snapping items to nearby ones; hold Ctrl to toggle snapping on/off for as long as the key is down.
Proportional Editing (O): smoothly transforms unselected items near the selected ones (see Proportional Editing).

Display & Shading:
Object Type Visibility: controls which object types can be seen and selected in this viewport (see Object Type Visibility).
Viewport Gizmos: sets how gizmos are drawn in the 3D Viewport.
Viewport Overlays: sets how overlays are drawn in the 3D Viewport.
Toggle X-Ray (Alt-Z): makes the whole scene transparent so you can see and select otherwise-hidden items; it's a shortcut to the X-Ray option inside the Viewport Shading popover. In Pose Mode the same button drives a separate setting with its own on/off state: rather than going transparent, it draws the armature in front of any geometry.
Viewport Shading: sets the 3D Viewport's shading.

Toolbar Region: the Toolbar holds tools that depend on the mode (modeling tools in Edit Mode, brush tools in Sculpt Mode, and so on). See Tools for more.

Sidebar Region: the Sidebar holds properties of the active object and tool, plus the viewport's own. See Sidebar for more.

Asset Shelf Region: depending on the mode, the asset shelf may be available for quick access to mode-specific assets (Pose Mode surfaces pose assets, Sculpt Mode surfaces brush assets). See Asset Shelf for more.

[Related references](INDEX.md).
