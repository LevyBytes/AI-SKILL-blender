# bpy.ops.object.lightprobe_cache_free

bpy.ops.object. lightprobe_cache_free ( * , subset = 'SELECTED' ) 

Discard stored indirect brightness information

Parameters :

subset ( Literal [ 'ALL' , 'SELECTED' , 'ACTIVE' ] ) – Subset, Which probes to process (optional)

- ALL
All Light Probes – Erase stored brightness from all probes.

- SELECTED
Selected Only – Erase stored brightness from highlighted probes.

- ACTIVE
Active Only – Erase stored brightness from the topmost probe.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
