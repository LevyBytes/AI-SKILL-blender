# bpy.ops.file.external_operation

bpy.ops.file.external_operation(*, operation='OPEN')

Perform an action on a document or directory outside of Blender

Parameters:

operation (Literal['OPEN', '`FOLDER_OPEN`', 'EDIT', 'NEW', 'FIND', 'SHOW', 'PLAY', 'BROWSE', 'PREVIEW', 'PRINT', 'INSTALL', 'RUNAS', 'PROPERTIES', '`FOLDER_FIND`', 'CMD']) – Operation, Work to execute with the marked document or route (optional)

- OPEN
Open – Launch the document.

- `FOLDER_OPEN`
Open Folder – Launch the folder.

- EDIT
Edit – Modify the document.

- NEW
New – Make a fresh document of this form.

- FIND
Find File – Seek documents of this form.

- SHOW
Show – Exhibit this document.

- PLAY
Play – Execute this document.

- BROWSE
Browse – Look through this document.

- PREVIEW
Preview – Peek at this document.

- PRINT
Print – Output this document.

- INSTALL
Install – Set up this document.

- RUNAS
Run As User – Run as specific user.

- PROPERTIES
Properties – Reveal system traits for this element.

- `FOLDER_FIND`
Find in Folder – Hunt for things in this folder.

- CMD
Command Prompt Here – Launch a shell session here.

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
