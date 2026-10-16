# bpy.types.bpy_struct: keyframe_delete ( data_path , * , index = -1 , frame = bpy.context.scene.frame_current , group = '' )

keyframe_delete ( data_path , * , index = -1 , frame = bpy.context.scene.frame_current , group = '' )

Strips a keyframe off this property's fcurve.

Parameters :

- data_path ( str ) – path to the property to remove a key, analogous to the fcurve's data path.

- index ( int ) – array index of the property to remove a key. Defaults to -1 removing all indices or a single channel if the property is not an array.

- frame ( float ) – The frame on which the keyframe is deleted, defaulting to the current frame.

- group ( str ) – The name of the group the F-Curve should be added to if it doesn't exist yet.

Returns :

Success of keyframe deletion.

Return type :

bool

[Related references](INDEX.md).
