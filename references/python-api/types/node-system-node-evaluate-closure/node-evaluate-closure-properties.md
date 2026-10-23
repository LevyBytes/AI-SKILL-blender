# bpy.types.NodeEvaluateClosure: properties

## NodeEvaluateClosure(NodeInternal)

### NodeEvaluateClosure(NodeInternal)

base classes: bpy_struct, Node, NodeInternal
class bpy.types. NodeEvaluateClosure ( NodeInternal )

Run the supplied closure.
active_input_index

Position of the currently active item (in [0, inf], default 0)

Type :

int
active_output_index

Position of the currently active item (in [0, inf], default 0)

Type :

int
define_signature

Have this node establish a closure signature for other nodes to use (default False)

Type :

bool
input_items

(default None, readonly)

Type :

NodeEvaluateClosureInputItems[NodeEvaluateClosureInputItem]
output_items

(default None, readonly)

Type :

NodeEvaluateClosureOutputItems[NodeEvaluateClosureOutputItem]

[Related references](INDEX.md).
