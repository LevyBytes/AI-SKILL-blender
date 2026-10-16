# bpy.types.Camera: view_frame

view_frame ( * , scene = None )

Get 4 corner points of the camera frame (pre-transformation)

Parameters :

scene (Scene) – Scene to use for aspect calculation, when omitted 1:1 aspect is used (optional)

Returns :

result_1 , Result, mathutils.Vector

result_2 , Result, mathutils.Vector

result_3 , Result, mathutils.Vector

result_4 , Result, mathutils.Vector

Return type :

tuple[mathutils.Vector, mathutils.Vector, mathutils.Vector, mathutils.Vector]

[Related references](INDEX.md).
