# Editing Nodes

## Editing Nodes

Transform (Node ‣ Move, Rotate, Resize; G, R, S): move selected node(s) by clicking and dragging any empty part of them, or press G, move the mouse, and click LMB to confirm. Dragging a node onto an existing link smartly inserts it into the link path, generally using the first socket that matches the link type; toggle this automatic node attachment with Alt. When a node auto-attaches, the surrounding nodes shift right or left depending on the T toggle (see Auto-Offset). While dragging, press F to toggle the nodes' parent Frame: nodes inside a frame are detached from it, and nodes outside one with a frame under the cursor are attached to it. As a rule, arrange nodes so data flows left to right, top to bottom. Drag a node's left or right border to change its width. Rotating (R) and scaling (S) apply only when multiple nodes are selected and only affect their positions.

Connecting Sockets: LMB-click a socket and drag — a line ("Connect to Output") emerges, called a link; keep dragging to an input socket of another node and release LMB. An output socket can feed many links, but an input socket typically takes only one, unless it's a multi-socket input (shown as a pill-shaped socket). Hold Alt while moving a link to swap multiple links of a similar type, which also works when adding a new link into a pre-existing socket. Hold Ctrl while dragging from an output socket to reposition a node's outgoing links rather than add a new one (works for single and multiple outgoing links). A node with no connections can be inserted on a link by moving it over the link and releasing when the link highlights.
Make Links (J): select multiple nodes with open sockets, then use Make Links to create links between them; use it again to connect any other nodes that can be.
Make and Replace Links (Shift-J): works like Make Links, but replaces existing links where present.

Disconnecting Sockets:
Interactively: drag a link away from its input socket and release it, leaving it unconnected.
Mute Links (Node ‣ Mute Links; Ctrl-Alt-RMB) — activate the menu item or hold the key combination, then draw a line across one or more links to mute/unmute them; a muted link acts as though it's no longer there, which also makes the input fields for fixed values visible again. Muting the links on a reroute node's input side mutes its output side too.
Cut Links (Node ‣ Cut Links; Ctrl-RMB) — activate the menu item or hold the key combination, then draw a line across one or more links to delete them. Note: that combination is normally reserved for Lasso Select; in node editors lasso selection is instead done with Ctrl-Alt-LMB.
Detach Links (Alt-LMB drag): cut all the links attached to the selected nodes and move the nodes to a new location.

Cut/Copy/Paste (Node ‣ Cut, Node ‣ Copy, Node ‣ Paste; Ctrl-C, Ctrl-V): these operators transfer nodes within a node tree, between different trees, or even between Blender instances.
Cut: remove the selected nodes onto the clipboard, reconnecting links where possible to preserve the node flow.
Copy (Ctrl-C): copy the selected nodes to the clipboard, including the connections between them.
Paste (Ctrl-V): insert the clipboard nodes into the node tree. Note: pasted nodes land at the same coordinates they were copied from, with the same considerations as duplicating nodes. Tip: copy/paste works between Blender instances and across different node editors, provided the destination editor supports the node types.

Duplicate (Node ‣ Duplicate; Shift-D): select one or more nodes, activate the menu item or press the key combination, then move the mouse and click LMB (or press Return) to place the duplicate(s). Note: a duplicate is positioned exactly on top of its original, which is easy to miss — when unsure, select a node and move it slightly to see whether another hides underneath.
Duplicate Linked (Node ‣ Duplicate Linked; Alt-D): duplicate selected nodes but not their node trees (for group nodes), and move them.
Delete (Node ‣ Delete; X, Delete): delete the selected node(s).
Delete with Reconnect (Node ‣ Delete; Ctrl-Delete): delete the selected node(s), then create new links connecting their former input nodes to their former output nodes.
Swap (Node ‣ Swap; Shift-S): replace the selected node with another node type chosen from the menu.

When swapping nodes, existing connections auto-reconnect where possible, matching sockets by name and type; unmatched connections remain unconnected.

Muting (M) disables a node's contribution, making all links pass through as if unchanged (red appearance signals muting). Individual links can be muted separately via Mute Links.

Node Preview (Shift+H) shows/hides a preview region displaying the result after that node's operation (compositing only). Click the material ball icon to toggle.

Node Options shows/hides all node properties.

Unconnected Sockets (Ctrl+H) collapses/expands sockets with no external connections.

Collapse (H) hides the node body, displaying only the header; click the left triangle to toggle.

Collapse and Hide Unused Sockets applies both operations.

Read View Layers (Ctrl+R) loads current scene render layers from cache if Cache Result is enabled (compositing only), saving RAM and recovering render data.

Connect to Output (Shift+Alt+LMB) links the selected node's output to the final output (Material Output, World Output in Shader; Group Output in Geometry Nodes/Compositor; Output in Texture Nodes), or to Group Output if inside a group.

[Related references](INDEX.md).
