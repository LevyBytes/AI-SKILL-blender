# Menu Switch Node

## Menu Switch Node

The Menu Switch node outputs one of its inputs by a selected menu item, evaluating only the active input for efficient switching. The menu entries are user-defined — added, removed, renamed, and reordered in the editor sidebar, and renaming an entry keeps the matching input socket's links. It works in node groups and the nodes-modifier UI: connecting the menu input to a Group Input node exposes the menu as a group input, and a menu socket in a group, reroute, or other pass-through node must connect to a Menu Switch node to work (an unconnected menu socket shows an empty menu). Connecting several Menu Switch nodes to the same output socket conflicts (even with identical entries), avoidable by wrapping a menu switch in a node group, since multiple groups of the same type share the same menu switch. (The Index Switch Node is similar but exposes the choices as an integer index.) Inputs: Menu (which input socket passes through), with one input per entry — the selected entry's input is evaluated and passed, labels renamable via Ctrl-LMB on the socket name or the Properties panel, more inputs added by dragging a connection onto the bottom empty socket or clicking the header icon, and unused inputs not computed (improving performance). Properties: Type (the data type handled). Outputs: Output (the value from the selected item's input, unchanged) plus a Boolean output per entry — true for the selected one, false for the rest — usable to trigger branches, control visibility, or drive conditional operations.

Passes one of its inputs through to the output based on an active menu selection.
Only the chosen input evaluates, making it efficient for switching between alternatives.

Menu entries are user-defined and editable through the editor sidebar or node properties.
The menu can appear in node groups when linked to a Group Input node.
For a menu socket to function in node groups or reroute nodes, it must connect to a Menu Switch node;
unconnected menu sockets show an empty menu.

If different menus connect to the same output, Blender reports a conflict.
Wrapping the Menu Switch in a node group avoids this, since identical group instances share the same internal switch.

See also: The Index Switch Node for switching via integer index.

**Inputs**

Menu
Selects which input socket to pass through.

Each menu entry creates one input socket. The active entry's input evaluates and propagates to the output.

Labels can be edited via Ctrl-LMB on the socket name or in the Properties panel.

New inputs are added by:
- Dragging onto the empty socket below the list
- Clicking the header icon

Inactive inputs skip evaluation, improving performance on large graphs.

**Properties**

Type
Sets the data type handled by the node.

**Outputs**

Output
Passes the selected input without modification.

For each menu entry, a Boolean output is also created.
The active entry's Boolean is true; all others are false.
Use these to activate downstream branches, toggle visibility, or control conditional logic.

### Menu Switch Node

The Menu Switch node passes one of its inputs through based on the menu item picked. Only the active input is evaluated, which makes switching between options efficient.

You define the menu entries yourself. Entries can be added, removed, renamed and reordered in the editor sidebar; renaming one keeps the existing links on its input socket.

The menu works in node groups and in the nodes modifier UI. Wire the menu input to a Group Input node and it shows up as a group input. A menu socket inside a node group, a reroute node, or other pass-through nodes has to reach a Menu Switch node to do anything; left unconnected, it shows an empty menu by default.

Hooking several Menu Switch nodes to the same output socket causes a conflict, even with identical menu entries. Wrapping a menu switch in a node group sidesteps it: several node groups of the same type can share one menu, since they all contain the same menu switch node.

| Description | Description |
| --- | --- |
| Conflict caused by connecting different menus. | Same node group can be connected without conflict. |

See also

The Index Switch Node is similar, but it exposes the choices as an integer index.

### Inputs

Menu
Decides which input socket passes through to the output.

One input is spawned per menu entry, and whichever input matches the chosen item gets evaluated and forwarded onward.

Relabel a menu item via Ctrl - LMB over its socket name, or from the node's Properties panel.

Two ways to add input sockets:
- Drop a connection onto the spare socket sitting at the bottom of the list.
- Hit the icon up in the node header.

Inputs nobody uses stay uncomputed, a help to performance across crowded node networks.

### Properties

Type
Decides the type of data the node handles.

### Outputs

Output
Passes through the value from the input tied to the selected menu item, unchanged.

A Boolean output is also spawned per menu entry. The one belonging to the chosen item reads true , the rest false . You can wire these Booleans to fire separate node branches, switch things visible or hidden, or steer conditional behaviour anywhere else in the tree.

[Related references](INDEX.md).
