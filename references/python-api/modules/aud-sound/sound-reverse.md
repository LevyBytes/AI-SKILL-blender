# aud.Sound: reverse ( )

reverse ( ) 

Plays a sound in reverse order.

Returns :

The created Sound object.

Return type :

Sound

Note

The sound has to have a finite length and has to be seekable.
It's recommended to use this only with factories with
fast and accurate seeking, which is not true for encoded audio
files, such ones should be buffered using cache() before
being played reversed.

Warning

If seeking is not accurate in the underlying sound
you'll likely hear skips/jumps/cracks.

[Related references](INDEX.md).
