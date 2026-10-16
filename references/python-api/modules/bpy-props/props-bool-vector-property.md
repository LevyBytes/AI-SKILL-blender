# bpy.props.BoolVectorProperty

```text
bpy.props.BoolVectorProperty ( * , name = '' , description = '' , translation_context = '*' , default = (False, False, False) , options = {'ANIMATABLE'} , override = set() , tags = set() , subtype = 'NONE' , size = 3 , update = None , get = None , set = None , get_transform = None , set_transform = None )
```

Defines a Boolean array property.

## Parameters

- `name` (str): label displayed in the user interface.
- `description` (str): tooltip and API documentation text.
- `translation_context` (str): context used to disambiguate translated text.
- `options` (set[str]): values from Property Flag Items; enums also support `ENUM_FLAG`.
- `override` (set[str]): values from Property Override Flag Items.
- `tags` (set[str]): tags defined by the parent class.
- `default` (Sequence[bool]): initial values matching the declared size.
- `size` (int | Sequence[int]): dimensions in [1, 32]; a sequence declares a multidimensional array.
- `subtype` (str): value from Property Subtype Number Array Items.

## Callbacks

All callbacks are optional (`None` by default). `self` is the owning `bpy.types.bpy_struct`; `context` is `bpy.types.Context`.

- `update(self, context) -> None` runs when the value changes. Blender does not guard against infinite recursion in this callback.
- `get(self) -> Sequence[bool]` reads the value using custom storage rather than Blender's default storage. Without a matching `set`, the property is read-only even without `READ_ONLY`.
- `set(self, value: tuple[bool, ...]) -> None` writes the value through custom storage. A setter without a matching getter is invalid.
- `get_transform(self, stored_value: Sequence[bool], is_set: bool) -> Sequence[bool]` transforms the stored value when read. `is_set` says whether the property has been set.
- `set_transform(self, new_value: Sequence[bool], stored_value: Sequence[bool], is_set: bool) -> Sequence[bool]` transforms a value before storage. The stored value is raw, before any `get_transform` operation.

Both transform callbacks must respect the property's limits, including numeric bounds and array length where applicable. Invalid results raise `ValueError`.

Returns an opaque `_PropertyDeferred` definition for property registration.

[Related references](INDEX.md).
