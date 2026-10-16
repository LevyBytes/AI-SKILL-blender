# bpy.types.Context: Methods: temp_override

temp_override ( * , window = None , screen = None , area = None , region = None , ** keywords )

A context manager that swaps out chosen context members for the duration of a block.

Parameters :

- window (bpy.types.Window | None) – Window override or None.

- screen (bpy.types.Screen | None) – Screen override or None.

Note

Moving into or out of full-screen areas and temporary screens is not handled. Hand in one of those screens and an exception is raised; operations that exit the context with such screens won't bring back the previous screen.

Note

A screen swap reaches further than the other arguments, since it can pull the workspace along — and the scene too, where pinning applies.

- area (bpy.types.Area | None) – Area override or None.

- region (bpy.types.Region | None) – Region override or None.

- keywords – Additional keywords override context members.

Returns :

The context manager.

Return type :

ContextTempOverride

Use a context override to bring a different window / area & region to the foreground for a moment, or to swap in members like the active_object or bone .

Notes:

- The window, area, and region arguments have to agree with one another: a region you pass must belong to the current area or to the area you also pass. Likewise the area must belong to the current window.

- These overrides can sit inside one another; nesting simply layers the new members on top of the overrides already in place.

- Once the context-manager's block ends, the members go back to what they were. The lone exception is when the underlying data has since vanished.

Should the windowing data disappear (for one reason or another), the context simply keeps whatever state it currently holds.
Although it's an unusual situation, deliberate window actions — closing windows, or loading another file — wipe out the windowing data that was assigned before the temporary context began.

Setting up the context after a file load is one good use, since otherwise it would be None. For instance:

```python
import bpy
from bpy import context

### Reload the current file and select all.
bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)
window = context.window_manager.windows[0]
with context.temp_override(window=window):
    bpy.ops.mesh.primitive_uv_sphere_add()
    ### The context override is needed so it's possible to set edit-mode.
    bpy.ops.object.mode_set(mode='EDIT')
```

Here is how you can drop an object into the scene under a different window.

```python
import bpy
from bpy import context

win_active = context.window
win_other = None
for win_iter in context.window_manager.windows:
    if win_iter != win_active:
        win_other = win_iter
        break

### Add cube in the other window.
with context.temp_override(window=win_other):
    bpy.ops.mesh.primitive_cube_add()
```

[Related references](INDEX.md).
