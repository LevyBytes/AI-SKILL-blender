# bpy.types.StripsMeta: new_sound ( name , filepath , channel , frame_start )

new_sound ( name , filepath , channel , frame_start )

Add a new sound strip

Parameters :

- name ( str ) – Name for the new strip (never None)

- filepath ( str ) – Filepath to movie (never None)

- channel ( int ) – Channel, The channel for the new strip (in [1, 128])

- frame_start ( int ) – The start frame for the new strip (in [-1048574, 1048574])

Returns :

New Strip

Return type :

Strip

[Related references](INDEX.md).
