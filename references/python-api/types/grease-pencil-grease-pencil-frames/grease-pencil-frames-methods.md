# bpy.types.GreasePencilFrames: methods

new ( frame_number )

Add a new Grease Pencil frame

Parameters :

frame_number ( int ) – Frame Number, The frame on which the drawing appears (in [-1048574, 1048574])

Returns :

The newly created frame

Return type :

GreasePencilFrame
remove ( frame_number )

Remove a Grease Pencil frame

Parameters :

frame_number ( int ) – Frame Number, The frame number of the frame to remove (in [-1048574, 1048574])
copy ( from_frame_number , to_frame_number , * , instance_drawing = False )

Copy a Grease Pencil frame

Parameters :

- from_frame_number ( int ) – Source Frame Number, The frame number of the source frame (in [-1048574, 1048574])

- to_frame_number ( int ) – Frame Number of Copy, The frame number to copy the frame to (in [-1048574, 1048574])

- instance_drawing ( bool ) – Instance Drawing, Let the copied frame use the same drawing as the source (optional)

Returns :

The newly copied frame

Return type :

GreasePencilFrame
move ( from_frame_number , to_frame_number )

Move a Grease Pencil frame

Parameters :

- from_frame_number ( int ) – Source Frame Number, The frame number of the source frame (in [-1048574, 1048574])

- to_frame_number ( int ) – Target Frame Number, The frame number to move the frame to (in [-1048574, 1048574])

Returns :

The moved frame

Return type :

GreasePencilFrame
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
