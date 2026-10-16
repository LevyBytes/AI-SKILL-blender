# bpy.ops.sequencer.strip_modifier_equalizer_redefine

bpy.ops.sequencer.strip_modifier_equalizer_redefine(*, graphs='SIMPLE', name='Name')

Modify the definitions of equalizer curves.

Parameters:

- graphs (Literal['SIMPLE', 'DOUBLE', 'TRIPLE']) – Graphs, Quantity of curves (optional)
  - SIMPLE
    Unique – One distinct graphical meaning.
  - DOUBLE
    Double – Graphical meaning in 2 areas.
  - TRIPLE
    Triplet – Graphical meaning in 3 areas.
- name (str) – Name, Name of modifier to redescribe (optional, never None)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.strip_modifier_equalizer_redefine(*, graphs='SIMPLE', name='Name')

Modify the definitions of equalizer curves.

Parameters:

- graphs (Literal['SIMPLE', 'DOUBLE', 'TRIPLE']) – Graphs, Quantity of curves (optional)
  - SIMPLE
    Unique – One distinct graphical meaning.
  - DOUBLE
    Double – Graphical meaning in 2 areas.
  - TRIPLE
    Triplet – Graphical meaning in 3 areas.
- name (str) – Name, Name of modifier to redescribe (optional, never None)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer. strip_modifier_equalizer_redefine ( * , graphs = 'SIMPLE' , name = 'Name' ) 

Rebuild the equalizer graphs

Parameters :

- graphs ( Literal [ 'SIMPLE' , 'DOUBLE' , 'TRIPLE' ] ) – Graphs, How many graphs to use (optional)

- SIMPLE
Unique – A single graphical definition.

- DOUBLE
Double – A graphical definition divided into 2 sections.

- TRIPLE
Triplet – A graphical definition divided into 3 sections.

- name ( str ) – Name, Which modifier to redefine, by name (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
