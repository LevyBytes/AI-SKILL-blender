# bpy.types.NodeLink: properties

## NodeLink(bpy_struct)

### NodeLink(bpy_struct)

base class: bpy_struct
class bpy.types. NodeLink ( bpy_struct )

A connection joining two nodes inside a node tree
from_node

(readonly)

Type :

Node
from_socket

(readonly)

Type :

NodeSocket
is_hidden

The link stays out of view because its sockets are not shown (default False, readonly)

Type :

bool
is_muted

The link is silenced and may be skipped (default False)

Type :

bool
is_valid

Whether the link is valid (default False)

Type :

bool
multi_input_sort_id

Determines ordering when several links feed one input; the link with the largest ID sits on top. (in [0, inf], default 0, readonly)

Type :

int
to_node

(readonly)

Type :

Node
to_socket

(readonly)

Type :

NodeSocket

[Related references](INDEX.md).
