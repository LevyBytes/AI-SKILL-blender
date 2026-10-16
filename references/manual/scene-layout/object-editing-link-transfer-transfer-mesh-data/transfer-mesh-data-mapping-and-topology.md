# Transfer Mesh Data: Mapping, Topology

Source Layers Selection
Specifies which source layers to transfer to destination meshes (e.g. only the active vertex group, all vertex groups, or a named vertex group).

Destination Layers Matching
The method for identifying destination layers for provided source layers: by identity or by sequential order.

Mix Mode
How to combine transferred source data with existing destination mesh data.

Replace
Blend between original and new values using Mix Factor.

Above Threshold
Substitute the destination value if it surpasses or equals Mix Factor. For multi-component data such as colors, threshold evaluation compares against component averages.

For boolean Data Types like Freestyle Mark, this achieves a logical AND: ensure Mix Factor is 0.5 or higher, and marked edges/faces in both source and destination are retained.

Below Threshold
Substitute the destination value if it falls below or equals Mix Factor. For multi-component data such as colors, threshold evaluation compares against component averages.

For boolean Data Types like Freestyle Mark, this achieves a logical OR: ensure Mix Factor is 0.5 or higher, and marked edges/faces from either source or destination are retained.

Mix
Combine transferred source value with destination value, like alpha blending for color attributes. Then, blend using Mix Factor.

Add
Add transferred source value to destination value, then blend using Mix Factor.

Subtract
Remove transferred source value from destination value, then blend using Mix Factor.

Multiply
Amplify destination value by transferred source value, then blend using Mix Factor.

Mix Factor
Interpolation balance between original destination value and newly computed value. When Mix Mode is Above Threshold or Below Threshold, this becomes a threshold value instead.

### Mapping

### Topology

Matches components by numerical ordering. All meshes must have matching element counts and identical ordering. Best for destination meshes that are deformed copies of sources.

See also

Sort Elements to guarantee matching element ordering.

[Related references](INDEX.md).
