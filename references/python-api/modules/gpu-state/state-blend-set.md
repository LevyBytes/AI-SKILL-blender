# gpu.state: gpu.state. blend_set ( mode )

gpu.state. blend_set ( mode )

Sets the blending equation of the fixed pipeline.

Parameters :

mode ( Literal [ 'NONE' , 'ALPHA' , '`ALPHA_PREMULT`' , 'ADDITIVE' , '`ADDITIVE_PREMULT`' , 'MULTIPLY' , 'SUBTRACT' , 'INVERT' ] ) – The type of blend mode.

- NONE No blending.

- ALPHA Blends the existing color channels by weighting them with the alpha value.

- `ALPHA_PREMULT` Blends the existing color channels by the alpha value, with the incoming colors already multiplied through by it.

- ADDITIVE Sums the existing color channels with their counterparts.

- `ADDITIVE_PREMULT` Sums the existing color channels with their counterparts after those have been pre-multiplied by alpha.

- MULTIPLY Scales the existing color channels by their counterparts.

- SUBTRACT Takes the counterpart channels away from the existing color channels.

- INVERT Swaps the existing color channels for their complementary color.

[Related references](INDEX.md).
