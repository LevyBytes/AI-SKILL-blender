# bpy.types.FCurve: bake

bake ( start , end , * , step = 1.0 , remove = '`IN_RANGE`' )

Drop keys at regular spacing along the curve as it already stands.

Parameters :

- start ( int ) – Start Frame, Frame at which to start baking (in [-1048574, 1048574])

- end ( int ) – End Frame, Frame at which to end baking (inclusive) (in [-1048574, 1048574])

- step ( float ) – Step, At which interval to add keys (in [0.01, inf], optional)

- remove ( Literal [ 'NONE' , '`IN_RANGE`' , '`OUT_RANGE`' , 'ALL' ] ) – Remove Options, Choose which keys should be automatically removed by the bake (optional)

- NONE
None – Hold on to every key.

- `IN_RANGE`
In Range – Drop every key falling inside the chosen range.

- `OUT_RANGE`
Outside Range – Drop every key falling outside the chosen range.

- ALL
All – Drop every key that already exists.

[Related references](INDEX.md).
