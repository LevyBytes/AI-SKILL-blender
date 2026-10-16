# bpy_extras.node_utils

## bpy_extras submodule (bpy_extras.node_utils)

### bpy_extras submodule (bpy_extras.node_utils)
bpy_extras.node_utils. connect_sockets ( input , output ) 

Link two sockets inside a node tree.

This helps because links made via the regular Python API come out
invalid when one of the sockets is a virtual socket (the grayed-out sockets in
Group Input and Group Output nodes).

It stands in for node_tree.links.new(input, output)

Parameters :

- input (bpy.types.NodeSocket) – The input socket.

- output (bpy.types.NodeSocket) – The output socket.
bpy_extras.node_utils. find_base_socket_type ( socket ) 

Determine the socket's base class.

A socket may carry a subtype such as NodeSocketFloatFactor,
yet only the base type is permitted, e.g. NodeSocketFloat

Parameters :

socket (bpy.types.NodeSocket) – The socket to find the base type for.

Returns :

The base socket type identifier.

Return type :

str
bpy_extras.node_utils. find_node_input ( node , name ) 

Locate a node input socket by its name.

Since names aren't unique, the first match is returned.

Parameters :

- node (bpy.types.Node) – The node to search.

- name ( str ) – The name of the input socket.

Returns :

The input socket or None if not found.

Return type :

bpy.types.NodeSocket | None

[Related references](INDEX.md).
