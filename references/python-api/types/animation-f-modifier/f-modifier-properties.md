# bpy.types.FModifier: properties

active

Whether this F-Curve modifier exposes its settings in the editor (default False)

Type :

bool
blend_in

Count of frames measured from the start frame over which the influence ramps up (in [-inf, inf], default 0.0)

Type :

float
blend_out

Count of frames measured from the end frame over which the influence ramps down (in [-inf, inf], default 0.0)

Type :

float
frame_end

Frame at which the modifier stops having an effect, when Restrict Frame Range is active (in [-inf, inf], default 0.0)

Type :

float
frame_start

Frame at which the modifier begins having an effect, when Restrict Frame Range is active (in [-inf, inf], default 0.0)

Type :

float
influence

How strongly the F-Curve Modifier acts once it is past any fade in or out (in [0, 1], default 1.0)

Type :

float
is_valid

Set when the F-Curve Modifier's settings are invalid, so it is skipped during evaluation (default True, readonly)

Type :

bool
mute

Turn evaluation of the F-Curve modifier on (default False)

Type :

bool
name

Name given to the F-Curve Modifier (default “”, never None)

Type :

str
show_expanded

Whether the F-Curve Modifier's panel appears expanded in the UI (default False)

Type :

bool
type

Kind of F-Curve Modifier (default 'NULL' , readonly)

Type :

Literal[Fmodifier Type Items]
use_influence

When set, a default factor scales down what the F-Curve Modifier does (default False)

Type :

bool
use_restricted_range

Confine the F-Curve Modifier to the chosen frame range, which helps mask off its effect so several can be chained (default False)

Type :

bool

[Related references](INDEX.md).
