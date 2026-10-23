# bpy.types.NodeCombineBundle: properties

## NodeCombineBundle(NodeInternal)

### NodeCombineBundle(NodeInternal)

base classes: bpy_struct, Node, NodeInternal
class bpy.types. NodeCombineBundle ( NodeInternal )

Merge several socket values down into a single one.
active_index

Position of the currently active item (in [0, inf], default 0)

Type :

int
bundle_items

(default None, readonly)

Type :

NodeCombineBundleItems[NodeCombineBundleItem]
define_signature

Have this node establish a bundle signature for other nodes to use (default False)

Type :

bool

[Related references](INDEX.md).
