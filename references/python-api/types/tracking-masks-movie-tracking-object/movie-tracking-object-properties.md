# bpy.types.MovieTrackingObject: properties

## MovieTrackingObject(bpy_struct)

### MovieTrackingObject(bpy_struct)

base class — bpy_struct
class bpy.types. MovieTrackingObject ( bpy_struct )

Tracking and reconstruction data for a match-moved object
is_camera

Whether the object serves as the camera-tracking object (default False, readonly)

Type :

bool
keyframe_a

First keyframe seeding the reconstruction (in [-inf, inf], default 0)

Type :

int
keyframe_b

Second keyframe seeding the reconstruction (in [-inf, inf], default 0)

Type :

int
name

Object's unique name (default “”, never None)

Type :

str
plane_tracks

Set of plane tracks belonging to this tracking data (default None, readonly)

Type :

MovieTrackingObjectPlaneTracks[MovieTrackingPlaneTrack]
reconstruction

(readonly)

Type :

MovieTrackingReconstruction
scale

Object-solution scale within camera space (in [0.0001, 10000], default 1.0)

Type :

float
tracks

Set of tracks belonging to this tracking data (default None, readonly)

Type :

MovieTrackingObjectTracks[MovieTrackingTrack]

[Related references](INDEX.md).
