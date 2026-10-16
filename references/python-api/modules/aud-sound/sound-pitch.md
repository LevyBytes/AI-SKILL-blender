# aud.Sound: pitch ( factor )

pitch ( factor ) 

Modifies the pitch of a sound by a scaling value.

Parameters :

factor ( float ) – Pitch scaling multiplier.

Returns :

The created Sound object.

Return type :

Sound

Note

This is done by changing the sample rate of the
underlying sound, which has to be an integer, so the factor
value rounded and the factor may not be 100 % accurate.

Note

This is a filter function, you might consider using
Handle.pitch instead.

[Related references](INDEX.md).
