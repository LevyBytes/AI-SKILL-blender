# aud.Sound: envelope(attack, release, threshold, arthreshold)

envelope(attack, release, threshold, arthreshold)

Applies a volume envelope based on input amplitude.

Parameters:

- attack (float) – Attack time in seconds.

- release (float) – Release time in seconds.

- threshold (float) – Amplitude threshold for detection.

- arthreshold (float) – Threshold for amplitude ratio.

Returns:

The new Sound object.

Return type:

Sound
envelope(attack, release, threshold, arthreshold)

Applies a volume envelope determined by input amplitude.

Parameters:

- attack (float) – Attack duration in seconds.

- release (float) – Release duration in seconds.

- threshold (float) – Amplitude threshold for activation.

- arthreshold (float) – Threshold for amplitude ratio.

Returns:

The new Sound object.

Return type:

Sound

Postpones playback by inserting silence before the other sound source.

Parameters :

- attack ( float ) – Controls the onset intensity.

- release ( float ) – Controls the decay behavior.

- threshold ( float ) – The general threshold value.

- arthreshold ( float ) – The attack/release threshold value.

Returns :

The created Sound object.

Return type :

Sound

[Related references](INDEX.md).
