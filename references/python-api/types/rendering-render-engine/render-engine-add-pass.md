# bpy.types.RenderEngine: add_pass

add_pass ( name , channels , chan_id , * , layer = '' ) 

Add a pass to the render layer

Parameters :

- name ( str ) – Name, Name of the Pass, without view or channel tag (never None)

- channels ( int ) – Channels, (in [0, inf])

- chan_id ( str ) – Channel IDs, Channel names, one character per channel (never None)

- layer ( str ) – Layer, Single layer to add render pass to (optional, never None)

[Related references](INDEX.md).
