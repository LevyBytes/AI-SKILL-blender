# bpy.app.handlers: bpy.app.handlers. exit_pre

bpy.app.handlers. exit_pre
Just before Blender shuts down, while all data is still valid. Accepts one boolean argument: True means either a user was working in Blender and exited, or Blender is exiting in a situation that should be treated that way; False means Blender is running in background mode, or is exiting due to failed command-line arguments, etc.
Type: list[Callable[[bool], None]]

[Related references](INDEX.md).
