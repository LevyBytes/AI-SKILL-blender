# bpy.types.LayerCollection: properties

## LayerCollection(bpy_struct)

### LayerCollection(bpy_struct) 

base class — bpy_struct
class bpy.types. LayerCollection ( bpy_struct ) 

Layer collection
children 

Nested layer collections of this one (default None, readonly)

Type :

bpy_prop_collection[LayerCollection]
collection 

The Collection that this layer collection wraps (readonly, never None)

Type :

Collection
exclude 

Leave this out of the view layer (default False)

Type :

bool
hide_viewport 

Hide in the viewport for now (default False)

Type :

bool
holdout 

Hold out the collection's objects from the view layer (default False)

Type :

bool
indirect_only 

Let the collection's objects contribute only indirectly, via shadows and reflections, within the view layer (default False)

Type :

bool
is_visible 

Whether this collection shows for the view layer, with the parent collection taken into account (default False, readonly)

Type :

bool
name 

Name of this layer collection (same as its collection one) (default “”, readonly, never None)

Type :

str

[Related references](INDEX.md).
