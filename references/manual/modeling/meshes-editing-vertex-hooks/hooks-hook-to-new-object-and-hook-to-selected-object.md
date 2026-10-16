# Hooks: Hook to New Object, Hook to Selected Object, Hook to Selected Object Bone

## Hooks

### Hooks

This mechanism pairs with the Hook Modifier, which "hooks" vertex sets to an external object. Moving that object also moves those vertices.

The reverse – attaching an external object to a vertex – uses Make Vertex Parent.

### Hook to New Object

Reference

Mode:

Edit Mode

Menu:

Vertex → Hooks → Hook to New Object

Shortcut:

Ctrl - H

Generates an Empty at the selected vertices' average position, then installs a Hook modifier tying vertices to the Empty.

If no vertices are chosen, the active Vertex Group gets used instead.

### Hook to Selected Object

Reference

Mode:

Edit Mode

Menu:

Vertex → Hooks → Hook to Selected Object

Shortcut:

Ctrl - H

Installs a Hook modifier linking the chosen vertices to the chosen object (not the active mesh). If no vertices are chosen, the active Vertex Group gets used instead.

To pick another object while in Edit Mode, use the Outliner or Ctrl - LMB in the 3D Viewport.

### Hook to Selected Object Bone

Reference

Mode:

Edit Mode

Menu:

Vertex → Hooks → Hook to Selected Object Bone

Shortcut:

Ctrl - H

Installs a Hook modifier linking the chosen vertices to the chosen bone.
If no vertices are chosen, the active Vertex Group gets used instead.

To choose the bone of another object while in Edit Mode, click it with Ctrl - LMB in the 3D Viewport.

Tip

The Armature Modifier is the more typical way to attach vertices to bones.

[Related references](INDEX.md).
