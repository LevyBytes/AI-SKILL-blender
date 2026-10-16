# bpy.types.XrActionMapItem: haptic_amplitude, haptic_duration, haptic_frequency, haptic_match_user_paths, haptic_mode, haptic_name

haptic_amplitude 

Strength of the haptic vibration, on a 0.0-to-1.0 scale (in [0, 1], default 0.0)

Type :

float
haptic_duration 

Length of the haptic pulse in seconds; 0.0 is the smallest supported value. (in [0, inf], default 0.0)

Type :

float
haptic_frequency 

Vibration frequency in hertz; 0.0 falls back to the OpenXR runtime's default. (in [0, inf], default 0.0)

Type :

float
haptic_match_user_paths 

Send haptics along the same user paths used by both the haptic action and this one (default False)

Type :

bool
haptic_mode 

When the haptics fire (default 'PRESS' )

- PRESS
Press – Apply haptics on button press.

- RELEASE
Release – Apply haptics on button release.

- `PRESS_RELEASE`
Press Release – Apply haptics on button press and release.

- REPEAT
Repeat – Apply haptics repeatedly for the duration of the button press.

Type :

Literal[‘PRESS’, ‘RELEASE’, ‘`PRESS_RELEASE`’, ‘REPEAT’]
haptic_name 

Which haptic action runs when this action fires (default “”, never None)

Type :

str

[Related references](INDEX.md).
