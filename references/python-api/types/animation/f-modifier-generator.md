# bpy.types.FModifierGenerator

coefficients

The ‘x’ coefficients, ordered from the lowest power x^0 upward (array of 32 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
mode

Type of generator to use (default 'POLYNOMIAL' )

Type :

Literal[‘POLYNOMIAL’, ‘`POLYNOMIAL_FACTORISED`’]
poly_order

The highest power of ‘x’ for this polynomial (number of coefficients - 1) (in [1, 100], default 0)

Type :

int
use_additive

Adds this modifier's output onto the existing values rather than replacing them (default False)

Type :

bool
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
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data FModifier.name FModifier.type FModifier.show_expanded FModifier.mute FModifier.is_valid FModifier.active | FModifier.use_restricted_range FModifier.frame_start FModifier.frame_end FModifier.blend_in FModifier.blend_out FModifier.use_influence FModifier.influence |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values FModifier.bl_rna_get_subclass FModifier.bl_rna_get_subclass_py |
## FModifierGenerator(FModifier)

### FModifierGenerator(FModifier)

base classes: bpy_struct, FModifier
class bpy.types. FModifierGenerator ( FModifier )

Computes deterministic values for the F-Curve it modifies.

[Related references](INDEX.md).
