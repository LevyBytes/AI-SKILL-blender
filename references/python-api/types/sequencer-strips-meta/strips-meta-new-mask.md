# bpy.types.StripsMeta: new_mask ( name , mask , channel , frame_start )

new_mask ( name , mask , channel , frame_start )

Add a new mask strip

Parameters :

- name ( str ) – Name for the new strip (never None)

- mask (Mask) – Mask to add (never None)

- channel ( int ) – Channel, The channel for the new strip (in [1, 128])

- frame_start ( int ) – The start frame for the new strip (in [-1048574, 1048574])

Returns :

New Strip

Return type :

Strip

[Related references](INDEX.md).
