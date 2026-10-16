# bpy.ops.object.transform_apply

bpy.ops.object. transform_apply ( * , location = True , rotation = True , scale = True , properties = True , corrective_flip_normals = True , isolate_users = False ) 

Bake the item's movement, orientation, and sizing into its information

Parameters :

- location ( bool ) – Location, (optional)

- rotation ( bool ) – Rotation, (optional)

- scale ( bool ) – Scale, (optional)

- properties ( bool ) – Apply Properties, Revise attributes such as curve vertex thickness, character sizing and armature envelope (optional)

- corrective_flip_normals ( bool ) – Corrective Flip Normals, Reverse surface directions for items with negative sizing. (optional)

- isolate_users ( bool ) – Isolate Multi User Data, Produce fresh item-information holders if required (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
