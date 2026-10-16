# bpy_extras.io_utils: bpy_extras.io_utils. axis_conversion_ensure ( operator , forward_attr , up_attr )

bpy_extras.io_utils. axis_conversion_ensure ( operator , forward_attr , up_attr ) 

Makes sure an operator holds valid axis conversion settings; meant
for use from bpy.types.Operator.check.

Parameters :

- operator (bpy.types.Operator) – the operator to access axis attributes from.

- forward_attr ( str ) – attribute storing the forward axis

- up_attr ( str ) – attribute storing the up axis

Returns :

True if the value was modified.

Return type :

bool

[Related references](INDEX.md).
