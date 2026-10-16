# bpy.types.NodeTreeInterfaceSocket: methods — NodeTreeInterfaceSocket(NodeTreeInterfaceItem), NodeTreeInterfaceSocket(NodeTreeInterfaceItem), Inherited Properties, Inherited Functions

## NodeTreeInterfaceSocket(NodeTreeInterfaceItem)

### NodeTreeInterfaceSocket(NodeTreeInterfaceItem) 

base classes — bpy_struct, NodeTreeInterfaceItem

subclasses —
NodeTreeInterfaceSocketBool, NodeTreeInterfaceSocketBundle, NodeTreeInterfaceSocketClosure, NodeTreeInterfaceSocketCollection, NodeTreeInterfaceSocketColor, NodeTreeInterfaceSocketFloat, NodeTreeInterfaceSocketFloatAngle, NodeTreeInterfaceSocketFloatColorTemperature, NodeTreeInterfaceSocketFloatDistance, NodeTreeInterfaceSocketFloatFactor, NodeTreeInterfaceSocketFloatFrequency, NodeTreeInterfaceSocketFloatMass, NodeTreeInterfaceSocketFloatPercentage, NodeTreeInterfaceSocketFloatTime, NodeTreeInterfaceSocketFloatTimeAbsolute, NodeTreeInterfaceSocketFloatUnsigned, NodeTreeInterfaceSocketFloatWavelength, NodeTreeInterfaceSocketFont, NodeTreeInterfaceSocketGeometry, NodeTreeInterfaceSocketImage, NodeTreeInterfaceSocketInt, NodeTreeInterfaceSocketIntFactor, NodeTreeInterfaceSocketIntPercentage, NodeTreeInterfaceSocketIntUnsigned, NodeTreeInterfaceSocketMask, NodeTreeInterfaceSocketMaterial, NodeTreeInterfaceSocketMatrix, NodeTreeInterfaceSocketMenu, NodeTreeInterfaceSocketObject, NodeTreeInterfaceSocketRotation, NodeTreeInterfaceSocketScene, NodeTreeInterfaceSocketShader, NodeTreeInterfaceSocketSound, NodeTreeInterfaceSocketString, NodeTreeInterfaceSocketStringFilePath, NodeTreeInterfaceSocketText, NodeTreeInterfaceSocketTexture, NodeTreeInterfaceSocketVector, NodeTreeInterfaceSocketVector2D, NodeTreeInterfaceSocketVector4D, NodeTreeInterfaceSocketVectorAcceleration, NodeTreeInterfaceSocketVectorAcceleration2D, NodeTreeInterfaceSocketVectorAcceleration4D, NodeTreeInterfaceSocketVectorDirection, NodeTreeInterfaceSocketVectorDirection2D, NodeTreeInterfaceSocketVectorDirection4D, NodeTreeInterfaceSocketVectorEuler, NodeTreeInterfaceSocketVectorEuler2D, NodeTreeInterfaceSocketVectorEuler4D, NodeTreeInterfaceSocketVectorFactor, NodeTreeInterfaceSocketVectorFactor2D, NodeTreeInterfaceSocketVectorFactor4D, NodeTreeInterfaceSocketVectorPercentage, NodeTreeInterfaceSocketVectorPercentage2D, NodeTreeInterfaceSocketVectorPercentage4D, NodeTreeInterfaceSocketVectorTranslation, NodeTreeInterfaceSocketVectorTranslation2D, NodeTreeInterfaceSocketVectorTranslation4D, NodeTreeInterfaceSocketVectorVelocity, NodeTreeInterfaceSocketVectorVelocity2D, NodeTreeInterfaceSocketVectorVelocity4D, NodeTreeInterfaceSocketVectorXYZ, NodeTreeInterfaceSocketVectorXYZ2D, NodeTreeInterfaceSocketVectorXYZ4D
class bpy.types. NodeTreeInterfaceSocket ( NodeTreeInterfaceItem ) 

A socket declared inside a node interface.
bl_system_properties_get ( * , do_create = False ) 

DEBUG ONLY. A back door into the runtime-built RNA data store, meant purely for tests and debugging. Leave it alone during normal scripting, and never count on its contents being writable.

Parameters :

do_create ( bool ) – Create the system properties when none have been set up yet (optional)

Returns :

The root container holding the system properties; None when this data has none stored yet and creation was not asked for

Return type :

PropertyGroup
draw ( context , layout ) 

Render the socket interface's properties.

Parameters :

- context (Context) – (never None)

- layout (UILayout) – Layout, Layout in the UI (never None)
init_socket ( node , socket , data_path ) 

Set up a node socket instance.

Parameters :

- node (Node) – Node, Node of the socket to initialize (never None)

- socket (NodeSocket) – Socket, Socket to initialize (never None)

- data_path ( str ) – Data Path, Path to specialized socket data (never None)
from_socket ( node , socket ) 

Derive the template parameters from a socket that already exists.

Parameters :

- node (Node) – Node, Node of the original socket (never None)

- socket (NodeSocket) – Socket, Original socket (never None)
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default (bpy.types.Struct | None) – Fallback returned if no match is found.

Returns :

Either the matching RNA type or the supplied fallback when nothing matches.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default ( type | None ) – Fallback returned if no match is found.

Returns :

Either the matching class or the supplied fallback when nothing matches.

Return type :

type
### Inherited Properties 

| Members | Members |
| --- | --- |
| bpy_struct.id_data NodeTreeInterfaceItem.item_type NodeTreeInterfaceItem.parent | NodeTreeInterfaceItem.position NodeTreeInterfaceItem.index |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values NodeTreeInterfaceItem.bl_rna_get_subclass NodeTreeInterfaceItem.bl_rna_get_subclass_py |

[Related references](INDEX.md).
