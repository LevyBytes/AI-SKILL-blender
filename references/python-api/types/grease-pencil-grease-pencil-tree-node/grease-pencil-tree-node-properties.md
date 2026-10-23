# bpy.types.GreasePencilTreeNode: properties

## GreasePencilTreeNode(bpy_struct)

### GreasePencilTreeNode(bpy_struct)

base class: bpy_struct

subclasses —
GreasePencilLayer, GreasePencilLayerGroup
class bpy.types. GreasePencilTreeNode ( bpy_struct )

An entry in the Grease Pencil layer tree, representing either a single layer or a group.
channel_color

Color of the channel in the dope sheet (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
hide

Set tree node visibility (default False)

Type :

bool
lock

Protect tree node from editing (default False)

Type :

bool
name

The name of the tree node (default "", never None)

Type :

str
next_node

The tree node sitting just after (above) this one in the layer tree (readonly)

Type :

GreasePencilTreeNode
parent_group

The group that contains this layer tree node (readonly)

Type :

GreasePencilLayerGroup
prev_node

The tree node sitting just before (below) this one in the layer tree (readonly)

Type :

GreasePencilTreeNode
select

Tree node is selected (default False)

Type :

bool
use_masks

Let the layers in the masks list drive how drawings in this tree node show or hide (default True)

Type :

bool
use_onion_skinning

Show onion skins on either side of the current frame (default True)

Type :

bool

[Related references](INDEX.md).
