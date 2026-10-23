# bpy.types.FileHandler: Basic FileHandler for importing a single file

### Basic FileHandler for importing a single file

Through a file handler you can attach custom drag-and-drop behavior to a particular Operator
(FileHandler.bl_import_operator) together with a list of file extensions
(FileHandler.bl_file_extensions). Which UI area is willing to receive the
drag-and-drop is decided by the FileHandler.poll_drop method.

Just like operators that open a file select window, an operator taking part in drag-and-drop while
handling only one file has to declare the property below:

```text
filepath: bpy.props.StringProperty(subtype='`FILE_PATH`', options={'`SKIP_SAVE`'})
```

Once the user drops a file, this filepath property receives that file's full path.

The complete program is in the [upstream source](https://docs.blender.org/api/5.1/bpy.types.FileHandler.html#basic-filehandler-for-importing-a-single-file).

[Related references](INDEX.md).
