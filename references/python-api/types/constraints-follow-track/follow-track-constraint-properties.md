# bpy.types.FollowTrackConstraint: properties

## FollowTrackConstraint(Constraint)

### FollowTrackConstraint(Constraint)

base classes: bpy_struct, Constraint
class bpy.types. FollowTrackConstraint ( Constraint )

Pins an object's motion to follow the target motion track.
camera

Camera the motion is parented to; when left empty the active scene camera is used instead

Type :
Object
clip

Movie Clip that supplies the tracking data

Type :

MovieClip
depth_object

Object whose surface is projected onto to establish depth within camera space

Type :

Object
frame_method

The way the footage is fitted inside the camera frame (default 'STRETCH' )

Type :

Literal[‘STRETCH’, ‘FIT’, ‘CROP’]

object

Movie tracking object to follow (if empty, camera object is used) (default “”, never None)

Type :

str
track

Movie tracking track to follow (default “”, never None)

Type :

str
use_3d_position

Use 3D position of track to parent to (default False)

Type :

bool
use_active_clip

Use active clip defined in scene (default False)

Type :

bool
use_undistorted_position

Parent to undistorted position of 2D track (default False)

Type :

bool

[Related references](INDEX.md).
