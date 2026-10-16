# bpy.types.USDHook: Example Code

### Example Code

In the example that follows, the USDHookExample class wires up these functions:

- on_export() function to add custom data to the stage’s root layer.

- on_material_export() function to create a simple MaterialX shader on the given USD material.

- on_import() function to create a text object to display the stage’s custom layer data.

- material_import_poll() returns True if the given USD material has an mtlx context.

- on_material_import() function to convert a simple MaterialX shader with a base_color input.

[Open the complete example modules](../../examples/usd-hooks/INDEX.md).

[Related references](INDEX.md).
