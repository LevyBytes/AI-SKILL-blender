# Switch Node

## Switch Node

The Switch node switches between two images via a checkbox. Tip: the switch state can be animated with a keyframe, making it handy for bypassing nodes you don't want during part of a sequence. Inputs: Switch (unchecked passes the first input, "Off," to the output; checked passes the second, "On"), Off (the first image), and On (the second image). Output: Image (standard color output).

Routes one of two inputs based on a boolean condition.

When inputs are regular values, only the routed input evaluates.
When inputs are Fields, both may evaluate before selection is applied; do not rely on this node to skip expensive field computations.

See also: Menu Switch Node and Index Switch Node for multi-input selection.

**Inputs**

Switch
Determines which input passes through.

False
Routed when switch is false.

True
Routed when switch is true.

**Properties**

Type
Sets the data type handled by the node.

**Outputs**

Output
One of the two inputs unchanged.

[Related references](INDEX.md).
