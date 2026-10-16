# Clean Up: Clean, Quantize, Levels

### Clean

Clean Vertex Group Weights strips vertices from
Vertex Groups
whose weights fall below the Limit threshold. Removes low weights.
Useful for clearing groups of minimal (or empty) weight assignments.

In the example, a threshold of 0.2 removes
all blue sections.

Note, images display Show Zero weights Active
so unassigned weights appear Black.

Clean example.

Subset
Limit operation to a subset.
See The Subset Option above for subset definitions.

Limit
The minimum weight magnitude retained. Weights below this remove from the group.

Keep Single
Prevents the Clean operation from producing completely unassigned vertices
(not linked to any group), ensuring each keeps at least one weight even below threshold!

### Quantize

This tool uses Quantization,
constraining input weights to discrete steps between (0 - 1),
eliminating smooth gradients.

Quantize example (Steps = 2).

Steps
How many discrete intervals between 0 and 1 to divide weights into.
For instance, 5 yields allowed values [0.0, 0.2, 0.4, 0.6, 0.8, 1.0] .

### Levels

Applies offset and scaling to active group weights.
Adjust the perceived "intensity" of the weight group using this tool.

Note

All results clamp between 0.0 and 1.0 regardless of input values.

Levels example.

Subset
Limit operation to a subset.
See The Subset Option above for subset definitions.

Offset
A value within (-1.0 - 1.0) added across all weights in the group.

Gain
All Subset weights multiply by the gain factor.

Note

Whichever Gain and Offset values apply,
the final result always clamps to
(0.0 - 1.0). Negative weights and excessive areas
(weight > 1.0) never occur with this tool.

[Related references](INDEX.md).
