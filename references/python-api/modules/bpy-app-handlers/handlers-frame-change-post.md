# bpy.app.handlers: bpy.app.handlers. frame_change_post

bpy.app.handlers. frame_change_post
Called after a frame change for playback and rendering, once the data has been evaluated for the new frame. Accepts one or two arguments: the scene data-block, and optionally the dependency graph being updated.
Type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]

[Related references](INDEX.md).
