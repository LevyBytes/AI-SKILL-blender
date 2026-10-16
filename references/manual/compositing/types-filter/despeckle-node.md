# Despeckle Node

## Despeckle Node

The Despeckle node smooths noticeably noisy areas of an image while leaving complex areas alone, working by computing each pixel's standard deviation with its neighbors to gauge whether an area is high- or low-complexity, then smoothing it with a simple mean filter if the complexity is below the threshold. Inputs: Image (standard color input); Factor (how much the filter affects the image); Color Threshold (the threshold separating high and low complexity); and Neighbor Threshold (the threshold for how many pixels must match). Output: Image (standard color output).

[Related references](INDEX.md).
