# freestyle.shaders.GuidingLinesShader

class freestyle.shaders. GuidingLinesShader 

Class hierarchy: freestyle.types.StrokeShader > GuidingLinesShader

[Geometry shader]
__init__ ( offset ) 

Builds a GuidingLinesShader object.

Parameters :

offset ( float ) – The replacement line starts out centered in the original stroke's bounding box; offset is how far that line gets shifted along its normal.
shade ( stroke ) 

A shader that reworks the Stroke geometry so it follows its main-direction line. Pair it with the splitting operator that uses the curvature criterion, since how accurate the approximation turns out depends on the size of the stroke's pieces — the larger the pieces, the coarser the result.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
