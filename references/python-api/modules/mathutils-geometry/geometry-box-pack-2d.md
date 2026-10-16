# mathutils.geometry: mathutils.geometry. box_pack_2d ( boxes , / )

mathutils.geometry. box_pack_2d ( boxes , / )

Hands back a tuple holding the packed bounding box's width and height.

Parameters :

boxes ( list [ list [ float ] ] ) – list of boxes, each box is a list where the first 4 items are [X, Y, width, height, …] other items are ignored. The X & Y values in this list are modified to set the packed positions.

Returns :

The width and height of the packed bounding box.

Return type :

tuple[float, float]

[Related references](INDEX.md).
