# bpy.types.Modifier: methods

## Modifier(bpy_struct)

### Modifier(bpy_struct)

base class — bpy_struct

subclasses —
ArmatureModifier, ArrayModifier, BevelModifier, BooleanModifier, BuildModifier, CastModifier, ClothModifier, CollisionModifier, CorrectiveSmoothModifier, CurveModifier, DataTransferModifier, DecimateModifier, DisplaceModifier, DynamicPaintModifier, EdgeSplitModifier, ExplodeModifier, FluidModifier, GreasePencilArmatureModifier, GreasePencilArrayModifier, GreasePencilBuildModifier, GreasePencilColorModifier, GreasePencilDashModifierData, GreasePencilEnvelopeModifier, GreasePencilHookModifier, GreasePencilLatticeModifier, GreasePencilLengthModifier, GreasePencilLineartModifier, GreasePencilMirrorModifier, GreasePencilMultiplyModifier, GreasePencilNoiseModifier, GreasePencilOffsetModifier, GreasePencilOpacityModifier, GreasePencilOutlineModifier, GreasePencilShrinkwrapModifier, GreasePencilSimplifyModifier, GreasePencilSmoothModifier, GreasePencilSubdivModifier, GreasePencilTextureModifier, GreasePencilThickModifierData, GreasePencilTimeModifier, GreasePencilTintModifier, GreasePencilWeightAngleModifier, GreasePencilWeightProximityModifier, HookModifier, LaplacianDeformModifier, LaplacianSmoothModifier, LatticeModifier, MaskModifier, MeshCacheModifier, MeshDeformModifier, MeshSequenceCacheModifier, MeshToVolumeModifier, MirrorModifier, MultiresModifier, NodesModifier, NormalEditModifier, OceanModifier, ParticleInstanceModifier, ParticleSystemModifier, RemeshModifier, ScrewModifier, ShrinkwrapModifier, SimpleDeformModifier, SkinModifier, SmoothModifier, SoftBodyModifier, SolidifyModifier, SubsurfModifier, SurfaceDeformModifier, SurfaceModifier, TriangulateModifier, UVProjectModifier, UVWarpModifier, VertexWeightEditModifier, VertexWeightMixModifier, VertexWeightProximityModifier, VolumeDisplaceModifier, VolumeToMeshModifier, WarpModifier, WaveModifier, WeightedNormalModifier, WeldModifier, WireframeModifier
class bpy.types. Modifier ( bpy_struct )

Base type for anything that operates on an object's geometry data
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

- default (type | None ) – The value to return when not found.

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
| Object.modifiers ObjectModifiers.active | ObjectModifiers.new ObjectModifiers.remove |

[Related references](INDEX.md).
