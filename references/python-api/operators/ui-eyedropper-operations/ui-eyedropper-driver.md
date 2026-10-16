# bpy.ops.ui.eyedropper_driver

bpy.ops.ui. eyedropper_driver ( * , mapping_type = '`SINGLE_MANY`' ) 

Chooses a property to serve as a driver target

Parameters :

mapping_type ( Literal [ '`SINGLE_MANY`' , 'DIRECT' , 'MATCH' , '`NONE_ALL`' , '`NONE_SINGLE`' ] ) – Mapping Type, Method used to match target and driven properties (optional)

- `SINGLE_MANY`
All from Target – Drive every component of this property from the single target chosen.

- DIRECT
Single from Target – Drive just this one component using the target chosen.

- MATCH
Match Indices – Set up a driver for each matched pair of elements.

- `NONE_ALL`
Manually Create Later – Set up drivers across all properties but leave the targets unset for now.

- `NONE_SINGLE`
Manually Create Later (Single) – Set up a driver for this property alone, with no target assigned yet.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
