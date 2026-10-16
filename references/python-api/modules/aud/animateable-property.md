# aud.AnimateableProperty

class aud.AnimateableProperty

An AnimateableProperty stores float value arrays for animating sound parameters (such as pan, volume, pitch scale).
read(position)

Retrieves the property value at the specified position.

Parameters:

position (float) – The animation position in frames.

Returns:

A numpy array of property values.

Return type:

numpy.ndarray
readSingle(position)

Retrieves the property value at the specified position, if there is one value.

Parameters:

position (float) – The animation position in frames.

Returns:

The value at that position.

Return type:

float
write(data [, position])

Sets the property value. With position, the property becomes animated and values are written from that position onward.

Parameters:

- data (numpy.ndarray) – numpy array of float32 values.

- position (int) – The starting position in frames.
writeConstantRange(data, position_start, position_end)

Populates a span of frames with a single unchanging value and designates it animated.

Parameters:

- data (numpy.ndarray) – A numpy array holding float values for the constant.

- position_start (int) – Frame index marking the beginning.

- position_end (int) – Frame index marking the conclusion.
animated

Whether the property is animated.
count

The quantity of floats per property.

[Related references](INDEX.md).
