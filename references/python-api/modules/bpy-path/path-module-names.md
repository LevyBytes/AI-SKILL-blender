# bpy.path: bpy.path. module_names ( path , * , recursive = False , package = '' )

bpy.path. module_names ( path , * , recursive = False , package = '' ) 

Yield a set of instruments which can be brought in from route .

Parameters :

- path ( str ) – a listing to examine.

- recursive ( bool ) – Also yield child unit designations for packages.

- package ( str ) – Discretionary sequence, utilized as the prefix for unit designations (excluding the subsequent ".").

Returns :

a set of sequence groupings (unit_name, unit_file).

Return type :

list[tuple[str, str]]

[Related references](INDEX.md).
