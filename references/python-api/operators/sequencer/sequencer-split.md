# bpy.ops.sequencer.split

bpy.ops.sequencer.split(*, frame=0, channel=0, type='SOFT', use_cursor_position=False, side='MOUSE', ignore_selection=False, ignore_connections=False)

Partition the chosen pieces into halves.

Parameters:

- frame (int) – Frame, Picture where chosen pieces will be partitioned (in [-inf, inf], optional)
- channel (int) – Channel, Track in which piece will be severed (in [-inf, inf], optional)
- type (Literal['SOFT', 'HARD']) – Type, How the cut is performed on selected pieces (optional)
- use_cursor_position (bool) – Use Cursor Position, Sever at the pointer instead of current picture (optional)
- side (Literal['MOUSE', 'LEFT', 'RIGHT', 'BOTH', '`NO_CHANGE`']) – Side, Which direction continues picked after severing (optional)
- ignore_selection (bool) – Ignore Selection, Make cut even if piece is not picked maintaining choice state after cut (optional)
- ignore_connections (bool) – Ignore Connections, Keep cuts isolated to individual strips (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.split(*, frame=0, channel=0, type='SOFT', use_cursor_position=False, side='MOUSE', ignore_selection=False, ignore_connections=False)

Partition the chosen pieces into halves.

Parameters:

- frame (int) – Frame, Picture where chosen pieces will be partitioned (in [-inf, inf], optional)
- channel (int) – Channel, Track in which piece will be severed (in [-inf, inf], optional)
- type (Literal['SOFT', 'HARD']) – Type, How the cut is performed on selected pieces (optional)
- use_cursor_position (bool) – Use Cursor Position, Sever at the pointer instead of current picture (optional)
- side (Literal['MOUSE', 'LEFT', 'RIGHT', 'BOTH', '`NO_CHANGE`']) – Side, Which direction continues picked after severing (optional)
- ignore_selection (bool) – Ignore Selection, Make cut even if piece is not picked maintaining choice state after cut (optional)
- ignore_connections (bool) – Ignore Connections, Keep cuts isolated to individual strips (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer. split ( * , frame = 0 , channel = 0 , type = 'SOFT' , use_cursor_position = False , side = 'MOUSE' , ignore_selection = False , ignore_connections = False ) 

Cut each selected strip into two

Parameters :

- frame ( int ) – Frame, The frame at which the selected strips are divided (in [-inf, inf], optional)

- channel ( int ) – Channel, The channel where the cut is made (in [-inf, inf], optional)

- type ( Literal [ 'SOFT' , 'HARD' ] ) – Type, Which kind of split to run on the strips (optional)

- use_cursor_position ( bool ) – Use Cursor Position, Cut at the cursor's location rather than at the current frame (optional)

- side ( Literal [ 'MOUSE' , 'LEFT' , 'RIGHT' , 'BOTH' , '`NO_CHANGE`' ] ) – Side, Which part stays selected after the cut (optional)

- ignore_selection ( bool ) – Ignore Selection, Cut even unselected strips, leaving the selection state unchanged afterward (optional)

- ignore_connections ( bool ) – Ignore Connections, Stop the split from carrying through to connected strips (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
