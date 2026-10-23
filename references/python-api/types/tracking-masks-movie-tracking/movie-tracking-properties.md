# bpy.types.MovieTracking: properties

## MovieTracking(bpy_struct)

### MovieTracking(bpy_struct)

base class: bpy_struct
class bpy.types. MovieTracking ( bpy_struct )

Container for match-moving tracking data
active_object_index

Position of the active object in the list (in [-inf, inf], default 0)

Type :

int
camera

(readonly)

Type :

MovieTrackingCamera
dopesheet

(readonly)

Type :

MovieTrackingDopesheet
objects

Set of objects belonging to this tracking data (default None, readonly)

Type :

MovieTrackingObjects[MovieTrackingObject]
plane_tracks

Set of plane tracks belonging to this tracking data. Deprecated, use objects[name].plane_tracks (default None, readonly)

Type :

MovieTrackingPlaneTracks[MovieTrackingPlaneTrack]
reconstruction

(readonly)

Type :

MovieTrackingReconstruction
settings

(readonly)

Type :

MovieTrackingSettings
stabilization

(readonly)

Type :

MovieTrackingStabilization
tracks

Set of tracks belonging to this tracking data. Deprecated, use objects[name].tracks (default None, readonly)

Type :

MovieTrackingTracks[MovieTrackingTrack]

[Related references](INDEX.md).
