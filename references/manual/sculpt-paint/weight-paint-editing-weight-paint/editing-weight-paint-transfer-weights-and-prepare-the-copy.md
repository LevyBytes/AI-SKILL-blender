# Editing Weight Paint: Transfer Weights, Prepare the Copy, Adjust Last Operation Panel Confusion, Limit Total, Set Weight

### Transfer Weights

Move weights from other objects to the active object's groups.

By default transfers only the active group of source to
the active group of target or generates a new one if absent.
Behavior adjusts through the Adjust Last Operation panel.

For instance, shift Source Layers Selection to By Name
to copy all source groups to target.

Note

This tool applies generic "data transfer" from all selected objects to the target.
Consult Data Transfer
documentation for option explanations.

### Prepare the Copy

First choose all source objects, then pick the target
(target must remain active).

Source and target positioning matters.
Placement at opposite sides prevents successful transfer. (Review Vertex Mapping.)
Separate layer assignment works,
yet all must stay visible during tool invocation.

Ensure target sits in Weight Paint Mode.
Access the Toolbar and locate Transfer Weights in the Weight Tools area.

### Adjust Last Operation Panel Confusion

The Adjust Last Operation panel persists
post-transfer completion. It vanishes
only after calling another Operator with its own panel.
This confuses when reusing Transfer weights after vertex group changes.
Reapplying the existing panel
resets work to its initial state before your original Transfer Weights activation.

Wanting to invoke Transfer Weights afresh after modifying
groups? Always press the Transfer Weights button,
unless intentionally reverting to the first call.

### Limit Total

Reduce each vertex's weight count to the specified Limit.
Lowest weights get removed until threshold hits.

Hint

Operation works best with multiple selected groups.

Subset
Limit operation to a subset.
See The Subset Option above for subset definitions.

Limit
Maximum weights per vertex allowed.

### Set Weight

Reference

Mode :
Weight Paint Mode

Menu :
Weight ‣ Set Weight

Shortcut :
Ctrl - X

Populate the active group with the selected brush weight value.

[Related references](INDEX.md).
