# aud.Sound: filter ( b , a = (1,) )

filter ( b , a = (1,) ) 

Processes a sound using supplied IIR filter coefficients.
Without the second parameter you get a FIR filter instead.

If the initial value in the a sequence equals 0,
it will be set to 1 automatically.
If the first value in the a sequence is neither 0 nor 1, all
filter coefficients scale proportionally so the value becomes 1
at the end, eliminating the need for manual scaling.

Parameters :

- b ( sequence of float ) – The nominator filter coefficients.

- a ( sequence of float ) – The denominator filter coefficients.

Returns :

The created Sound object.

Return type :

Sound

[Related references](INDEX.md).
