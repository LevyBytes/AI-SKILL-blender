# bpy.types.FCurveKeyframePoints: methods

insert ( frame , value , * , options = set() , keyframe_type = 'KEYFRAME' )

Add a keyframe point to a F-Curve

Parameters :

- frame ( float ) – X Value of this keyframe point (in [-inf, inf])

- value ( float ) – Y Value of this keyframe point (in [-inf, inf])

- options ( set [ Literal [ 'REPLACE' , 'NEEDED' , 'FAST' ] ] ) – Keyframe options (optional)

- REPLACE
Replace – Create no fresh keyframes; only overwrite ones already present.

- NEEDED
Needed – Insert a keyframe only where one is actually required.

- FAST
Fast – Insert keyframes quickly by skipping a curve recalculation on each insert.

- keyframe_type (Literal[Beztriple Keyframe Type Items]) – Type of keyframe to insert (optional)

Returns :

Newly created keyframe

Return type :

Keyframe
add ( count )

Add a keyframe point to a F-Curve

Parameters :

count ( int ) – Number, Number of points to add to the spline (in [0, inf])
remove ( keyframe , * , fast = False )

Remove keyframe from an F-Curve

Parameters :

- keyframe (Keyframe) – Keyframe to remove (never None)

- fast ( bool ) – Fast, Remove keyframes quickly by skipping a curve recalculation each time (optional)
clear ( )

Remove all keyframes from an F-Curve
sort ( )

Ensure all keyframe points are chronologically sorted
deduplicate ( )

Drop any duplicate keys, on the assumption the points are already sorted
handles_recalc ( )

Refresh handles after the keyframe points change, so things like auto-clamping stay correct
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
