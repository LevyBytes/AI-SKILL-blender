# Collections: Collections Tab, Visibility, View Layer, Instancing

## Collections

### Collections

Complex scenes often contain many objects: furniture, props, lights, backdrops, and more. Blender supports gathering objects into logical groups without imposing transform dependencies (distinct from parenting). This grouping capability aids organization and facilitates cross-file or cross-scene sharing.

### Collections Tab

Reference

Menu :

Properties ‣ Collection Properties

The Collection Properties tab supplies immediate access to settings for the selected collection.

Collection properties.

### Visibility

Selectable
Toggles selectability of collection objects in the 3D Viewport.

Useful when elements have been positioned and you prefer to avoid accidental selection while focusing on other content—for example, reference images.

Show In – Renders
Enables/disables collection visibility in renders.

#### View Layer

Each collection may be configured per View Layer for flexible rendering control. These settings permit including or excluding specific collections, masking objects, or controlling indirect contributions.

Include
Incorporates this collection in the active View Layer. Disabling hides all collection objects from renders, viewport, and the Outliner for the current view layer.

Enables alternate scene versions or isolates components for compositing work.

Holdout
Designates all collection objects as holdouts in the active view layer.

Holdout objects render as transparent regions, masking anything behind them. This is typically used in compositing to generate masks or separate foreground from background content.

See also

Holdout Shader Node

Indirect Only Cycles Only
Collection objects do not appear directly in the final image but contribute through lighting, shadows, and reflections.

Valuable for clean product shots while maintaining realistic environment lighting or reflections.

### Instancing

Instance Offset X, Y Z
Applies a spatial shift for instanced collections relative to the original object's position.

[Related references](INDEX.md).
