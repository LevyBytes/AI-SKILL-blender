# Anti-Aliasing Node

## Anti-Aliasing Node

The Anti-Aliasing node removes jagged edges. Inputs: Image (standard color input); Threshold (edge-detection sensitivity across the whole image); Contrast Limit (the contrast level to consider when detecting edges — since the eye doesn't perceive all edges equally and tends to mask low-contrast edges amid much higher surrounding contrast, anti-aliasing those unperceived edges makes artifacts, and this quantifies the difference between low- and high-contrast neighboring edges); and Corner Rounding (detect corners to preserve the original shape — 0 means no corner detection or rounding, and higher values better preserve corners). Output: Image (standard color output). Examples show that changing the threshold affects all edges, the contrast limit affects neighboring edges below it, and corner detection/rounding off (0) smooths corners as artifacts while full detection preserves the sharp edges.

[Related references](INDEX.md).
