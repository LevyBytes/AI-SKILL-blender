# bpy.types.NodeTreeInterface: new_socket, new_panel

new_socket ( name , * , description = '' , in_out = 'INPUT' , socket_type = 'DEFAULT' , parent = None ) 

Append a fresh socket to the interface.

Parameters :

- name ( str ) – Name, Name of the socket (never None)

- description ( str ) – Description, Description of the socket (optional, never None)

- in_out ( Literal [ 'INPUT' , 'OUTPUT' ] ) – Input/Output Type, Create an input or output socket (optional)

- INPUT
Input – Generate a input node socket.

- OUTPUT
Output – Generate a output node socket.

- socket_type ( Literal [ 'DEFAULT' ] ) – Socket Type, Type of socket generated on nodes (optional)

- parent (NodeTreeInterfacePanel) – Parent, Panel to add the socket in (optional)

Returns :

Socket, New socket

Return type :

NodeTreeInterfaceSocket
new_panel ( name , * , description = '' , default_closed = False ) 

Append a fresh panel to the interface.

Parameters :

- name ( str ) – Name, Name of the new panel (never None)

- description ( str ) – Description, Description of the panel (optional, never None)

- default_closed ( bool ) – Default Closed, Panel is closed by default on new nodes (optional)

Returns :

Panel, New panel

Return type :

NodeTreeInterfacePanel

[Related references](INDEX.md).
