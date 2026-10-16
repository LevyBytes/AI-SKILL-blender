# aud.HRTF

class aud.HRTF

An HRTF set represents head-related transfer function impulse responses for binaural audio.
loadLeftHrtfSet(extension, directory)

Loads HRTF data from a directory.

Parameters:

- extension (string) – File type of the HRTF files.

- directory – Path containing the HRTF files.

Returns:

The loaded HRTF object.

Return type:

HRTF
loadRightHrtfSet(extension, directory)

Loads HRTF data from a directory.

Parameters:

- extension (string) – File type of the HRTF files.

- directory – Path containing the HRTF files.

Returns:

The loaded HRTF object.

Return type:

HRTF
addImpulseResponseFromSound(sound, azimuth, elevation)

Adds an HRTF impulse response to the HRTF object.

Parameters:

- sound (Sound) – The audio file holding the HRTF.

- azimuth (float) – The azimuth angle of the HRTF.

- elevation (float) – The elevation angle of the HRTF.

Returns:

Success status.

Return type:

bool

[Related references](INDEX.md).
