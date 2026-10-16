# bpy.ops.wm.read_factory_settings

bpy.ops.wm. read_factory_settings ( * , use_factory_startup_app_template_only = False , app_template = 'Template' , use_empty = False ) 

Initializes factory-default startup file and settings. To preserve changes, apply "Save Startup File" and "Save Preferences"

Parameters :

- use_factory_startup_app_template_only ( bool ) – Factory Startup App-Template Only, (optional)

- app_template ( str ) – (optional, never None)

- use_empty ( bool ) – Empty, On completion, erase everything except scenes, windows, and workspaces. Permits loading the startup file with its scene structure and window arrangement preserved, minus objects, materials, animations, … (optional)
Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
