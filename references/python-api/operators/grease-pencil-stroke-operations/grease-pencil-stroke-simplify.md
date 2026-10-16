# bpy.ops.grease_pencil.stroke_simplify

bpy.ops.grease_pencil.stroke_simplify ( * , factor = 0.01 , length = 0.05 , distance = 0.01 , steps = 1 , mode = 'FIXED' )
Reduce the number of points in highlighted strokes

Parameters:
- factor ( float ) – Factor, (in [0, 100], optional)
- length ( float ) – Length, (in [0, 100], optional)
- distance ( float ) – Distance, (in [0, 100], optional)
- steps ( int ) – Steps, (in [0, 50], optional)
- mode ( Literal [ 'FIXED' , 'ADAPTIVE' , 'SAMPLE' , 'MERGE' ] ) – Mode, Algorithm for point reduction (optional)
- FIXED: Discard alternating points while preserving extremes
- ADAPTIVE: Apply Ramer-Douglas-Peucker to smooth while keeping shape features
- SAMPLE: Re-tessellate with segments of the specified gap
- MERGE: Consolidate points closer than a given threshold

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
