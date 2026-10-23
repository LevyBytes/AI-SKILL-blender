# bpy.types.BoneCollections: properties

## BoneCollections(bpy_prop_collection)

### BoneCollections(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types. BoneCollections ( bpy_prop_collection )

This Armature's set of bone collections.
active

The bone collection currently active on the Armature.

Type :

BoneCollection
active_index

Index pointing at the Armature's active bone collection; a value of -1 signals that nothing is active. Keep in mind this indexes the raw backing array of collections, whose ordering can be surprising. Roots come first, and a collection's siblings always sit back-to-back, but beyond those guarantees the order is arbitrary — so stepping this index up or down may send the active collection somewhere unexpected. When you want consistent behavior, reach for active or active_name instead. (in [-inf, inf], default 0)

Type :

int
active_name

Name of whichever bone collection is active on the Armature; this comes back as an empty string (and never as None) whenever nothing is active (default "", never None)

Type :

str
is_solo_active

A read-only boolean that is set whenever one or more bone collections currently carry the 'solo' flag (default False, readonly)

Type :

bool

[Related references](INDEX.md).
