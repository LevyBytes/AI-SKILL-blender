# bpy.types.PropertyGroup: FloatVectorProperty

bpy.props.FloatVectorProperty(*, name='', description='', translation_context='*', default=(0.0, 0.0, 0.0), min=-sys.float_info.max, max=sys.float_info.max, soft_min=-sys.float_info.max, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None, get_transform=None, set_transform=None)

Constructs a property definition for a floating-point vector.

Parameters:

- name (str) – Label shown in the user interface.

- description (str) – Tooltip and documentation text.

- translation_context (str) – Context string for localization disambiguation.

- default (Sequence[float]) – Initial sequence of floats, matching the vector size.

- min (float) – Hard minimum; assignment below this clamps to this value silently.

- max (float) – Hard maximum; assignment above this clamps to this value silently.

- soft_min (float) – Soft minimum (>= min); UI widgets cannot be dragged below this in normal interaction.

- soft_max (float) – Soft maximum (<= max); UI widgets cannot be dragged above this in normal interaction.

- step (float) – Increment/decrement step in the UI, [1, 100]; defaults to 3 (actual step is /100).

- precision (int) – Maximum decimal places displayed, [0, 6]. Exact integer values with unit 'NONE' or 'TIME' and steps divisible by 100 suppress the fractional component automatically.

- options (set[str]) – Flags from Property Flag Items.

- override (set[str]) – Override flags from Property Override Flag Items.

- tags (set[str]) – Tags defined by the parent class.

- subtype (str) – Subtype from Property Subtype Number Array Items.

- unit (str) – Unit from Property Unit Items.

- size (int | Sequence[int]) – Dimensions, [1, 32]. An int sequence defines multi-dimensional arrays.

- update (Callable[[bpy.types.bpy_struct, bpy.types.Context], None] | None) – Callback on value modification; receives (self, context) and must return None. Warning: no infinite-recursion protection.

- get (Callable[[bpy.types.bpy_struct], Sequence[float]] | None) – Callback on read when custom storage is used; receives (self) and must return the property value.

Note: If defined alone (without set), the property becomes read-only even if `READ_ONLY` is not set.

- set (Callable[[bpy.types.bpy_struct, tuple[float, …]], None] | None) – Callback on write when custom storage is used; receives (self, value) and must return None.

Note: Cannot be defined without a matching get.

- get_transform (Callable[[bpy.types.bpy_struct, Sequence[float], bool], Sequence[float]] | None) – Callback on read to perform additional processing; receives (self, stored_value, is_set) and returns the final transformed value.

Note: Must ensure transformed values respect all limits, or a ValueError is raised.

- set_transform (Callable[[bpy.types.bpy_struct, Sequence[float], Sequence[float], bool], Sequence[float]] | None) – Callback on write to process the given value before storage; receives (self, new_value, raw_value, is_set) and returns the final transformed value.

Note: Must ensure transformed values respect all limits, or a ValueError is raised.

Returns an opaque type suitable for property registration.

Returns: _PropertyDeferred

[Related references](INDEX.md).
