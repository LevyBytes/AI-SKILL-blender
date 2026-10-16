# aud.Sound: timeStretchPitchScale ( time_stretch , pitch_scale , quality , preserve_formant )

timeStretchPitchScale ( time_stretch , pitch_scale , quality , preserve_formant ) 

Performs simultaneous time-stretching and pitch adjustment on the sound.

Parameters :

- time_stretch ( float ) – Duration scaling factor.

- pitch_scale ( float ) – Pitch adjustment multiplier.

- quality ( int ) – Rubberband stretcher quality (`STRETCHER_QUALITY`_*).

- preserve_formant ( bool ) – Whether to preserve the vocal formants during pitch-shifting.

Returns :

The created Sound object.

Return type :

Sound

[Related references](INDEX.md).
