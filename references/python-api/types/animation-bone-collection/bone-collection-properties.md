# bpy.types.BoneCollection: properties

## BoneCollection(bpy_struct)

### BoneCollection(bpy_struct)

base class: bpy_struct
class bpy.types.BoneCollection(bpy_struct)

A grouping of bones within an Armature data-block
bones

Bones that belong to this collection. While the armature is in edit mode this list always comes back empty, because collection memberships are only reconciled once edit mode is exited. (default None, readonly)

Type:
bpy_prop_collection[Bone]
child_number

Position of this collection in its parent's child list. Locating it requires scanning every bone collection, so use it sparingly. (in [-inf, inf], default 0)

Type:
int
children

(default None, readonly)

Type:
bpy_prop_collection[BoneCollection]
index

Position of this collection within the armature.collections_all array. Locating it requires scanning every bone collection, so use it sparingly. (in [-inf, inf], default 0, readonly)

Type:
int
is_editable

The collection belongs to a local Armature, or entered the current blend file through a library override (default False, readonly)

Type:
bool
is_expanded

Shows this collection in an unfolded state within the bone collections tree view (default False)

Type:
bool
is_local_override

The collection entered the current blend file through a library override (default False, readonly)

Type:
bool
is_solo

Display this bone collection alone, together with any others also flagged as 'solo' (default False)

Type:
bool
is_visible

The collection's bones become viewable while in pose or object mode (default False)

Type:
bool
is_visible_ancestors

True when every ancestor of this bone collection is flagged visible; root collections are always True (default False, readonly)

Type:
bool
is_visible_effectively

Indicates real viewport visibility for this bone collection. It is True when both this collection and all of its ancestors are visible, or when it is flagged as 'solo'. (default False, readonly)

Type:
bool
name

Unique within the Armature (default "", never None)

Type:
str
parent

Parent bone collection. Reading this requires scanning every bone collection to locate the parent.

Type:
BoneCollection
bones_recursive

A set of all bones assigned to this bone collection and its child collections.

(readonly)

[Related references](INDEX.md).
