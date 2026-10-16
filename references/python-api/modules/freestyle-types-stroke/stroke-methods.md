# freestyle.types.Stroke: methods

compute_sampling ( n ) 

Works out the sampling required to end up with N vertices. Should the requested vertex count fall below the count already present, the existing sampling value is returned instead. (To take vertices away, call this class's RemoveVertex() method.)

Parameters :

n ( int ) – The number of stroke vertices we eventually want
in our Stroke.

Returns :

The sampling that must be used in the Resample(float)
method.

Return type :

float
insert_vertex ( vertex , next ) 

Places the StrokeVertex passed in into the Stroke just ahead of the point indicated by next. Length and curvilinear abscissa are refreshed accordingly.

Parameters :

- vertex (StrokeVertex) – The StrokeVertex to insert in the Stroke.

- next (StrokeVertexIterator) – A StrokeVertexIterator pointing to the StrokeVertex
before which vertex must be inserted.
remove_all_vertices ( ) 

Clears every vertex out of the Stroke.
remove_vertex ( vertex ) 

Takes the StrokeVertex passed in out of the Stroke. Length and curvilinear abscissa are refreshed accordingly.

Parameters :

vertex (StrokeVertex) – the StrokeVertex to remove from the Stroke.
resample ( n ) 

resample ( sampling )

Resamples the stroke through one of two routes, aiming to yield a stroke that keeps the same shape with fewer points.

Parameters :

- n ( int ) – Drives the stroke to wind up holding N points; concretely it tacks
on N minus vertices_size more, where vertices_size counts the points already
present. Whenever vertices_size is N or greater, nothing is resampled.

- sampling ( float ) – Resamples the stroke at the sampling value you supply.
Should that value undercut the current sampling value, the stroke is left as is.
stroke_vertices_begin ( t = 0.0 ) 

Hands back a StrokeVertexIterator sitting on the Stroke's first StrokeVertex. A sampling value may be passed to re-sample the Stroke on the fly when needed.

Parameters :

t ( float ) – The resampling value to apply to the Stroke. Supply 0 and no
resampling takes place.

Returns :

A StrokeVertexIterator pointing on the first StrokeVertex.

Return type :

StrokeVertexIterator
stroke_vertices_end ( ) 

Hands back a StrokeVertexIterator sitting just past the Stroke's last StrokeVertex.

Returns :

A StrokeVertexIterator pointing after the last StrokeVertex.

Return type :

StrokeVertexIterator
stroke_vertices_size ( ) 

Hands back how many StrokeVertex make up the Stroke.

Returns :

The number of stroke vertices.

Return type :

int
update_length ( ) 

Refreshes the Stroke's 2D length.

[Related references](INDEX.md).
