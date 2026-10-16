# bpy.utils: bpy.utils. register_preset_path ( path )

bpy.utils. register_preset_path ( path ) 

Add a directory to the preset search paths.

Parameters :

path ( str ) – preset directory (must be an absolute path).

Inside this path there must be a "presets" subdirectory, which usually holds presets contributed by add-ons.

From an add-on's __init__.py you can invoke bpy.utils.register_preset_path(os.path.dirname(__file__))
when that __init__.py sits alongside a presets directory.
As an illustration, an operator preset would live under presets/operator/{operator.id}/,
with operator.id being the bl_idname of the operator.

Returns :

success

Return type :

bool

[Related references](INDEX.md).
