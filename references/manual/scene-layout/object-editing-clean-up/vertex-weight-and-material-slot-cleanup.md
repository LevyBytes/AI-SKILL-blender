# Clean Up: Clean Vertex Group Weights, Limit Total Vertex Groups, Remove Unused Material Slots

## Clean Up

### Clean Up

### Clean Vertex Group Weights

Reference

Mode :

Object Mode

Menu :

Object ‣ Clean Up ‣ Clean Vertex Group Weights

This operation removes vertex assignments from Vertex Groups whose weights fall below the Limit threshold. It eliminates insignificant (or zero) weights from your weight groups.

The displayed example uses a 0.2 cutoff (see operator options below), removing all blue areas.

Note: these images employ Show Zero weights Active so unreferenced Weights appear Black.

Clean example.

Subset
Narrow the tool to a subset. Refer to The Subset Option section for subset definition.

Limit
The minimum weight value retained in the group. Weights below this threshold are removed.

Keep Single
Guarantees the Clean Vertex Group Weights operation will not produce completely unlinked vertices (vertices not in any vertex group). Each vertex retains at least one weight, even below the limit.

### Limit Total Vertex Groups

Reference

Mode :

Object Mode

Menu :

Object ‣ Clean Up ‣ Limit Total Vertex Groups

Reduces the weight group count per vertex to the specified Limit. Lowest weights are discarded until the limit is met.

Hint

The tool requires more than one weight group selected to function well.

Subset
Narrow the tool to a subset. Refer to The Subset Option section for subset definition.

Limit
The maximum weight count permitted on each vertex.

### Remove Unused Material Slots

Reference

Mode :

Object Mode

Menu :

Object ‣ Clean Up ‣ Remove Unused Material Slots

Removes unused material slots.

[Related references](INDEX.md).
