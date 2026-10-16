# bpy.types.PropertyGroup: PointerProperty

bpy.props.PointerProperty(type, *, name='', description='', translation_context='*', options={'ANIMATABLE'}, override=set(), tags=set(), poll=None, update=None)

Constructs a property definition for a pointer to another data structure.

Parameters:

- type (type[bpy.types.PropertyGroup | bpy.types.ID]) – A subclass of PropertyGroup or ID.

- name (str) – Label shown in the user interface.

- description (str) – Tooltip and documentation text.

- translation_context (str) – Context string for localization disambiguation.

- options (set[str]) – Flags from Property Flag Items.

- override (set[str]) – Override flags from Property Override Flag Items.

- tags (set[str]) – Tags defined by the parent class.

- poll (Callable[[bpy.types.bpy_struct, bpy.types.ID], bool] | None) – Function to decide whether an item is valid for this property; receives (self, object) and returns a boolean.

Note: Return value is checked only for UI assignment. Direct property assignment can still set an "invalid" item.

- update (Callable[[bpy.types.bpy_struct, bpy.types.Context], None] | None) – Callback on value modification; receives (self, context) and must return None. Warning: no infinite-recursion protection.

Returns an opaque type suitable for property registration.

Returns: _PropertyDeferred

Note: Pointer properties cannot reference embedded IDs (e.g., bpy.types.Scene.collection, bpy.types.Material.node_tree). Access embedded IDs through their owning parent (e.g., the scene or material).

[Related references](INDEX.md).
