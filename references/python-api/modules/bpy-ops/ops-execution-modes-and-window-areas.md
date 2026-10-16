# bpy.ops: execution modes and window areas

Execution Mode Control

When invoking an operator, you may optionally specify the execution mode.

This mode determines the execution context provided to the operator and whether invoke() runs in addition to execute().

`EXEC_DEFAULT` runs only execute() (the standard), but `INVOKE_DEFAULT` will also call invoke() if available.

Execution modes are:

- `INVOKE_DEFAULT`
- `INVOKE_REGION_WIN`
- `INVOKE_REGION_CHANNELS`
- `INVOKE_REGION_PREVIEW`
- `INVOKE_AREA`
- `INVOKE_SCREEN`
- `EXEC_DEFAULT`
- `EXEC_REGION_WIN`
- `EXEC_REGION_CHANNELS`
- `EXEC_REGION_PREVIEW`
- `EXEC_AREA`
- `EXEC_SCREEN`

```python
# Collection add popup.
import bpy
bpy.ops.object.collection_instance_add('INVOKE_DEFAULT')
```

An operator can also target a particular UI zone by passing the window, area, and sometimes a region.

```python
# Maximize 3d view in all windows.
import bpy
from bpy import context

for window in context.window_manager.windows:
    screen = window.screen
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            with context.temp_override(window=window, area=area):
                bpy.ops.screen.screen_full_area()
            break
```

[Related references](INDEX.md).
