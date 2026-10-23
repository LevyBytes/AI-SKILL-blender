# bpy.types.BlendDataNodeTrees: methods

class bpy.types. BlendDataNodeTrees ( bpy_prop_collection )

Collection of node trees
## BlendDataNodeTrees(bpy_prop_collection)

Registry of scene element instances.

base classes: bpy_prop, bpy_prop_collection
new ( name , type ) 

Register a node tree in the database

Parameters :

- name ( str ) – New name for the data-block (never None)

- type ( Literal [ 'GeometryNodeTree' , 'CompositorNodeTree' , 'ShaderNodeTree' , 'TextureNodeTree' ] ) – Type, The type of node_group to add

- GeometryNodeTree
Geometry Node Editor – Advanced geometry editing and tools creation using nodes.

- CompositorNodeTree
Compositor – Create effects and post-process renders, images, and the 3D Viewport.

- ShaderNodeTree
Shader Editor – Edit materials, lights, and world shading using nodes.

- TextureNodeTree
Texture Node Editor – Edit textures using nodes.

Returns :

New node tree data-block

Return type :

NodeTree
remove ( tree , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Unregister a node tree from the current file

Parameters :

- tree (NodeTree) – Node tree to remove (never None)

- do_unlink ( bool ) – Break all references to this node tree before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)
tag ( value ) 

tag

Parameters :

value ( bool ) – Value
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

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
