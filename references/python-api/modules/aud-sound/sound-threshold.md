# aud.Sound: threshold ( threshold = 0 )

threshold ( threshold = 0 ) 

Converts an audio wave into a square wave by assigning samples with amplitude >= threshold to 1, samples with amplitude <= -threshold to -1, and all intermediate samples to 0.

Parameters :

threshold ( float ) – Amplitude limit for binary conversion.

Returns :

The created Sound object.

Return type :

Sound

[Related references](INDEX.md).
