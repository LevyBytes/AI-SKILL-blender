# Node Editors

## Node Editors

Header: holds menus, buttons, and options that depend partly on the current node tree type.
View: change your view of the editor.
Select: select a node or groups of nodes.
Add: add nodes.
Node: act on the selected nodes.
Pinned: when enabled, the editor always shows the currently selected node tree regardless of changes to the active object or scene, letting you edit a material, texture, or compositor node tree independently of the 3D Viewport selection or active scene; handy when working across objects or scenes while keeping the editor on one specific tree.
Parent Node Tree: leave the current node group and return to the parent node group/tree.
Snapping: change options for snapping node positions for a cleaner node tree layout (see Arranging Nodes).

Overlays: information drawn on top of the nodes and node trees; a toggle beside the overlay popover shows or hides all overlays for the node editor.
Wire Colors: color node links by their connected sockets.
Reroute Auto Labels: label Reroute Nodes from the label of connected reroute nodes.
Context Path: show breadcrumbs in the upper-left corner marking the hierarchy location of the displayed node tree/group.
Annotations: show Annotations in the preview region.
Previews: show each node's Preview when that node's preview is also toggled on.
Timings: show each node's last execution time; available only for compositing and geometry nodes (for geometry nodes, see Node Timings Overlay).

Toolbar: a set of tools for use in the node editor.
Select: select or move nodes and links.
Select Box: select nodes or links by dragging a box around them.
Select Circle: select nodes or links by clicking or dragging with a circular brush.
Select Lasso: select nodes or links by drawing a free-form lasso.
Annotate: draw free-hand annotation.
Annotate Line: draw a straight-line annotation.
Annotate Polygon: draw a polygon annotation.
Annotate Eraser: erase previously drawn annotations.
Link Cuts: delete connections between nodes by drawing a line across the links (see Cut Links).
Mute Links: mute connections by drawing a line across the links; muted links stay in place but are ignored in evaluation (see Mute Links).
Add Reroute: insert a Reroute Node point on links by drawing a line across them; reroute nodes help organize complex node trees by redirecting connections.

Sidebar: properties for the currently selected node plus node-editor-specific settings.
Node (Panel: Sidebar ‣ Node): properties controlling the active node's behavior and appearance; available options depend on the node type and the editor.
Node:
- Name: a unique identifier for the node within its node tree, used internally for references.
- Label: a custom title shown at the top of the node; unlike Name it need not be unique, and it helps organize complex node trees.
- Color: by default the node background color follows the current theme; enable this to override it with a custom color (useful as a visual cue to group related nodes or highlight important parts), with the preset button beside the color field for saving and reusing custom colors.
- Node Color Specials — operators related to custom node colors. Copy to Selected — copy the active node's color to all selected nodes.
- Show Options: show or hide extra node-specific options in the node header, where the node type offers them.
- Mute: temporarily disable the node without removing it; where possible it's bypassed and its inputs pass straight to its outputs.
- Propagation (Geometry Nodes): control which of this node's messages propagate to the parent node group or modifier: All Messages (informational messages, warnings, and errors), Errors and Warnings (only warnings and errors), Errors (only error messages), or None (no messages).
Properties: the properties shown depend on the selected node's type (a Mix node differs from a Mask node).
Custom Properties: create and manage your own properties to store data on the active node (see the Custom Properties page).
Tool (Panel: Sidebar region ‣ Tool) — Active Tool: this panel's info changes with the selected tool.
View (Panel: Sidebar region ‣ View) — Annotations: select the Annotate tool in the Toolbar to make annotations in the node editor (see Annotate Tool).

Navigating: done with both mouse movement and keyboard shortcuts.
Pan (MMB): move the view up, down, left, and right.
Zoom (Ctrl-MMB, Wheel): move the camera forward and back.
Frame Selected (NumpadPeriod): zoom to fit only the selected nodes in the view.
Frame All (Home): zoom to fit all nodes in the view.

Adding Nodes (Menu: Add; Shortcut: Shift-A): add nodes from the editor header's Add menu or with the keyboard shortcut. You can also add a node by dragging a connection from an existing node's input or output socket and dropping it over empty space instead of onto another socket — this opens a search menu of compatible nodes and their sockets that can be added and connected to the existing node, and confirming the selection adds the node for you to move and place.

[Related references](INDEX.md).
