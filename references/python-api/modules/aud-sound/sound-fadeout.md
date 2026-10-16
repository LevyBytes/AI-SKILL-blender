# aud.Sound: fadeout ( start , length )

fadeout ( start , length ) 

Gradually decreases the volume of a sound over a specified duration.

Parameters :

- start ( float ) – Timestamp where fading begins (in seconds).

- length ( float ) – Duration of the fade effect (in seconds).

Returns :

The created Sound object.

Return type :

Sound

Note

After the fade this sound plays silence, so that
the length of the sound is not altered.

[Related references](INDEX.md).
