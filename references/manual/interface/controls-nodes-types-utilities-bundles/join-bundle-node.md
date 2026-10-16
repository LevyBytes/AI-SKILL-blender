# Join Bundle Node

## Join Bundle Node

The Join Bundle node combines multiple input bundles into a single output bundle. Each input bundle merges by name. If multiple bundles contain same-name sockets (duplicate keys), the first occurrence is used; an information icon signals detection.

Bundle inputs one or more bundles to combine. Bundle outputs the merged result containing all input items. Use Separate Bundle Node to extract items if needed.

### Join Bundle Node

Merge multiple bundles: each input's contents fold into the output.

### Inputs

**Bundle**
One or more input bundles to merge.
Contents merge by name into the output.

**Note:** If multiple inputs share socket names (duplicates), the first occurrence wins.
An information icon flags duplicates in the header.

### Outputs

**Bundle**
Combined bundle holding all input items.

Use Separate Bundle to extract individual items if needed.

### Join Bundle Node

This node folds several bundles into one output bundle. Each input bundle wired in is merged with the rest, leaving a lone bundle carrying everything the inputs held.

### Inputs

Bundle
A bundle or several, to be combined. Each one's contents fold into the output bundle keyed by name.

Note

Where several bundles carry sockets sharing a name (duplicate keys), the value from the first one wins. An information icon in the node header flags any duplicate keys it spots.

### Outputs

Bundle
The resulting bundle, holding every item from the input bundles.

Reach for the Separate Bundle Node to pull individual items back out of the combined bundle when you need them.

[Related references](INDEX.md).
