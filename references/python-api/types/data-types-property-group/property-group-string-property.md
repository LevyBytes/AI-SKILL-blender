# bpy.types.PropertyGroup: StringProperty

bpy.props.StringProperty(*, name='', description='', translation_context='*', default='', maxlen=0, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None, search=None, search_options={'SUGGESTION'})

Constructs a property definition for a string.

Parameters:

- name (str) – Label shown in the user interface.

- description (str) – Tooltip and documentation text.

- translation_context (str) – Context string for localization disambiguation.

- default (str) – Starting string value.

- maxlen (int) – Upper bound on string length.

- options (set[str]) – Flags from Property Flag Items.

- override (set[str]) – Override flags from Property Override Flag Items.

- tags (set[str]) – Tags defined by the parent class.

- subtype (str) – Subtype from Property Subtype String Items.

- update (Callable[[bpy.types.bpy_struct, bpy.types.Context], None] | None) – Callback on value modification; receives (self, context) and must return None. Warning: no infinite-recursion protection.

- get (Callable[[bpy.types.bpy_struct], str] | None) – Callback on read when custom storage is used; receives (self) and must return the property value.

Note: If defined alone (without set), the property becomes read-only even if `READ_ONLY` is not set.

- set (Callable[[bpy.types.bpy_struct, str], None] | None) – Callback on write when custom storage is used; receives (self, value) and must return None.

Note: Cannot be defined without a matching get.

- get_transform (Callable[[bpy.types.bpy_struct, str, bool], str] | None) – Callback on read to perform additional processing; receives (self, stored_value, is_set) and returns the final transformed value.

Note: Must ensure transformed values respect all limits, or a ValueError is raised.

- set_transform (Callable[[bpy.types.bpy_struct, str, str, bool], str] | None) – Callback on write to process the given value before storage; receives (self, new_value, raw_value, is_set) and returns the final transformed value.

Note: Must ensure transformed values respect all limits, or a ValueError is raised.

- search (Callable[[bpy.types.bpy_struct, bpy.types.Context, str], Iterable[str | tuple[str, str]]] | None) – Function called to populate autocomplete options shown in the UI. Receives (self, context, edit_text) and must return a sequence, iterator, or generator. Each item must be either:

- A single string (candidate to display).

- A tuple pair (candidate, additional_info).

- search_options (set[str]) – Control set construction using:

- 'SORT' orders the results.

- 'SUGGESTION' allows user-entered values outside search results. WARNING: disabling this causes the search callback to run on every redraw, which can hurt performance if the callback is expensive.

Returns an opaque type suitable for property registration.

Returns: _PropertyDeferred

[Related references](INDEX.md).
