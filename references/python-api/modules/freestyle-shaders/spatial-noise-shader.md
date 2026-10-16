# freestyle.shaders.SpatialNoiseShader

class freestyle.shaders. SpatialNoiseShader 

Class hierarchy: freestyle.types.StrokeShader > SpatialNoiseShader

[Geometry shader]
__init__ ( amount , scale , num_octaves , smooth , pure_random ) 

Builds a SpatialNoiseShader object.

Parameters :

- amount ( float ) – The amplitude of the noise.

- scale ( float ) – The noise frequency.

- num_octaves ( int ) – The number of octaves

- smooth ( bool ) – Set true for smooth noise.

- pure_random ( bool ) – Set true if no coherence is wanted.
shade ( stroke ) 

A Spatial Noise stroke shader that shifts vertices to roughen the stroke.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
