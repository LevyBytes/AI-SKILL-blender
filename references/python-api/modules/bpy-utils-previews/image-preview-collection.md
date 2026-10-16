# bpy.utils.previews.ImagePreviewCollection

class bpy.utils.previews. ImagePreviewCollection 

A dict-like container of previews.

It derives from Python's built-in dict type
and holds several image previews.

Note

- instance with bpy.utils.previews.new

- keys must be str type.

- values will be bpy.types.ImagePreview
clear ( ) 

Clear all previews.
close ( ) 

Shut the collection and wipe every preview.
load ( name , filepath , file_type , force_reload = False ) 

Build a new preview from the given file path.

Parameters :

- name ( str ) – The name (unique id) identifying the preview.

- filepath ( str | bytes ) – The file path to generate the preview from.

- file_type ( Literal [ 'IMAGE' , 'MOVIE' , 'BLEND' , 'FONT' , '`OBJECT_IO`' ] ) – The type of file, needed to generate the preview.

- force_reload ( bool ) – If True, run the thumbnail manager again even when the preview is already cached.

Returns :

The Preview matching given name, or a new empty one.

Return type :
new ( name ) 

Build a new empty preview.

Parameters :

name ( str ) – The name (unique id) identifying the preview.

Returns :

The Preview matching given name, or a new empty one.

Return type :

[Related references](INDEX.md).
