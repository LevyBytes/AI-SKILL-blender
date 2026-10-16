# Undo & Redo: Undo, Redo, Adjust Last Operation

## Undo & Redo

### Undo & Redo

The tools below let you back out of a mistaken action, redo your most recent one, or jump to a particular moment by choosing from the list of recent actions Blender keeps.

### Undo
Reference

Mode :

All Modes

Menu :

Edit ‣ Undo

Shortcut :

Ctrl - Z

Undo your last action with a simple Ctrl - Z.

See also

Memory & Limits Preferences to change undo settings.

### Redo
Reference

Mode :

All Modes

Menu :

Edit ‣ Redo

Shortcut :

Shift - Ctrl - Z

Reverse an Undo with Shift - Ctrl - Z.

### Adjust Last Operation
Reference

Mode :

All Modes

Menu :

Edit ‣ Adjust Last Operation…

Shortcut :

F9

After an operator runs, you can fine-tune its parameters. Where supported, a "head-up display" panel for the last operation sits in the bottom left of the editor. F9 raises the same thing as a pop-up if you'd rather.

Say your last action was a rotation in Object Mode: Blender surfaces the last angle value you changed (see Fig. Rotation (Object Mode, 60 degrees). left), and typing Numpad0 into the Angle Field reverses it entirely. Other useful options appear depending on the operator, so you're not limited to undoing — you can fully reshape an action through the available options.

Over in Edit Mode, Blender adapts the panel's contents to your last action too. In the second example (on the right), the last operation in Object Mode was a Move, but in Edit Mode it was a Scale on a Face — and, as you can see, the contents of Adjust Last Operation differ because of the mode (Edit Mode) (See Fig. Scale (Edit Mode, Resize face). right).

| Description | Description |
| --- | --- |
| Rotation (Object Mode, 60 degrees). | Scale (Edit Mode, Resize face). |

Tip

Particularly useful results come out of Adjust Last Operation for some operations. Add a Circle in the 3D Viewport, for example; drop the Vertices to three and you land a perfect equilateral triangle.

Tip

Tucking the Adjust Last Operation region out of sight is done through View ‣ Adjust Last Operation .

[Related references](INDEX.md).
