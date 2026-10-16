# bpy.props.EnumProperty

```text
bpy.props.EnumProperty ( items , * , name = '' , description = '' , translation_context = '*' , default = None , options = {'ANIMATABLE'} , override = set() , tags = set() , update = None , get = None , set = None , get_transform = None , set_transform = None )
```

Defines an enumeration property.

## Parameters

- `name` (str): label displayed in the user interface.
- `description` (str): tooltip and API documentation text.
- `translation_context` (str): context used to disambiguate translated text.
- `options` (set[str]): values from Property Flag Items; enums also support `ENUM_FLAG`.
- `override` (set[str]): values from Property Override Flag Items.
- `tags` (set[str]): tags defined by the parent class.
- `items`: an iterable of item tuples or `None` separators, or a callback `items(self, context)` returning that iterable. For this callback, `context` may be `None`.
- Each item is `(identifier, name, description)`, `(identifier, name, description, number)`, or `(identifier, name, description, icon, number)`.
- The first three fields are strings: Python identifier, UI label, and tooltip/documentation text.
- `icon` is a string icon identifier or integer icon value, such as one returned by `bpy.types.UILayout.icon`.
- `number` is the unique integer identifier stored in file data. Supply it when the string identifier may change. With `ENUM_FLAG`, use power-of-two bit masks.
- An empty identifier creates a separator. A nonempty name on that tuple becomes a label above the separator; `None` creates an unnamed separator.
- For dynamic items, keep Python references to all returned strings. Otherwise Blender may behave incorrectly or crash.
- `default` (str | int | set[str] | None): an item identifier, matching numeric item value, or a set of string identifiers with `ENUM_FLAG`. String defaults cannot be used with dynamic items; the implementation accepts an integer default or `None` for a callback-driven enum.

## Callbacks

All callbacks are optional (`None` by default). `self` is the owning `bpy.types.bpy_struct`; `context` is `bpy.types.Context`.

- `update(self, context) -> None` runs when the value changes. Blender does not guard against infinite recursion in this callback.
- `get(self) -> int` reads the value using custom storage rather than Blender's default storage. Without a matching `set`, the property is read-only even without `READ_ONLY`.
- `set(self, value: int) -> None` writes the value through custom storage. A setter without a matching getter is invalid.
- `get_transform(self, stored_value: int, is_set: bool) -> int` transforms the stored value when read. `is_set` says whether the property has been set.
- `set_transform(self, new_value: int, stored_value: int, is_set: bool) -> int` transforms a value before storage. The stored value is raw, before any `get_transform` operation.

Both transform callbacks must respect the property's limits, including numeric bounds and array length where applicable. Invalid results raise `ValueError`.

Returns an opaque `_PropertyDeferred` definition for property registration.

[Related references](INDEX.md).
