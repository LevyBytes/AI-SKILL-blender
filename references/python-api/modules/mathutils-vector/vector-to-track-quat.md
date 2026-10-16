# mathutils.Vector: to_track_quat ( track = 'Z' , up = 'Y' , / )

to_track_quat ( track = 'Z' , up = 'Y' , / ) 

Build a quaternion orientation from this vector together with the chosen track and up axes.

Parameters :

- track ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Track axis string.

- up ( Literal [ 'X' , 'Y' , 'Z' ] ) – Up axis string.

Returns :

the orientation derived from this vector together with the track and up axes.

Return type :

Quaternion

[Related references](INDEX.md).
