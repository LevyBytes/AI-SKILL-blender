# bpy.types.NodeSocket: methods

bl_system_properties_get ( * , do_create = False )

DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

Parameters :

do_create ( bool ) – Ensure that system properties are created if they do not exist yet (optional)

Returns :

The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested

Return type :

PropertyGroup
draw ( context , layout , node , text )

Draw socket

Parameters :

- context (Context) – (never None)

- layout (UILayout) – Layout, Layout in the UI (never None)

- node (Node) – Node, Node the socket belongs to (never None)

- text ( str ) – Text, Text label to draw alongside properties (never None)
draw_color ( context , node )

Color of the socket icon

Parameters :

- context (Context) – (never None)

- node (Node) – Node, Node the socket belongs to (never None)

Returns :

Color, (array of 4 items, in [0, 1])

Return type :

bpy_prop_array[float]
classmethod draw_color_simple ( )

Color of the socket icon. Used to draw sockets in places where the socket does not belong to a node, like the node interface panel. Also used to draw node sockets if draw_color is not defined.

Returns :

Color, (array of 4 items, in [0, 1])

Return type :

bpy_prop_array[float]
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
