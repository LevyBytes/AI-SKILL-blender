# Node Groups

## Node Groups

Grouping nodes can simplify a node tree by hiding complexity and reusing common functionality. A node group is recognizable by its green title bar. Conceptually, node groups let you treat a set of nodes as a single unit — much like functions in programming: reusable, composable, and parametrizable. For instance, say you build a "Wood" material and want it in several colors: rather than duplicating the whole setup per color (a pain to maintain if you later change the grain detail), move the wood-pattern nodes into a node group, have each material reuse that group and pass its own color in, and then any grain-detail change is made once, inside the group. Node groups can be nested — a group can contain other groups.
Note: recursive node groups are forbidden to prevent infinite recursion; a group cannot contain itself, directly or indirectly.
Tip: like other data-blocks, node groups whose names start with . are hidden from menus and lists and reachable only via search — handy for node-asset authors who want internal utility groups hidden from end users.

Group Input and Group Output nodes represent the data flowing into and out of the group. The Group Input node exposes the group's input sockets from inside it; these act as parameters that steer the group's behavior from outside, and you connect them to internal nodes to drive values such as factors, colors, or geometry inputs.
Note: input values that don't affect the output are grayed out.
The Group Output node defines what the group passes out; only sockets connected to it become outputs on the group itself.
Important: avoid using output nodes such as Material Output inside node groups — keep those on the top-level node tree to make groups more reusable. Use Group Output to pass data out of a node group.

Usage — Managing Inputs/Outputs: add, remove, and reorder input/output sockets in the Group panel in the Sidebar; you can also create a socket directly by dragging a link to or from the hollow socket on the Group Input or Group Output node to another socket in the editor.
Reusing Node Groups (Menu: Add ‣ Group; Shortcut: Shift-A): once defined, a node group can be placed again, in the same tree or another, and you can import groups from another blend-file via File ‣ Link/Append.
Tip: when appending groups from another blend-file, Blender doesn't distinguish types like material vs. compositing groups, so adopt a naming convention — prefixes such as Mat_, Comp_, Geo_ — to signal each group's context.

Properties — Group (Panel: Sidebar ‣ Group ‣ Group): properties about the group node, such as its name and look.
Name — the node's name shown in the Title.
Description — the message shown when hovering the Title or in add menus.
Color Tag — the group's color tag, which influences the header color.
Node Width — the width for newly created group nodes.
(Set Default Node Width) — set the width from the parent group node in the current context.
Show Manage Panel (Geometry Nodes) — show the Manage panel in Geometry Nodes modifiers when creating a modifier from a node-group asset.
Usage (Geometry Nodes) — this panel shows only in the Geometry Node Editor.
- Modifier: the group is meant for the Geometry Nodes Modifier.
- Tool: the group is meant to be used as a tool.
The data-block menu in the Geometry Node Editor header lists only groups whose Usage matches the current Node Tree Sub-Type.
Tip: if you disable both Usages by accident, the group drops off the data-block menu; to get it back, add it as a node in another group (Add ‣ Group), select it, press Tab to enter it, and re-enable a Usage.

Group Sockets (Panel: Sidebar ‣ Group ‣ Group Sockets): add, remove, reorder, and edit a node group's interface elements, defining how sockets appear on the group node and organizing them for clarity and usability. Available item types:
- Inputs: define the group's input sockets.
- Outputs: define the group's output sockets.
- Panels: group related sockets together for structuring complex setups; panels always sit at the bottom of the node interface and can be nested by dragging one panel onto another in the interface item list.
- Panel Toggle: add a boolean checkbox to a panel's header to control its contents; available only when a panel is selected in the interface item list. Panel toggles have their own options under the Panel Toggle subpanel, and a toggle socket isn't listed directly — a panel with a toggle instead shows a boolean socket icon by its name; unlink it from the panel to make the toggle socket visible again.
Note: a panel toggle doesn't automatically disable or grey out its sockets; to disable sockets visually and functionally, use a Switch Node or similar logic and disconnect the socket manually.
Interface Item List — a UI list view of all input/output sockets and panels; each item can be renamed and configured individually, and its name appears in the node's user interface.

The Group panel contains properties for the group node itself. Name identifies the node uniquely within its tree. Label provides a custom title displayed in the header (not required to be unique). Color Tag influences header appearance. Node Width sets width for newly created group nodes; (Set Default Node Width) bases it on the parent.

Show Manage Panel Geometry Nodes enables the Manage panel in Geometry Nodes modifiers when creating from a node group asset.

Usage (Geometry Nodes only): Modifier indicates use with Geometry Nodes Modifier; Tool marks it as a tool. The data-block menu in the Geometry Node Editor header only lists groups matching the current Node Tree Sub-Type. If both Usages accidentally disable, add the group to another group (Add ‣ Group), select that node, press Tab to enter, and re-enable one Usage.

The Group Sockets panel adds, removes, reorders, and edits the user interface of a node group, organizing sockets for clarity. Item types include: Inputs (define input sockets), Outputs (define output sockets), Panels (group related sockets; appear at the bottom, nestable), Panel Toggle (boolean checkbox for panel headers; toggle sockets aren't listed directly—panels with toggles show a boolean icon; toggles don't auto-disable sockets, so use Switch Nodes or disconnect manually).

The Interface Item List displays all sockets and panels; each is renamable and configurable. Selecting a socket label on the node also selects it in this list. Specials: Duplicate Item copies a socket/panel; Make Panel Toggle converts a boolean input into a panel toggle (available when a panel is selected and the active item is boolean); Unlink Panel Toggle removes the toggle relationship, making it a regular input.

Socket properties vary by type, input/output, data type, and node tree. Type specifies the socket's data type. Description provides hover text. Attribute Domain (Geometry Nodes output—Integer, Color, Vector, Boolean, Float) indicates the geometry element type. Default Attribute (Geometry Nodes input) sets the default attribute name for modifiers. Subtype interprets and displays data; changing subtype doesn't alter the underlying type, only presentation. Integer subtypes: None (standard), Percentage (0–100), Factor (0.0–1.0 normalized). Float subtypes: None, Percentage, Factor, Mass (scene units), Angle (degrees/radians per scene settings), Time (Scene Relative—frames converted to seconds by frame rate), Time (Absolute—seconds), Distance (scene length units), Wavelength (mm/µm/nm/pm), Color Temperature (Kelvin), Frequency (hertz). Vector subtypes: None, Percentage (each component as percentage), Factor (normalized), Translation (scene units), Direction (typically normalized), Velocity (speed/direction), Acceleration (velocity rate), Euler Angles, XYZ (Cartesian, with optional W component). String subtypes: None (standard text), File Path (file selection dialogs). Dimensions Vector sets component count: 2D (X, Y), 3D (X, Y, Z), 4D (X, Y, Z, W). Default is the value when unconnected. Min/Max limit UI controls (not data clamping). Expanded Menu shows all options at once (in node editors without labels; in modifier/operator panels with labels). Default Input (Geometry Nodes input—Integer, Vector, Matrix) is used when unconnected (requires Hide Value enabled). Optional Label indicates the label isn't necessary. Hide Value hides default values even when unconnected. Layer Selection (Geometry Nodes input boolean) takes Grease Pencil layers. Hide in Modifier (Geometry Nodes input) hides the input value in modifier interfaces. Shape (Geometry Nodes input) specifies higher-order data: Auto (most appropriate), Dynamic (flexible), Single (constants only), Field (field values), Grid (grid data structure).

Panel properties: Description provides hover text. Closed by Default collapses the panel on new nodes.

Animation controls animation data and active Actions/Slots (see Manually Assigning Actions and Slots).

Make Group (Menu: Node ‣ Make Group; Shortcut: Ctrl-G): create a new node group containing all selected nodes. Group Input and Group Output nodes are made to represent connections to the unselected nodes outside the group, with inputs routed to the Group Input and outputs to the Group Output. Grouping a single node gives a group that preserves the original node's interface (including panels and default values) and inherits its name; grouping multiple nodes builds the group with input and output sockets generated from the connections and a generic name such as "NodeGroup", "NodeGroup.001", and so on.

Insert Into Group (Menu: Node ‣ Insert Into Group): move the selected nodes into the active group node — select a set of nodes ending with the destination group node, then run the operation to move them in. The moved nodes are gathered into a group of their own (with their own group input and output nodes) to preserve their connection context, and the group's existing input/output nodes gain new sockets from the added nodes as needed. The node group must be edited to hold a single Group Input and a single Group Output node.

Edit Group (Menu: Node ‣ Edit Group; Header: Go to Parent Node Tree; Shortcut: Tab, Ctrl-Tab): with a node group selected, press Tab to move into it and see its content; press Tab again (or Ctrl-Tab) to leave and return to its parent, whether the top-level node tree or another node group. The breadcrumbs in the editor's top-left corner show where you are in the hierarchy.

Ungroup (Menu: Node ‣ Ungroup; Shortcut: Ctrl-Alt-G): remove the group and place its individual nodes into your editor workspace, losing no internal connections, so you can now link those nodes to others in your workspace.

Separate (Shortcut: P): remove the selected nodes from a node group and place them in the parent node tree — useful when nodes need editing outside a group for clarity or reuse.
Copy — duplicate the selected nodes into the parent node tree while keeping the originals inside the group, useful for reusing nodes outside the group while preserving its definition.
Move — move the selected nodes to the parent node tree, removing them from the original group, useful for simplifying a group or exposing its contents directly.

Join Group Inputs (Menu: Node ‣ Join Group Inputs; Shortcut: Ctrl-J): merge multiple selected Group Input nodes into one consolidated Group Input node where possible, preserving existing links and unifying duplicate inputs to cut clutter and simplify the node tree — useful for tidying groups that have become disorganized or hold redundant input nodes.

[Related references](INDEX.md).
