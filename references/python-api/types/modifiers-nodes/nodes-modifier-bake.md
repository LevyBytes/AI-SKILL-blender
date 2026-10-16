# bpy.types.NodesModifier: bake_directory, bake_target

bake_directory

Location on disk where the bake data is stored (default “”, never None, blend relative // prefix supported)

Type :

str
bake_target

Where to store the baked data (default 'PACKED' )

- PACKED
Packed – Pack the baked data into the .blend file.

- DISK
Disk – Store the baked data in a directory on disk.

Type :

Literal[‘PACKED’, ‘DISK’]

[Related references](INDEX.md).
