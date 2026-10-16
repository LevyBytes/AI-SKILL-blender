# bpy.types.Depsgraph: properties

ids

Every data-block in its evaluated form (default None, readonly)

Type :

bpy_prop_collection[ID]
mode

Which evaluation mode is in effect (default 'VIEWPORT' , readonly)

- VIEWPORT
Viewport – Non-rendered viewport mode.

- RENDER
Render – Render.

Type :

Literal[‘VIEWPORT’, ‘RENDER’]
object_instances

Every object instance up for display or render (Warning: Treat this strictly as an iterator rather than a sequence, and hold on to no references to the items it yields) (default None, readonly)

Type :

bpy_prop_collection[DepsgraphObjectInstance]
objects

The dependency graph’s evaluated objects (default None, readonly)

Type :

bpy_prop_collection[Object]
scene

The original scene this dependency graph was built around (readonly)

Type :

Scene
scene_eval

The scene in its evaluated form (readonly)

Type :

Scene
updates

Changes affecting data-blocks (default None, readonly)

Type :

bpy_prop_collection[DepsgraphUpdate]
view_layer

The original view layer this dependency graph was built around (readonly)

Type :

ViewLayer
view_layer_eval

The view layer in its evaluated form (readonly)

Type :

ViewLayer

[Related references](INDEX.md).
