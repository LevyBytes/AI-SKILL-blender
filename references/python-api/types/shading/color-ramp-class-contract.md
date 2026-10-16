# bpy.types.ColorRamp — class-contract, Inherited Properties, Inherited Functions, References, ColorRamp(bpy_struct)

color_mode

Choose which color mode the interpolation runs in (default 'RGB' )

Type :

Literal[‘RGB’, ‘HSV’, ‘HSL’]
elements

(default None, readonly)

Type :

ColorRampElements[ColorRampElement]
hue_interpolation

Choose how the color is interpolated (default 'NEAR' )

Type :

Literal[‘NEAR’, ‘FAR’, ‘CW’, ‘CCW’]
interpolation

Choose how colors are interpolated between the stops (default 'LINEAR' )

Type :

Literal[‘EASE’, ‘CARDINAL’, ‘LINEAR’, ‘`B_SPLINE`’, ‘CONSTANT’]
evaluate ( position )

Sample the Color Ramp at the given position

Parameters :

position ( float ) – Position, Where along the ramp to sample (in [0, 1])

Returns :

Color, The color found at that position (array of 4 items, in [-inf, inf])

Return type :

bpy_prop_array[float]
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
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Description | Description |
| --- | --- |
| Brush.gradient ColorMapping.color_ramp DynamicPaintBrushSettings.paint_ramp DynamicPaintBrushSettings.velocity_ramp FluidDomainSettings.color_ramp GreasePencilTintModifier.color_ramp LineStyleColorModifier_AlongStroke.color_ramp LineStyleColorModifier_CreaseAngle.color_ramp LineStyleColorModifier_Curvature_3D.color_ramp | LineStyleColorModifier_DistanceFromCamera.color_ramp LineStyleColorModifier_DistanceFromObject.color_ramp LineStyleColorModifier_Material.color_ramp LineStyleColorModifier_Noise.color_ramp LineStyleColorModifier_Tangent.color_ramp PreferencesView.weight_color_range ShaderNodeValToRGB.color_ramp Texture.color_ramp TextureNodeValToRGB.color_ramp |
## ColorRamp(bpy_struct)

[Related references](INDEX.md).
