# aud.Sound: cache()

cache()

Buffers sound into RAM.

Reduces decoding and file I/O overhead if the source reads from disk, but uses substantial memory.

Returns:

The new Sound object.

Return type:

Sound

Note

Only fixed-length sounds can be cached.

Warning

Uncompressed PCM requires significant space; cache only short sounds.
cache()

Stores sound in RAM.

Minimizes decoding and file overhead when reading from disk, but demands large memory.

Returns:

The new Sound object.

Return type:

Sound

Note

Only fixed-length sounds can be cached.

Warning

Uncompressed PCM consumes significant space; buffer only short sounds.

[Related references](INDEX.md).
