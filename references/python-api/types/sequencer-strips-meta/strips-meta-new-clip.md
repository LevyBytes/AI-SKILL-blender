# bpy.types.StripsMeta: new_clip ( name , clip , channel , frame_start )

new_clip ( name , clip , channel , frame_start )

Add a new movie clip strip

Parameters :

- name ( str ) – Name for the new strip (never None)

- clip (MovieClip) – Movie clip to add (never None)

- channel ( int ) – Channel, The channel for the new strip (in [1, 128])

- frame_start ( int ) – The start frame for the new strip (in [-1048574, 1048574])

Returns :

New Strip

Return type :

Strip

[Related references](INDEX.md).
