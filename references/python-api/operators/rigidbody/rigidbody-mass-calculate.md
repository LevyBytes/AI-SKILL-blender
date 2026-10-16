# bpy.ops.rigidbody.mass_calculate

bpy.ops.rigidbody. mass_calculate ( * , material = 'DEFAULT' , density = 1.0 )

Derive mass from volume for every selected Rigid Body, estimating based on material type

Parameters :

- material ( Literal [ 'DEFAULT' ] ) – Material Preset, Material category governing how heavy the objects behave (optional)

- density ( float ) – Density, Mass per unit volume (kg/m^3), allows custom value if the 'Custom' preset is used (in [1.17549e-38, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
