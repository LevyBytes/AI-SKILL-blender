# bpy.types.Image: pack

pack ( * , data = b'' , data_len = 0 )

Embed an image as packed data inside the .blend file.

Parameters :

- data ( bytes ) – data, Raw data (bytes, exact content of the embedded file) (optional, never None)

- data_len ( int ) – data_len, length of given data (mandatory if data is provided) (in [0, inf], optional)

[Related references](INDEX.md).
