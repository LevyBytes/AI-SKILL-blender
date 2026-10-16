# bpy.types.PropertyGroup: RemoveProperty

bpy.props.RemoveProperty(cls, attr)

Undefines a dynamically added property.

Parameters:

- cls (type[bpy.types.bpy_struct]) – The class hosting the property (positional argument required).

- attr (str) – Property name (keyword argument required).

Note: Typically not called directly. Instead use del cls.attr

[Related references](INDEX.md).
