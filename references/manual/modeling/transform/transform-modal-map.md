# Transform Modal Map

## Transform Modal Map

### Transform Modal Map

While a transformation is underway, certain hotkeys let you alter how the operation behaves.

You can check editing the keys of these modal modifiers in
Blender Preferences ‣ Keymap ‣ Transform Modal Map
(at the bottom of the keymap).

### Constraints

If you want a move, rotation, or scale to touch only some axes, you can lock the transformation down to those.

Out of the box those constraint keys are X , Y and Z .
Hold Shift while pressing one to limit the constraint to a plane, or
press MMB to have it picked out automatically.

It's worth noting that pressing the same constraint hotkey again
flips the orientation between Local and Global; a third press turns the constraint off.

### Snapping

Transform operations use the snapping settings set in the scene.
That said, some options can be tweaked mid-transformation.

### Snap Invert

Even with the magnetic icon switched off, snapping can be kicked in partway through a transformation.
By default Ctrl is the hotkey for that.

### Set Snap Base

Blender works out the Snap Base automatically from the Snap Base options.
But that auto-detected point of origin won't always be where the user actually wants it.
So transform operations include a tool for setting a fresh snap origin mid-transformation.
The new Snap Base lines up with the snap point whose target the
Snap Target defines.

By default the hotkey is B .

Note

When Snap to Increment is the only Snap Target enabled,
the targets Vertex , Edge , Face and Edge Center step in instead.

### Add Snap Point

With snapping on as you transform a selection,
press A any time a snap target is highlighted to
flag it. Flag several targets and the selection
snaps to their average location.

Flag a target more than once and it counts for more.

Multiple snapping targets.

### Navigating

A transformation doesn't lock you out of navigation: hold Alt and you can still zoom, pan, or orbit while it runs.

This behavior can be changed through the Transform Navigation with Alt setting
in the Keymap Preferences.

[Related references](INDEX.md).
