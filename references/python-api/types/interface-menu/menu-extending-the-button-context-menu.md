# bpy.types.Menu: Extending the Button Context Menu

### Extending the Button Context Menu

With this approach you can add a custom entry to the right-click menu that pops up whenever the cursor is over a UI button (an operator, a value field, a color, a string, and so on).

For the example to run, select an object first, then right-click on some interface widget — perhaps a color in the material properties — and pick Execute Custom Action.

Running the operator prints every value out.

The complete program is in the [upstream source](https://docs.blender.org/api/5.1/bpy.types.Menu.html#extending-the-button-context-menu).

base class: bpy_struct

[Related references](INDEX.md).
