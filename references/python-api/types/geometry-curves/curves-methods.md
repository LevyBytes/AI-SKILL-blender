# bpy.types.Curves: methods

## Curves(ID)

### Curves(ID)

base classes: bpy_struct, ID
class bpy.types. Curves ( ID )

A data-block for hair, built from hair curves.
add_curves ( sizes )

add_curves

Parameters :

sizes ( Sequence [ int ] ) – Sizes, The number of points in each curve (array of 1 items, in [0, inf])
remove_curves ( * , indices = (0,) )

Drop every curve, or — when indices are supplied — only the curves at those indices.

Parameters :

indices ( Sequence [ int ] ) – Indices, The indices of the curves to remove (array of 1 items, in [0, inf], optional)
resize_curves ( sizes , * , indices = (0,) )

Resize all the curves, or just those at the given indices. Shrinking a curve trims it, while growing one default-initializes the extra end values.

Parameters :

- sizes ( Sequence [ int ] ) – Sizes, The number of points in each curve (array of 1 items, in [1, inf])

- indices ( Sequence [ int ] ) – Indices, The indices of the curves to resize (array of 1 items, in [0, inf], optional)
reorder_curves ( new_indices )

Shuffle the curves into the order given by the new indices.

Parameters :

new_indices ( Sequence [ int ] ) – New indices, The new index for each of the curves (array of 1 items, in [0, inf])
set_types ( * , type = '`CATMULL_ROM`' , indices = (0,) )

Assign the curve type, applying it only to the curves at the given indices when those are provided.

Parameters :

- type (Literal[Curves Type Items]) – Type, (optional)

- indices ( Sequence [ int ] ) – Indices, The indices of the curves to resize (array of 1 items, in [0, inf], optional)
unit_test_compare ( * , curves = None , threshold = 7.1526e-06 )

unit_test_compare

Parameters :

- curves (Curves) – Curves to compare to (optional)

- threshold ( float ) – Threshold, Comparison tolerance threshold (in [0, inf], optional)

Returns :

Return value, String description of result of comparison (never None)

Return type :

str
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
