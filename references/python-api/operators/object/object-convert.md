# bpy.ops.object.convert

bpy.ops.object. convert ( * , target = 'MESH' , keep_original = False , merge_customdata = True , thickness = 5 , faces = True , offset = 0.01 ) 

Reclassify chose entities into an alternative representation

Parameters :

- target ( Literal [ 'CURVE' , 'MESH' , 'POINTCLOUD' , 'CURVES' , 'GREASEPENCIL' ] ) – Target, Type of object to convert to (optional)

- CURVE
Curve – Curve from Mesh or Text objects.

- MESH
Mesh – Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects.

- POINTCLOUD
Point Cloud – Point Cloud from Mesh objects.

- CURVES
Curves – Curves from evaluated curve data.

- GREASEPENCIL
Grease Pencil – Grease Pencil from Curve or Mesh objects.

- keep_original ( bool ) – Keep Original, Keep original objects instead of replacing them (optional)

- merge_customdata ( bool ) – Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers (optional)

- thickness ( int ) – Thickness, (in [1, 100], optional)

- faces ( bool ) – Export Faces, Export faces as filled strokes (optional)

- offset ( float ) – Stroke Offset, Offset strokes from fill (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
