# Filter Node

## Filter Node

The Filter node implements several common image-enhancement filters. Inputs: Image (standard color input); Factor (how much the node influences the output); and Type — where Soften, Laplace, Sobel, Prewitt, and Kirsch all detect edges (in slightly different ways) via vector calculus and set theory: Soften (slightly blur), Box Sharpen (raise contrast, especially at edges), Diamond Sharpen (less aggressive than Box, reducing artifacts), Laplace (edge highlighting, prone to highlighting noise), Sobel (a negative image highlighting edges), Prewitt (similar to Sobel), Kirsch (better blending than Sobel or Prewitt near an edge), and Shadow (a relief/emboss effect, darkening outside edges). Output: Image (standard color output).

[Related references](INDEX.md).
