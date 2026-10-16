# bpy.types.AnimDataDrivers: methods

## AnimDataDrivers(bpy_prop_collection)

Stores F-Curves that drive animation values.

base classes — bpy_prop, bpy_prop_collection
class bpy.types. AnimDataDrivers ( bpy_prop_collection )

Mechanism for storing driven animation curves.
new ( data_path , * , index = 0 )

Create a new driven F-Curve.

Parameters :

- data_path ( str ) – Data Path, F-Curve data path to use (never None)

- index ( int ) – Index, Array index (in [0, inf], optional)

Returns :

Newly Driver F-Curve

Return type :

FCurve
remove ( driver )

Delete a driven curve.

Parameters :

driver (FCurve) – (never None)
from_existing ( * , src_driver = None )

Create a new driven curve based on an existing one.

Parameters :

src_driver (FCurve) – Existing Driver F-Curve to use as template for a new one (optional)

Returns :

New Driver F-Curve

Return type :

FCurve
find ( data_path , * , index = 0 )

Locate a driven F-Curve via linear search across all driver curves.

Parameters :

- data_path ( str ) – Data Path, F-Curve data path (never None)

- index ( int ) – Index, Array index (in [0, inf], optional)

Returns :

The found F-Curve, or None if it doesn't exist

Return type :

FCurve
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
