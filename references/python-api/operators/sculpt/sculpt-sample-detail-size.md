# bpy.ops.sculpt.sample_detail_size

bpy.ops.sculpt. sample_detail_size ( * , location = (0, 0) , mode = 'DYNTOPO' )

Acquire the surface fineness at the target location

Parameters :

- location ( Sequence [ int ] ) – Location, Zone coordinates of sampling (array of 2 items, in [0, 32767], optional)

- mode ( Literal [ 'DYNTOPO' , 'VOXEL' ] ) – Detail Mode, Sculpting workflow context that will apply the sampled measurement (optional)

- DYNTOPO
Dyntopo – Sample dyntopo detail.

- VOXEL
Voxel – Sample mesh voxel size.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.sculpt. sample_detail_size ( * , location = (0, 0) , mode = 'DYNTOPO' )
Samples the mesh detail at the clicked point.
Parameters:
- location ( Sequence [ int ] ) – Location, Screen coordinates of sampling (array of 2 items, in [0, 32767], optional)
- mode ( Literal [ 'DYNTOPO' , 'VOXEL' ] ) – Detail Mode, Target sculpting workflow that is going to use the sampled size (optional)
- DYNTOPO - Dyntopo: sample dyntopo detail.
- VOXEL - Voxel: sample mesh voxel size.
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
