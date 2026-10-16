# aud.Sound: ADSR(attack, decay, sustain, release)

ADSR(attack, decay, sustain, release)

Applies Attack-Decay-Sustain-Release volume envelope to a sound.

Note: release triggering is not currently implemented in this API.

Parameters:

- attack (float) – Attack time in seconds.

- decay (float) – Decay time in seconds.

- sustain (float) – Sustain level.

- release (float) – Release level.

Returns:

The new Sound object.

Return type:

Sound
ADSR(attack, decay, sustain, release)

Applies Attack-Decay-Sustain-Release volume contouring to sound. Note: release activation is not available in the current API.

Parameters:

- attack (float) – Attack duration in seconds.

- decay (float) – Decay duration in seconds.

- sustain (float) – Sustain level.

- release (float) – Release level.

Returns:

The new Sound object.

Return type:

Sound

[Related references](INDEX.md).
