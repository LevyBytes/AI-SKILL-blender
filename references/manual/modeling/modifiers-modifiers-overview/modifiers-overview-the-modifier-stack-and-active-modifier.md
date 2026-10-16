# Introduction: The Modifier Stack, Active Modifier, Example

Extras

Apply Ctrl - A
Turns the modifier "real": rewrites the object's geometry to match what the applied modifier produced,
and removes the modifier.

If you apply a modifier on an object that shares Object Data with others,
the object has to be made a Single User first,
done by accepting the pop-up message.

Warning

Apply a modifier that isn't first in line and the stack order gets disregarded
(it acts as though it were first), which can yield results you didn't want.

Apply as Shape Key
Tucks that modifier's result into a fresh relative shape key
and then drops the modifier from the stack.
Only modifiers that leave topology alone offer this (Deform modifiers, as a rule).

Note

In principle it ought to handle any geometry type that supports shape keys,
but right now meshes are the only thing it works on.

Save as Shape Key
Tucks that modifier's result into a fresh relative shape key
while leaving the modifier sitting in the stack.
Only modifiers that leave topology alone offer this (Deform modifiers, as a rule).

Duplicate Shift - D
Drops a copy of the modifier into the stack right beneath the current one.

Copy to Selected
Pushes the modifier from the Active object out to every selected object.

Move to First/Last
Shifts the modifier to the very top or very bottom of the stack.

Pin to Last
Holds the modifier at the tail of the stack.
A pinned modifier shows a pin icon on the right-hand side of its panel header.

Move to Nodes
Converts the current Geometry Nodes Modifier
node tree into a group node, ready for reuse across other trees.
The Move to Nodes Operator section spells this out.

Only the Geometry Nodes Modifier offers this operator.

Delete X , Delete
Removes the modifier.

(Move)
Shifts the modifier up or down the stack,
which alters the order in which the modifiers are evaluated.

A modifier can't be moved while Pin to Last is on.

Underneath this header sit all the options that belong to each individual modifier.

Tip

Hold Alt to act on every selected object at once
during operators like add, apply, remove, and move to index.

See Multi-Object Editing for more information.

### The Modifier Stack

A modifier is one link in a chain of non-destructive operations stacked over an object's geometry, and you can sequence them in almost whatever order suits you. People commonly call this arrangement a "modifier stack," and you'll run into it across various other 3D packages as well.

Inside a stack, the sequence the modifiers run in shapes the outcome. To reshuffle them, grab the grip icon at the upper right and drag your chosen modifier higher or lower. For example, the picture below shows Subdivision Surface and Mirror modifiers once they've traded places.

| Description | Description |
| --- | --- |
| The Mirror modifier is the last item in the stack and the result looks like two surfaces. | The Subdivision Surface modifier is the last item in the stack and the result is a single merged surface. |

The stack is evaluated top to bottom. Here the wanted outcome (shown on the right) comes from mirroring the object first and then working out the subdivision surface.

#### Active Modifier

Click a modifier in the stack and it becomes Active, drawn with an outline framing its panel. To make one active, click its panel background or its icon, or pick the modifier over in the Outliner.

The Geometry Node Editor relies on the active modifier to know which node group it's editing.

### Example

Here a plain subdivided cube has been worked up into a fairly intricate object by stacking modifiers on it.

Download example file.

[Related references](INDEX.md).
