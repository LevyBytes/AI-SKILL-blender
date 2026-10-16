# aud.Sound: highpass ( frequency , Q = 0.5 )

highpass ( frequency , Q = 0.5 ) 

Constructs a second order highpass filter based on the transfer
function \\(H(s) = s^2 / (s^2 + s/Q + 1)\\)

Parameters :

- frequency ( float ) – Cutoff point for the highpass effect.

- Q ( float ) – Q factor of the lowpass.

Returns :

The created Sound object.

Return type :

Sound

[Related references](INDEX.md).
