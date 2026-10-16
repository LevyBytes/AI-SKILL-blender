# bpy.types.Speaker: properties

animation_data

This data-block's animation data (readonly)

Type :

AnimData
attenuation

Strength with which distance affects volume, according to the distance model (in [0, inf], default 1.0)

Type :

float
cone_angle_inner

Inner cone angle in degrees; volume stays at 100% within this cone (in [0, 360], default 360.0)

Type :

float
cone_angle_outer

Outer cone angle in degrees; past it the volume drops to the outer cone volume, and it is interpolated between the inner and outer cones (in [0, 360], default 360.0)

Type :

float
cone_volume_outer

Volume beyond the outer cone (in [0, 1], default 1.0)

Type :

float
distance_max

Farthest distance considered for volume, regardless of how distant the object becomes (in [0, inf], default 3.40282e+38)

Type :

float
distance_reference

Distance of reference where volume reaches 100% (in [0, inf], default 1.0)

Type :

float
muted

Silence the speaker (default False)

Type :

bool
pitch

Pitch the sound plays back at (in [0.1, 10], default 1.0)

Type :

float
sound

The sound data-block the speaker uses

Type :

Sound
volume

Loudness of the sound (in [0, 1], default 1.0)

Type :

float
volume_max

Highest volume, regardless of how near the object gets (in [0, 1], default 1.0)

Type :

float
volume_min

Lowest volume, regardless of how distant the object gets (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).
