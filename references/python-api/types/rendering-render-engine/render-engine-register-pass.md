# bpy.types.RenderEngine: register_pass

register_pass ( scene , view_layer , name , channels , chanid , type ) 

Register a render pass that will be part of the render with the current settings

Parameters :

- name ( str ) – Name, (never None)

- channels ( int ) – Channels, (in [1, 8])

- chanid ( str ) – Channel IDs, (never None)

- type ( Literal [ 'VALUE' , 'VECTOR' , 'COLOR' ] ) – Type

[Related references](INDEX.md).
