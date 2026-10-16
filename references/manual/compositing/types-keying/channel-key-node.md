# Channel Key Node

## Channel Key Node

The Channel Key node separates background from foreground by the difference in a chosen channel's levels — for example, in the YUV color model it suits compositing stock explosion footage (very bright) shot against a solid dark background. Inputs: Image (standard color input); Minimum (the lowest values counted as foreground — meant to be relatively high, from this value to 1.0); and Maximum (the highest values counted as background — meant to be relatively low, from 0.0 to this value), where leaving a gap between Minimum and Maximum gives a transparency gradient between foreground and background. Also: Color Space (the color model the channels represent — RGB, HSV, YUV, YCbCr); Key Channel (which of that model's channels determines the matte); Limit Method (how the level difference is computed — Max, limiting by the maximum of the two channels other than the Key Channel, or Single, limiting by the maximum of a chosen Limit Channel); and Limit Channel (the channel used for the maximum, its options set by the Color Space). Outputs: Image (with its alpha adjusted for the keyed selection) and Matte (a black-and-white alpha mask of the key).

[Related references](INDEX.md).
