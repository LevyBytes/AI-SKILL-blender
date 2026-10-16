# bpy.ops.wm.properties_edit

bpy.ops.wm. properties_edit ( * , data_path = '' , property_name = '' , property_type = 'FLOAT' , is_overridable_library = False , description = '' , use_soft_limits = False , array_length = 3 , default_int = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) , min_int = -10000 , max_int = 10000 , soft_min_int = -10000 , soft_max_int = 10000 , step_int = 1 , default_bool = (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False) , default_float = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) , min_float = -10000.0 , max_float = -10000.0 , soft_min_float = -10000.0 , soft_max_float = -10000.0 , precision = 3 , step_float = 0.1 , subtype = '' , default_string = '' , id_type = 'OBJECT' , eval_string = '' ) 

Modifies a custom property's format, or adjusts its interface presentation

Parameters :

- data_path ( str ) – Property Edit, Property data_path edit (optional, never None)

- property_name ( str ) – Property Name, Property name edit (optional, never None)

- property_type ( Literal [ 'FLOAT' , '`FLOAT_ARRAY`' , 'INT' , '`INT_ARRAY`' , 'BOOL' , '`BOOL_ARRAY`' , 'STRING' , '`DATA_BLOCK`' , 'PYTHON' ] ) – Type, (optional)

- FLOAT
Float – A single floating-point value.

- `FLOAT_ARRAY`
Float Array – An array of floating-point values.

- INT
Integer – A single integer.

- `INT_ARRAY`
Integer Array – An array of integers.

- BOOL
Boolean – A true or false value.

- `BOOL_ARRAY`
Boolean Array – An array of true or false values.

- STRING
String – A string value.

- `DATA_BLOCK`
Data-Block – A data-block value.

- PYTHON
Python – Edit a Python value directly, for unsupported property types.
- is_overridable_library ( bool ) – Library Overridable, Permits the property to be overridden when the data-block is linked (optional)

- description ( str ) – Description, (optional, never None)

- use_soft_limits ( bool ) – Soft Limits, Constrains the Property Value slider to a specific range; values outside require manual entry (optional)

- array_length ( int ) – Array Length, (in [1, 32], optional)

- default_int ( Sequence [ int ] ) – Default Value, (array of 32 items, in [-inf, inf], optional)

- min_int ( int ) – Min, (in [-inf, inf], optional)

- max_int ( int ) – Max, (in [-inf, inf], optional)

- soft_min_int ( int ) – Soft Min, (in [-inf, inf], optional)

- soft_max_int ( int ) – Soft Max, (in [-inf, inf], optional)

- step_int ( int ) – Step, (in [1, inf], optional)

- default_bool ( Sequence [ bool ] ) – Default Value, (array of 32 items, optional)

- default_float ( Sequence [ float ] ) – Default Value, (array of 32 items, in [-inf, inf], optional)

- min_float ( float ) – Min, (in [-inf, inf], optional)

- max_float ( float ) – Max, (in [-inf, inf], optional)

- soft_min_float ( float ) – Soft Min, (in [-inf, inf], optional)

- soft_max_float ( float ) – Soft Max, (in [-inf, inf], optional)

- precision ( int ) – Precision, (in [0, 8], optional)

- step_float ( float ) – Step, (in [0.001, inf], optional)

- subtype ( str ) – Subtype, (optional)

- default_string ( str ) – Default Value, (optional, never None)

- id_type ( Literal [ 'ACTION' , 'ARMATURE' , 'BRUSH' , 'CACHEFILE' , 'CAMERA' , 'COLLECTION' , 'CURVE' , 'CURVES' , 'FONT' , 'GREASEPENCIL' , '`GREASEPENCIL_V3`' , 'IMAGE' , 'KEY' , 'LATTICE' , 'LIBRARY' , 'LIGHT' , '`LIGHT_PROBE`' , 'LINESTYLE' , 'MASK' , 'MATERIAL' , 'MESH' , 'META' , 'MOVIECLIP' , 'NODETREE' , 'OBJECT' , 'PAINTCURVE' , 'PALETTE' , 'PARTICLE' , 'POINTCLOUD' , 'SCENE' , 'SCREEN' , 'SOUND' , 'SPEAKER' , 'TEXT' , 'TEXTURE' , 'VOLUME' , 'WINDOWMANAGER' , 'WORKSPACE' , 'WORLD' ] ) – ID Type, (optional)

- eval_string ( str ) – Value, Python value for unsupported custom property types (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:1872

[Related references](INDEX.md).
