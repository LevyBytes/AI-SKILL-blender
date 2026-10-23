# bpy.types.NodeSeparateBundle: properties

## NodeSeparateBundle(NodeInternal)

### NodeSeparateBundle(NodeInternal)

base classes: bpy_struct, Node, NodeInternal
class bpy.types. NodeSeparateBundle ( NodeInternal )

Break a bundle apart into several sockets.
active_index

Index of the active item (in [0, inf], default 0)

Type :

int
bundle_items

(default None, readonly)

Type :

NodeSeparateBundleItems[NodeSeparateBundleItem]
define_signature

When set, this node lays down a bundle signature for other nodes to follow (default False)

Type :

bool

[Related references](INDEX.md).
