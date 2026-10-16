# bpy.app.handlers: bpy.app.handlers. frame_change_pre

bpy.app.handlers. frame_change_pre
Called when a frame change is triggered for playback and rendering, before any data is evaluated for the new frame. This lets you change data and relations (for example, swapping an object to another mesh) for the new frame. Note it isn't meant as a "before the frame changes" event, and the dependency graph isn't available here since data and relations may have been altered and the graph hasn't yet been updated for them. Accepts one or two arguments: the scene data-block, and optionally the dependency graph being updated.
Type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]

[Related references](INDEX.md).
