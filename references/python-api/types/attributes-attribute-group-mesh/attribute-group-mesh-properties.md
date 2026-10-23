# bpy.types.AttributeGroupMesh: properties

## AttributeGroupMesh(bpy_prop_collection)

Collection of geometry attributes on mesh.

base classes: bpy_prop, bpy_prop_collection
class bpy.types. AttributeGroupMesh ( bpy_prop_collection )

Container of per-element data channels.
active

Active attribute

Type :

Attribute
active_color

Active color attribute for display and editing

Type :

Attribute
active_color_index

Active color attribute index (in [-inf, inf], default 0)

Type :

int
active_color_name

The name of the active color attribute for display and editing (default "", never None)

Type :

str
active_index

Active attribute index or -1 when none are active (in [-1, inf], default 0)

Type :

int
default_color_name

The name of the default color attribute used as a fallback for rendering (default "", never None)

Type :

str
render_color_index

The index of the color attribute used as a fallback for rendering (in [-inf, inf], default 0)

Type :

int

[Related references](INDEX.md).
