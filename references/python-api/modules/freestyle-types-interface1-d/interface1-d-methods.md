# freestyle.types.Interface1D: methods

__init__ ( ) 

Default constructor.
points_begin ( t = 0.0 ) 

Hands back an iterator over the Interface1D points that starts on the first point. Unlike vertices_begin(), this lets you step through the 1D element's points at whatever sampling you choose, since a virtual point is spawned on every iteration.

Parameters :

t ( float ) – The sampling rate to use when stepping across this 1D
element's points.

Returns :

An Interface0DIterator pointing to the first point.

Return type :

Interface0DIterator
points_end ( t = 0.0 ) 

Hands back an iterator over the Interface1D points that sits just past the last point. Unlike vertices_end(), this lets you step through the 1D element's points at whatever sampling you choose, since a virtual point is spawned on every iteration.

Parameters :

t ( float ) – The sampling rate to use when stepping across this 1D
element's points.

Returns :

An Interface0DIterator pointing after the last point.

Return type :

Interface0DIterator
vertices_begin ( ) 

Hands back an iterator over the Interface1D vertices that starts on the first vertex.

Returns :

An Interface0DIterator pointing to the first vertex.

Return type :

Interface0DIterator
vertices_end ( ) 

Hands back an iterator over the Interface1D vertices that sits just past the last vertex.

Returns :

An Interface0DIterator pointing after the last vertex.

Return type :

Interface0DIterator

[Related references](INDEX.md).
