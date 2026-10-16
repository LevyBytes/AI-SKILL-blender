# bpy.ops.wm.read_homefile

bpy.ops.wm. read_homefile ( * , filepath = '' , load_ui = True , use_splash = False , use_factory_startup = False , use_factory_startup_app_template_only = False , app_template = 'Template' , use_empty = False ) 

Reads the initial file

Parameters :

- filepath ( str ) – File Path, Location of an alternate initial file (optional, never None)

- load_ui ( bool ) – Load UI, Include user interface layout from the .blend file (optional)

- use_splash ( bool ) – Splash, (optional)

- use_factory_startup ( bool ) – Factory Startup, Read the initial ('factory startup') blend file. This is separate from the normal start-up file that users can store (optional)

- use_factory_startup_app_template_only ( bool ) – Factory Startup App-Template Only, (optional)

- app_template ( str ) – (optional, never None)

- use_empty ( bool ) – Empty, On completion, erase everything except scenes, windows, and workspaces. Permits loading the startup file with its scene structure and window arrangement preserved, minus objects, materials, animations, … (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
