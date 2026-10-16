# bpy_extras.io_utils: bpy_extras.io_utils. path_reference ( filepath , base_src , base_dst , mode = 'AUTO' , copy_subdir = '' , copy_set = None , library = None )

bpy_extras.io_utils. path_reference ( filepath , base_src , base_dst , mode = 'AUTO' , copy_subdir = '' , copy_set = None , library = None ) 

Hand back a filepath expressed relative to a destination directory, for
exporters to use.

Parameters :

- filepath ( str ) – the file path to return,
supporting blenders relative '//' prefix.

- base_src ( str ) – the directory the filepath is relative to
(normally the blend file).

- base_dst ( str ) – the directory the filepath will be referenced from
(normally the export path).

- mode ( Literal [ 'AUTO' , 'ABSOLUTE' , 'RELATIVE' , 'MATCH' , 'STRIP' , 'COPY' ] ) – the method used to reference the path.

- copy_subdir ( str ) – the subdirectory of base_dst to use when mode='COPY'.

- copy_set ( set [ tuple [ str , str ] ] | None ) – collect from/to pairs when mode='COPY',
pass to path_reference_copy when exporting is done.

- library (bpy.types.Library | None) – The library this path is relative to.

Returns :

the new filepath.

Return type :

str

[Related references](INDEX.md).
