# Geometry Node Editor

## Geometry Node Editor

The Geometry Node editor edits Node Groups used by the Geometry Node Modifier; such a group can define plenty of operations to reshape an object's geometry. A full list of Geometry Nodes lives in the modeling section, and the Nodes page covers working with nodes in general.

Interface - Header:
Node Tree Sub-Type: Geometry Nodes can take on several contexts depending on what the group is for, and switching context adapts the UI to suit it. Modifier creates groups meant for the Geometry Nodes Modifier; Tool creates groups meant for Node-Based Tools.
View: the standard view menu.
Select: the menu for Selecting Nodes.
Add: the menu for adding new Geometry Nodes.
Node: the menu for Editing Nodes.
Geometry Node Group: a data-block menu for creating and choosing node groups.
/ Pinned — the pin button holds the current node-group selection fixed instead of following the Active Modifier; a pinned group stays visible in the editor even when you select another object or modifier elsewhere.
Parent Node Tree: jumps up a node-group level (see Edit Group).
Snapping: snapping options (see Arranging Nodes).
Overlays: see Overlays.

Toolbar:
Select: see Selecting Nodes.
Annotate: see Annotations.
Links Cut: see Cut Links.

Sidebar:
Node: reaches the active node's properties.
Tool: reaches the active tool's settings.
View: manages annotations.
Group: edits the current node group's inputs and outputs.
Tip: within the Geometry Node Modifier you're able to supply values for the root node group's inputs and choose destination Attributes for its outputs.

Tool Context: these popover menus show in the header once the tool context is on, and their properties decide where in the UI the tool is offered (see Supported Modes & Object Types).
Types: which Object Types the tool works with: Mesh covers Mesh Objects, Hair Curves covers Curve Objects, Grease Pencil covers Grease Pencil Objects, and Point Cloud covers Point Cloud Objects.
Modes: which Object Modes it runs in: Object Mode, Edit Mode, Sculpt Mode, and Draw Mode (Grease Pencil), enabling the group across Object, Edit, Sculpt, and Grease Pencil Draw modes respectively.
Options - Wait for Click: holds for a mouse click (LMB) before running the operator from a menu, which helps with the Mouse Position Node.

[Related references](INDEX.md).
