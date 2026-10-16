# bpy.utils: bpy.utils. modules_from_path ( path , loaded_modules )

bpy.utils. modules_from_path ( path , loaded_modules ) 

Load every module found in a path and hand them back as a list.

Parameters :

- path ( str ) – this path is scanned for scripts and packages.

- loaded_modules ( set [ str ] ) – names of modules already loaded; files whose names
match these are skipped.

Returns :

all loaded modules.

Return type :

list[ModuleType]

[Related references](INDEX.md).
