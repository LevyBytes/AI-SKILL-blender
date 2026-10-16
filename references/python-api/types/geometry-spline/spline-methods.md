# bpy.types.Spline: methods

## Spline(bpy_struct)

### Spline(bpy_struct)

base class — bpy_struct
class bpy.types. Spline ( bpy_struct )

A single curve element: NURBS, Bézier, Polyline, or a character on text objects
calc_length ( * , resolution = 0 )

Compute the length of the spline

Parameters :

resolution ( int ) – Resolution, Spline resolution to be used, 0 defaults to the resolution_u (in [0, 1024], optional)

Returns :

Length, Length of the polygonaly approximated spline (in [0, inf])

Return type :

float
valid_message ( direction )

Return the message

Parameters :

direction ( int ) – Direction, The direction where 0-1 maps to U-V (in [0, 1])

Returns :

Return value, The message or an empty string when there is no error

Return type :

str
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – Identifier of the RNA type.

- default (bpy.types.Struct | None) – Value returned if nothing matches.

Returns :

Either the matching RNA type, or the default when there is no match.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – Identifier of the RNA type.

- default (type | None ) – Value returned if nothing matches.

Returns :

Either the matching class, or the default when there is no match.

Return type :

type
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Description | Description |
| --- | --- |
| Curve.splines CurveSplines.active | CurveSplines.new CurveSplines.remove |

[Related references](INDEX.md).
