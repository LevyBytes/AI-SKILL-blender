# bpy.ops.uv.sphere_project

bpy.ops.uv. sphere_project ( * , direction = '`VIEW_ON_EQUATOR`' , align = '`POLAR_ZX`' , pole = 'PINCH' , seam = False , correct_aspect = True , clip_to_bounds = False , scale_to_bounds = False ) 

Maps the mesh's UV vertices onto the curved outside of a sphere

Parameters :

- direction ( Literal [ '`VIEW_ON_EQUATOR`' , '`VIEW_ON_POLES`' , '`ALIGN_TO_OBJECT`' ] ) – Direction, Direction of the sphere or cylinder (optional)

- `VIEW_ON_EQUATOR`
View on Equator – The 3D viewpoint sits at the equator.

- `VIEW_ON_POLES`
View on Poles – The 3D viewpoint sits at the poles.

- `ALIGN_TO_OBJECT`
Align to Object – Follow the object's transform for alignment.

- align ( Literal [ '`POLAR_ZX`' , '`POLAR_ZY`' ] ) – Align, How to determine rotation around the pole (optional)

- `POLAR_ZX`
Polar ZX – Take X as polar 0.

- `POLAR_ZY`
Polar ZY – Take Y as polar 0.

- pole ( Literal [ 'PINCH' , 'FAN' ] ) – Pole, How to handle faces at the poles (optional)

- PINCH
Pinch – Squeeze the UVs together at the poles.

- FAN
Fan – Spread the UVs out at the poles.

- seam ( bool ) – Preserve Seams, Separate projections by islands isolated by seams (optional)

- correct_aspect ( bool ) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)

- clip_to_bounds ( bool ) – Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)

- scale_to_bounds ( bool ) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
