# Directional Blur Node

## Directional Blur Node

The Directional Blur node blurs an image along a chosen direction, usable to fake motion blur. Inputs: Image (standard color input); Samples (the sample count — more samples are smoother but slower, the actual number being two to the power of this input, so it grows exponentially); Center (the pivot for the transformations, in normalized coordinates where 0 is the lower-left and 1 the upper-right); Rotation (how much rotation the blur spans); and Scale (how much scaling the blur spans). Translation: Amount (how much translation the blur spans in the given direction relative to the image size, with negative values going the opposite way) and Direction (the angle setting the translation direction). Output: Image (standard color output).

[Related references](INDEX.md).
