# bpy.ops.geometry.color_attribute_add

bpy.ops.geometry.color_attribute_add(*, name='', domain='POINT', data_type='`FLOAT_COLOR`', color=(0.0, 0.0, 0.0, 1.0))

Insert a tint attribute to the form

Parameters:

- name (str) – Name, Title of the new tint attribute (optional, never None)
- domain (Literal[Color Attribute Domain Items]) – Domain, Classification of component that attribute is held via (optional)
- data_type (Literal[Color Attribute Type Items]) – Data Type, Kind of material retained in attribute (optional)
- color (Sequence[float]) – Color, Base fill tint (sequence of 4 items, in [0, inf], optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
