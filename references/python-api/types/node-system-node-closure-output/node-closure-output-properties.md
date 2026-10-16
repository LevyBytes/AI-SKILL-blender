# bpy.types.NodeClosureOutput: properties

## NodeClosureOutput(NodeInternal)

### NodeClosureOutput(NodeInternal)

base classes — bpy_struct, Node, NodeInternal
class bpy.types. NodeClosureOutput ( NodeInternal )
active_input_index

Position of the currently active item (in [0, inf], default 0)

Type :

int
active_output_index

Position of the currently active item (in [0, inf], default 0)

Type :

int
define_signature

Have this zone establish a closure signature for other nodes to use (default False)

Type :

bool
input_items

(default None, readonly)

Type :

NodeClosureInputItems[NodeClosureInputItem]
output_items

(default None, readonly)

Type :

NodeClosureOutputItems[NodeClosureOutputItem]

[Related references](INDEX.md).
