# bpy.ops.scene.new

bpy.ops.scene. new ( * , type = 'NEW' )

Establish a fresh scene selected by kind

Parameters :

type ( Literal [ 'NEW' , 'EMPTY' , '`LINK_COPY`' , '`FULL_COPY`' ] ) – Type, (optional)

- NEW
New – Add a new, empty scene with default settings.

- EMPTY
Copy Settings – Add a new, empty scene, and copy settings from the current scene.

- `LINK_COPY`
Linked Copy – Link in the collections from the current scene (shallow copy).

- `FULL_COPY`
Full Copy – Make a full copy of the current scene.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
