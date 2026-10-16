# bpy.types.CurveMapping: methods

update ( )

Apply the changes you've made to the curve mapping
reset_view ( )

Set the curve mapping grid back to match its clipping size
initialize ( )

Initialize curve
evaluate ( curve , position )

Evaluate curve at given location

Parameters :

- curve (CurveMap) – curve, Curve to evaluate (never None)

- position ( float ) – Position, Position to evaluate curve at (in [-inf, inf])

Returns :

Value, Value of curve at given location (in [-inf, inf])

Return type :

float
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
| Brush.automasking_cavity_curve Brush.curve_distance_falloff Brush.curve_jitter Brush.curve_random_hue Brush.curve_random_saturation Brush.curve_random_value Brush.curve_size Brush.curve_strength BrushCurvesSculptSettings.curve_parameter_falloff BrushGpencilSettings.curve_jitter BrushGpencilSettings.curve_random_hue BrushGpencilSettings.curve_random_pressure BrushGpencilSettings.curve_random_saturation BrushGpencilSettings.curve_random_strength BrushGpencilSettings.curve_random_uv BrushGpencilSettings.curve_random_value BrushGpencilSettings.curve_sensitivity BrushGpencilSettings.curve_strength ColorManagedViewSettings.curve_mapping CompositorNodeCurveRGB.mapping CompositorNodeHueCorrect.mapping CompositorNodeTime.curve CurvesModifier.curve_mapping EQCurveMappingData.curve_mapping GPencilInterpolateSettings.interpolation_curve GPencilSculptSettings.multiframe_falloff_curve GPencilSculptSettings.thickness_primitive_curve GreasePencilColorModifier.custom_curve GreasePencilHookModifier.custom_curve GreasePencilNoiseModifier.custom_curve GreasePencilOpacityModifier.custom_curve GreasePencilSmoothModifier.custom_curve GreasePencilThickModifierData.custom_curve GreasePencilTintModifier.custom_curve | HookModifier.falloff_curve HueCorrectModifier.curve_mapping LineStyleAlphaModifier_AlongStroke.curve LineStyleAlphaModifier_CreaseAngle.curve LineStyleAlphaModifier_Curvature_3D.curve LineStyleAlphaModifier_DistanceFromCamera.curve LineStyleAlphaModifier_DistanceFromObject.curve LineStyleAlphaModifier_Material.curve LineStyleAlphaModifier_Noise.curve LineStyleAlphaModifier_Tangent.curve LineStyleThicknessModifier_AlongStroke.curve LineStyleThicknessModifier_CreaseAngle.curve LineStyleThicknessModifier_Curvature_3D.curve LineStyleThicknessModifier_DistanceFromCamera.curve LineStyleThicknessModifier_DistanceFromObject.curve LineStyleThicknessModifier_Material.curve LineStyleThicknessModifier_Tangent.curve Paint.cavity_curve ParticleBrush.curve ParticleSettings.clump_curve ParticleSettings.roughness_curve ParticleSettings.twist_curve RenderSettings.motion_blur_shutter_curve Sculpt.automasking_cavity_curve Sculpt.automasking_cavity_curve_op ShaderNodeFloatCurve.mapping ShaderNodeRGBCurve.mapping ShaderNodeVectorCurve.mapping TextureNodeCurveRGB.mapping TextureNodeCurveTime.curve UvSculpt.curve_distance_falloff VertexWeightEditModifier.map_curve VertexWeightProximityModifier.map_curve WarpModifier.falloff_curve |

[Related references](INDEX.md).
