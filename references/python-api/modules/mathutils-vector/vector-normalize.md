# mathutils.Vector: normalize ( )

normalize ( ) 

Rescale the vector in place so its length becomes exactly 1.0.

Warning

A vector that is all zeros stays unchanged when normalized.

Note

On 4D vectors only x, y and z get scaled; w stays as-is,
so the resulting 4D vector might not end up with unit length.

[Related references](INDEX.md).
