# Geometry Nodes Modifier: Bake, Named Attributes, Move to Nodes Operator

#### Bake

Bake Target
Sets where baked data goes. Individual bakes can override the choice.

Packed :

The baked data is folded into the .blend file, so no separate file is needed.

Disk :

The baked data lives in its own directory on disk.

Bake Path
The on-disk spot where baked data for
Simulation Zones
and Bake Nodes ends up.

See also

Geometry Node Baking

#### Named Attributes

Here you get a rundown of every custom named attribute the node group makes use of.
Further detail lives on the
geometry nodes inspection page.

### Move to Nodes Operator

Spins up a fresh geometry node tree named after the current one with .wrapper tacked onto the end.
Every input and output from the former modifier is shifted across into a new node group.
For the operator to work, the node group needs both a Group Input and a Group Output,
each wired to a Geometry socket.
As a result, all Output Attributes turn into Internal Dependencies driven by the
Store Named Attribute Node.
All of the modifier's "inputs" then become inputs of the freshly made node group as well.

Where this operator earns its keep is in letting a node tree be reused across other trees,
or tagged as an Asset for reuse in separate projects.

[Related references](INDEX.md).
