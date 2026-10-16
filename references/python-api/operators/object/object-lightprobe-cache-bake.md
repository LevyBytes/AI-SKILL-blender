# bpy.ops.object.lightprobe_cache_bake

bpy.ops.object. lightprobe_cache_bake ( * , subset = 'ALL' ) 

Compute and store illumination data in light probe volumes

Parameters :

subset ( Literal [ 'ALL' , 'SELECTED' , 'ACTIVE' ] ) – Subset, Which probes to process (optional)

- ALL
All Volumes – Process every light-sampling volume.

- SELECTED
Selected Only – Process only highlighted light-sampling volumes.

- ACTIVE
Active Only – Process only the topmost light-sampling volume.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
