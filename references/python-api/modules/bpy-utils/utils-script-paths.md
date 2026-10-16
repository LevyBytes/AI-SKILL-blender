# bpy.utils: bpy.utils. script_paths ( * , subdir = None , user_pref = True , check_all = False , use_user = True , use_system_environment = True )

bpy.utils. script_paths ( * , subdir = None , user_pref = True , check_all = False , use_user = True , use_system_environment = True ) 

Give back a list of valid script paths.

Parameters :

- subdir ( str | None ) – Optional subdir.

- user_pref ( bool ) – Include the user preference script paths.

- check_all ( bool ) – Add local, user and system paths instead of only the ones Blender uses.

- use_user ( bool ) – Include user paths

- use_system_environment ( bool ) – Include `BLENDER_SYSTEM_SCRIPTS` variable path

Returns :

script paths.

Return type :

list[str]

[Related references](INDEX.md).
