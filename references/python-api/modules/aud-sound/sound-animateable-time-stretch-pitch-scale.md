# aud.Sound: animateableTimeStretchPitchScale(fps , time_stretch, pitch_scale, quality, preserve_formant)

animateableTimeStretchPitchScale(fps [, time_stretch, pitch_scale, quality, preserve_formant])

Applies time-stretching and pitch-scaling to sound.

Parameters:

- fps (float) – The animation frame rate.

- time_stretch (float or AnimateableProperty) – Time compression/expansion factor.

- pitch_scale (float or AnimateableProperty) – Pitch adjustment factor.

- quality (Rubberband stretcher quality (`STRETCHER_QUALITY`_*).) – Processing quality.

- preserve_formant (bool) – Whether vocal properties persist during pitch-shifting.

Returns:

The new Sound object.

Return type:

Sound
animateableTimeStretchPitchScale(fps [, time_stretch, pitch_scale, quality, preserve_formant])

Applies time-stretching and pitch-scaling to sound.

Parameters:

- fps (float) – The animation frame rate.

- time_stretch (float or AnimateableProperty) – Time compression/expansion magnitude.

- pitch_scale (float or AnimateableProperty) – Pitch adjustment magnitude.

- quality (Rubberband stretcher quality (`STRETCHER_QUALITY`_*).) – Processing grade.

- preserve_formant (bool) – Whether vocal formants endure pitch-shifting.

Returns:

The new Sound object.

Return type:

Sound

[Related references](INDEX.md).
