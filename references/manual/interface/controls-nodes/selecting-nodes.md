# Selecting Nodes

## Selecting Nodes

Nodes in the editor can be selected and manipulated; selections decide which nodes can be moved, duplicated, or connected. The active node (last selected) is highlighted with a lighter outline and serves as the reference for operations such as grouping or linking, and it also determines which properties show in the Sidebar and Properties Editor. Select nodes with LMB, or several at once with Shift-LMB. Blender also offers selection tools and shortcuts to pick nodes quickly by type, connections, or layout.

All (Menu: Select ‣ All; Shortcut: A) — select all nodes.
None (Menu: Select ‣ None; Shortcut: Alt-A) — deselect all nodes.
Invert (Menu: Select ‣ Invert; Shortcut: Ctrl-I) — flip the current selection, selecting the unselected nodes and deselecting the selected ones.
Box Select (Menu: Select ‣ Box Select; Shortcut: B) — click and drag to select nodes within a rectangular region (see Box Select).
Circle Select (Menu: Select ‣ Circle Select; Shortcut: C) — click and drag with a circular brush to select nodes (see Circle Select).
Lasso Select (Menu: Select ‣ Lasso Select) — draw a freeform lasso to select the nodes within the region (see Lasso Select).
Linked From (Menu: Select ‣ Linked From; Shortcut: L) — extend the selection to all nodes connected to the inputs of the selected nodes.
Linked To (Menu: Select ‣ Linked To; Shortcut: Shift-L) — extend the selection to all nodes connected from the outputs of the selected nodes.
Select Grouped (Menu: Select ‣ Select Grouped; Shortcut: Shift-G) — select nodes sharing similar properties with the active node:
- Type: all nodes of the same type (e.g. all Math nodes).
- Color: nodes with the same custom color (this means user-assigned editor colors, not the color data nodes process).
- Prefix/Suffix: nodes whose names match the same starting or ending text.
Activate Same Type Previous/Next (Menu: Select ‣ Activate Same Type Previous/Next; Shortcut: Shift-] / Shift-[) — cycle through nodes of the same type, activating the previous or next node in the tree and centering it in the view.
Find Node (Menu: Select ‣ Find Node; Shortcut: Ctrl-F) — open a search pop-up to quickly locate and select a node in the current node tree, searching by name, socket label, warning messages, or certain socket values such as strings and data-block references. Selecting a match automatically pans and centers the view on the found node and highlights it — especially useful for navigating complex networks in large node trees efficiently.

[Related references](INDEX.md).
