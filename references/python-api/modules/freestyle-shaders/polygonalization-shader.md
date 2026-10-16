# freestyle.shaders.PolygonalizationShader

class freestyle.shaders. PolygonalizationShader 

Class hierarchy: freestyle.types.StrokeShader > PolygonalizationShader

[Geometry shader]
__init__ ( error ) 

Builds a PolygonalizationShader object.

Parameters :

error ( float ) – How much error the polygonal approximation may carry against the original geometry; the smaller it is, the nearer the new stroke stays to the original. It is the maximum distance allowed between the new stroke and the old one.
shade ( stroke ) 

Reworks the Stroke geometry to give it a more "polygonal" look. The approach begins from the smallest possible stroke approximation — a single line from the first vertex to the last — then subdivides it using the original stroke vertices until a chosen error is met.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
