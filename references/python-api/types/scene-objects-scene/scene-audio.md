# bpy.types.Scene: audio_distance_model, audio_doppler_factor, audio_doppler_speed, audio_volume

audio_distance_model

Distance model used when computing distance attenuation (default '`INVERSE_CLAMPED`' )

- NONE
None – No distance attenuation.

- INVERSE
Inverse – Inverse distance model.

- `INVERSE_CLAMPED`
Inverse Clamped – Inverse distance model with clamping.

- LINEAR
Linear – Linear distance model.

- `LINEAR_CLAMPED`
Linear Clamped – Linear distance model with clamping.

- EXPONENT
Exponential – Exponential distance model.

- `EXPONENT_CLAMPED`
Exponential Clamped – Exponential distance model with clamping.

Type :

Literal[‘NONE’, ‘INVERSE’, ‘`INVERSE_CLAMPED`’, ‘LINEAR’, ‘`LINEAR_CLAMPED`’, ‘EXPONENT’, ‘`EXPONENT_CLAMPED`’]
audio_doppler_factor

Pitch factor used when computing the Doppler effect (in [0, inf], default 1.0)

Type :

float
audio_doppler_speed

Speed of sound used when computing the Doppler effect (in [0.01, inf], default 343.3)

Type :

float
audio_volume

Audio volume (in [0, 100], default 1.0)

Type :

float

[Related references](INDEX.md).
