# bpy.ops.preferences.studiolight_install

bpy.ops.preferences. studiolight_install ( * , files = None , directory = '' , filter_folder = True , filter_glob = '*.png;*.jpg;*.hdr;*.exr' , type = 'MATCAP' ) 

Place a hand-defined light source

Parameters :

- files ( bpy_prop_collection [ OperatorFileListElement ]) – File Path, (optional)

- directory ( str ) – directory, (optional, never None)

- filter_folder ( bool ) – Filter Folders, (optional)

- filter_glob ( str ) – filter_glob, (optional, never None)

- type ( Literal [ 'MATCAP' , 'WORLD' , 'STUDIO' ] ) – Type, (optional)

- MATCAP
MatCap – Install custom MatCaps.

- WORLD
World – Install custom HDRIs.

- STUDIO
Studio – Install custom Studio Lights.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:1110
bpy.ops.preferences. studiolight_install ( * , files = None , directory = '' , filter_folder = True , filter_glob = '*.png;*.jpg;*.hdr;*.exr' , type = 'MATCAP' )
Installs a user-defined light.
Parameters:
- files ( bpy_prop_collection [ OperatorFileListElement ]) – File Path, (optional)
- directory ( str ) – directory, (optional, never None)
- filter_folder ( bool ) – Filter Folders, (optional)
- filter_glob ( str ) – filter_glob, (optional, never None)
- type ( Literal [ 'MATCAP' , 'WORLD' , 'STUDIO' ] ) – Type, (optional)
- MATCAP — MatCap: install custom MatCaps.
- WORLD — World: install custom HDRIs.
- STUDIO — Studio: install custom Studio Lights.
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/userpref.py:1110

[Related references](INDEX.md).
