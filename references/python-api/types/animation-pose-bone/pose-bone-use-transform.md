# bpy.types.PoseBone: use_transform_around_custom_shape, use_transform_at_custom_shape

use_transform_around_custom_shape

Move the bone as though parented to the Custom Shape Transform bone. Handy when blending shape-key and armature deformations. (default False)

Type :

bool
use_transform_at_custom_shape

Drive transform gizmos and other 3D Viewport transform operators from the Custom Shape Transform bone's location and orientation. With this off, the 3D Viewport keeps using the real bone transform even where the custom bone shape transform overrides it. (default False)

Type :

bool

basename

This bone's name truncated before the first . character.

(readonly)

center

The point halfway between the head and the tail.

(readonly)

children

(readonly)

children_recursive

Every descendant of this bone collected into a list.

Note

Takes O(len(bones)**2) time.

(readonly)

children_recursive_basename

Walks the descendants that share this bone's base name and returns them as a chain. Only unbroken chains work; if two or more children share a base name the fork stops the walk and nothing past it is returned.

Note

Takes O(len(bones)**2) time.

(readonly)

parent_recursive

The parents listed from the closest one outward.

(readonly)

vector

Which way the bone points.
Utility function for (tail - head)

(readonly)

x_axis

Vector aimed along the bone's x-axis.

(readonly)

y_axis

Vector aimed along the bone's y-axis.

(readonly)

z_axis

Vector aimed along the bone's z-axis.

(readonly)

[Related references](INDEX.md).
