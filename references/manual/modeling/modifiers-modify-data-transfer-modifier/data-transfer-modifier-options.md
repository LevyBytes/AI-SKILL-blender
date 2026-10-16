# Data Transfer Modifier: Options

### Options

Source
The mesh object that data is copied from.

Object Transform
Decides whether the world space transforms of the source and destination objects are taken into account.
Leave it off and the modifier behaves as if both objects share the same position
along with default rotation and scale.

Mix Mode
Sets how the incoming source data is merged with the data already on the destination mesh.

Replace
Blend between the original and the new value by way of Mix Factor .

Above Threshold
Swaps in the destination value when it sits at or above Mix Factor .
With multi-component data such as colors, the threshold gets weighed against the average of
those components.

With boolean data such as Freestyle Mark , this gives you a logical AND:
set the Mix Factor to 0.5 or above and the destination mesh keeps a mark only on
edges or faces that were marked already and carry a mark in the source mesh too.

Below Threshold
Swaps in the destination value when it sits at or below Mix Factor .
With multi-component data such as colors, the threshold gets weighed against the average of
those components.

With boolean data such as Freestyle Mark , this gives you a logical OR:
set the Mix Factor to 0.5 or above and the destination mesh keeps a mark on
edges or faces that were marked already or carry a mark in the source mesh.

Mix
Blend the source value into the destination value, an alpha blend for color attributes being one case. Then interpolate using Mix Factor .

Add
Sum the source and destination values, then blend by way of Mix Factor .

Subtract
Take the source value away from the destination value, then blend by way of Mix Factor .

Multiply
Multiply destination by source, then blend by way of Mix Factor .

Mix Factor
The blend amount between the original destination value and the freshly computed one.
Where Mix Mode is Above Threshold or Below Threshold , it serves as a threshold instead.

Vertex Group
Lets the Mix Factor be tuned on a per-element basis.

Invert
Flip the vertex group weights, turning each into 1 - weight.

Generate Data Layers
Click to lay down any data layers that are missing, such as vertex groups present on the source mesh but
not yet on the modified one. Since the modifier won't do it for you, be sure to hit
this button (or add the missing layers yourself), or the transfer may fail.

Any layers laid down this way are left behind once the modifier is removed.

Data Types
The Custom Normals , Colors , UVs and similar toggle buttons flag which data
gets transferred.

Mapping
Sets the way a matching source element (or elements) is found for each destination element.
The choices are laid out in the Mapping section further down.

Layer Selection
Which source layers get copied across to the destination mesh (every vertex group,
or one specific vertex group, for instance).

Layer Mapping
Sets how the destination layer is matched to a given source layer: by name or by order.

Islands Precision
Governs the computation that keeps a destination face from pulling UV coordinates out of
mismatched source UV islands (regions walled off by seams).
Hold it at 0.0 and there's no island handling at all; raise it and correctness improves
at the expense of more computation.

Small figures around 0.02 usually do the trick, but mapping from
a very high-poly source onto a very low-poly destination may force you to push it up considerably.

[Related references](INDEX.md).
