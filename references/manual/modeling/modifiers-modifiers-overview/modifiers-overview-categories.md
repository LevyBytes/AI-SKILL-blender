# Introduction: Categories

### Introduction

Think of modifiers as automatic, non-destructive operations applied to an object's geometry. Through them you can pull off plenty of effects that would be painfully tedious by hand (subdivision surfaces among them), all while the object's underlying geometry stays untouched.

The thing they alter is how the object shows up on screen and in renders, not the geometry you edit directly. You're free to pile several modifiers onto one object, where together they make up The Modifier Stack, and any time you want a modifier's effect made permanent you can Apply it.

To add one to the active object, reach for the Add Modifier operator, the "Add Modifier" button sitting atop the Modifiers tab of the Properties Editor, or Shift - A while that tab is focused. Whatever you add lands at the foot of the stack, so it runs last.

A wide assortment of modifiers ships with Blender, and on top of that users can roll their own by way of Geometry Nodes.

### Categories

Built-in modifiers fall into four categories:

Edit
Akin to the Deform modifiers described below,
yet for the most part these leave the object's geometry alone
and act on other data instead, vertex groups among them.

Generate
Constructive or destructive modifiers that reshape the mesh's whole Topology.
They can shift the object's overall look or graft new geometry onto it…

Deform
Set apart from the Generate group above, these alter only an object's shape, leaving its topology intact.

Simulate
Stand in for physics simulations. Usually they get slotted into
the modifier stack on their own the moment a Particle System or Physics simulation is switched on. Their sole job is to mark
the point in the stack where the simulation they stand for reads its base data.
For that reason they tend to carry no properties of their own, being driven instead by settings found in
other parts of the Properties Editor.

A category labeled "Hair" will also catch your eye;
it originates from a bundled Asset Library shipped alongside Blender.
See Hair Nodes for more information.

Users can roll their own categories by turning geometry node groups into assets
and filing them under an Asset Catalog. Whatever the catalog is called becomes the category name.
Should a user name a catalog after one of the built-in categories,
its node group lands at the foot of the matching menu.

Node Groups that are non-assets, or that fall under no category, show up in the "Unassigned" sub-menu.

Note

A Geometry Node Group only appears in the Add Modifier menu once its Modifier
property has been switched on.

[Related references](INDEX.md).
