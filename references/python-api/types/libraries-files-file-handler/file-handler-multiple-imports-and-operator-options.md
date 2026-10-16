# bpy.types.FileHandler: FileHandler for Importing multiple files and exposing Operator options

### FileHandler for Importing multiple files and exposing Operator options

An operator that can run with several drag-and-dropped files at once needs these properties
declared: `directory` and `files`, as shown in the complete linked operator.


The drag-and-drop operation fills these directory and files properties with the data it needs.

On top of that, when the operator exposes operator properties the user should be able to reach,
the ImportHelper.invoke_popup method can present a dialog that reuses the standard
Operator.draw method for its layout and display.

[Complete example](../../examples/shader-file-import.py).

The complete operator declares the `directory` and `files` properties and their hidden, unsaved flags.

[Related references](INDEX.md).
