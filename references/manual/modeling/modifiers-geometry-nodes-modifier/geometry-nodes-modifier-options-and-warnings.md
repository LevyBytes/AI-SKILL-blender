# Geometry Nodes Modifier: Options, Warnings, Output Attributes, Manage

## Geometry Nodes Modifier

### Geometry Nodes Modifier

What the Geometry Nodes modifier does is spin up a modifier whose behavior comes entirely from a node group you attach to it.

A new Geometry Nodes modifier with a new node group.

Objects of the mesh, curve, text, and volume kinds can all carry this modifier.

### Options

Node Group
A Node Group carrying the geometry input and output.
These are, in turn, what arrives from and gets handed to the prior and following modifier in the stack.
See Nodes for all available nodes.

Inputs
A roster of the node group's inputs, each able to hold its own value even
when several modifiers share the same group.

When the input ties into a Field socket,
a toggle appears that flips between feeding the input a single value and
drawing from an attribute on the input geometry. Drawing from an attribute lets the
value vary across every element.

Which attribute name is picked the first time a node group is used in a modifier
comes from the node group inputs panel.

Note

Whatever node the input feeds from is what sets the attribute domain and the means of reading that attribute.

### Warnings

If a node raises a warning in the node editor, that same warning surfaces here too.

You can author your own warning text with the Warning Node.

### Output Attributes

Wire a field socket into the group output node and you can mint custom Attributes
out of a Field output belonging to any node anywhere in the tree.
The attribute's domain is set in the group node's output properties.
Be aware this has no effect with Instanced Data.

Which attribute name is picked the first time a node group is used in a modifier
comes from the node group outputs panel.

This panel stays hidden unless the output node carries attribute sockets.

### Manage

Surfaces controls for handling the data held inside the node group,

You can tuck the Manage panel away by turning off Show Manage Panel
among the modifier's header options.
That governs whether the panel appears for that one specific modifier.

To keep the panel off by default on new modifiers spun up from a node group asset,
flip Show Manage Panel Geometry Nodes
in the node group's properties.

[Related references](INDEX.md).
