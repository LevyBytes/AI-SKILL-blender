# bpy.types.PreferencesSystem: shader_compilation_method

shader_compilation_method

Method used to compile shaders in parallel. Subprocess needs much more RAM per worker but can finish faster on some machines. Requires a Blender restart to apply. (OpenGL only) (default 'THREAD' )

- THREAD
Thread – Compile shaders on threads.

- SUBPROCESS
Subprocess – Compile shaders in subprocesses.

Type :

Literal[‘THREAD’, ‘SUBPROCESS’]

[Related references](INDEX.md).
