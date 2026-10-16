# bpy.ops.import_anim.bvh

bpy.ops.import_anim. bvh ( * , filepath = '' , filter_glob = '*.bvh' , target = 'ARMATURE' , global_scale = 1.0 , frame_start = 1 , use_fps_scale = False , update_scene_fps = False , update_scene_duration = False , use_cyclic = False , rotate_mode = 'NATIVE' , axis_forward = '-Z' , axis_up = 'Y' )

Load a BVH motion capture file

Parameters :

- filepath ( str ) – File Path, Filepath used for importing the file (optional, never None)

- filter_glob ( str ) – filter_glob, (optional, never None)

- target ( Literal [ 'ARMATURE' , 'OBJECT' ] ) – Target, What to import the capture onto (optional)

- global_scale ( float ) – Scale, Multiply the BVH by this scale (in [0.0001, 1e+06], optional)

- frame_start ( int ) – Start Frame, Frame where the animation begins (in [-inf, inf], optional)

- use_fps_scale ( bool ) – Scale FPS, Convert the BVH frame-rate to the current scene's; otherwise each BVH frame maps straight to one Blender frame (optional)

- update_scene_fps ( bool ) – Update Scene FPS, Switch the scene frame-rate to the BVH file's (this makes 'Scale FPS' a no-op, since the scale becomes 1:1) (optional)

- update_scene_duration ( bool ) – Update Scene Duration, Stretch the scene's length out to the BVH duration (it is never shortened) (optional)

- use_cyclic ( bool ) – Loop, Play the animation on a loop (optional)

- rotate_mode ( Literal [ 'QUATERNION' , 'NATIVE' , 'XYZ' , 'XZY' , 'YXZ' , 'YZX' , 'ZXY' , 'ZYX' ] ) – Rotation, How rotations are converted (optional)

- QUATERNION
Quaternion – Turn rotations into quaternions.

- NATIVE
Euler (Native) – Keep the rotation order from the BVH file.

- XYZ
Euler (XYZ) – Turn rotations into euler XYZ.

- XZY
Euler (XZY) – Turn rotations into euler XZY.

- YXZ
Euler (YXZ) – Turn rotations into euler YXZ.

- YZX
Euler (YZX) – Turn rotations into euler YZX.

- ZXY
Euler (ZXY) – Turn rotations into euler ZXY.

- ZYX
Euler (ZYX) – Turn rotations into euler ZYX.

- axis_forward ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Forward, (optional)

- axis_up ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Up, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
