# bpy.types.Object: convert_space

convert_space ( * , pose_bone = None , matrix = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)) , from_space = 'WORLD' , to_space = 'WORLD' ) 

Transform the supplied matrix from one coordinate space into another

Parameters :

- pose_bone (PoseBone) – Bone to use to define spaces (may be None, in which case only the two ‘WORLD’ and ‘LOCAL’ spaces are usable) (optional)

- matrix (mathutils.Matrix) – The matrix to transform (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)

- from_space ( Literal [ 'WORLD' , 'POSE' , '`LOCAL_WITH_PARENT`' , 'LOCAL' ] ) – The space in which ‘matrix’ is currently (optional)

[Related references](INDEX.md).
