# aud.Sound: lowpass ( frequency , Q = 0.5 )

lowpass ( frequency , Q = 0.5 ) 

Constructs a second order lowpass filter based on the transfer function \\(H(s) = 1 / (s^2 + s/Q + 1)\\)

Parameters :

- frequency ( float ) – Cutoff point for the lowpass effect.

- Q ( float ) – Q factor of the lowpass.

Returns :

The created Sound object.

Return type :

Sound

[Related references](INDEX.md).
