# bpy.types.StripsTopLevel: new_movie ( name , filepath , channel , frame_start , * , fit_method = 'ORIGINAL' )

new_movie ( name , filepath , channel , frame_start , * , fit_method = 'ORIGINAL' )

Add a new movie strip

Parameters :

- name ( str ) – Name for the new strip (never None)

- filepath ( str ) – Filepath to movie (never None)

- channel ( int ) – Channel, The channel for the new strip (in [1, 128])

- frame_start ( int ) – The start frame for the new strip (in [-1048574, 1048574])

- fit_method (Literal[Strip Scale Method Items]) – Image Fit Method, (optional)

Returns :

New Strip

Return type :

Strip

[Related references](INDEX.md).
