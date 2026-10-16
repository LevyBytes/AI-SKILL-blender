# bpy.types.XrActionMapBindings: methods

## XrActionMapBindings(bpy_prop_collection)

### XrActionMapBindings(bpy_prop_collection) 

base classes — bpy_prop, bpy_prop_collection
class bpy.types. XrActionMapBindings ( bpy_prop_collection ) 

A grouping of XR action map bindings
new ( name , replace_existing ) 

new

Parameters :

- name ( str ) – Name of the action map binding, (never None)

- replace_existing ( bool ) – Replace Existing, Swap out any binding that already carries this name

Returns :

Binding, Added action map binding

Return type :

XrActionMapBinding
new_from_binding ( binding ) 

new_from_binding

Parameters :

binding (XrActionMapBinding) – Binding, A binding to copy as a template (never None)

Returns :

Binding, Added action map binding

Return type :

XrActionMapBinding
remove ( binding ) 

remove

Parameters :

binding (XrActionMapBinding) – Binding, (never None)
find ( name ) 

find

Parameters :

name ( str ) – Name, (never None)

Returns :

Binding, The action map binding with the given name

Return type :

XrActionMapBinding
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
