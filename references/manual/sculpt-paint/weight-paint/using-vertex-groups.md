# Using Vertex Groups

## Using Vertex Groups

### Using Vertex Groups

### Vertex Groups for Bones

One of the principal applications of weight painting. Though Blender can
generate weights mechanically (see
Skinning),
manual tweaking or full creation suits many cases,
particularly near articulations.

Steps involved:

- Pick the armature, shift to Pose Mode using Ctrl - Tab .

- Verify that Edit ‣ Lock Object Modes remains off
in the menu bar.

- Pick the mesh and switch to Weight Paint Mode .

- Ensure Bone Selection appears enabled in the 3D Viewport header.

- Pick a bone using Alt - LMB (or Shift - Ctrl - LMB ).
The bone's group activates and displays its assignments on the surface.

- Use LMB to assign weights for that bone.

Note

Only one bone selection at a time in this context.

Tip

Bones frequently hide inside geometry, becoming hard to click.
Activate In Front
to address this for the armature.

Missing a group when starting? Blender creates one automatically.

Symmetrical mesh + symmetrical armature? Use
Mirror Vertex Groups
to auto-generate groups and assignments on the other side.

### Vertex Groups for Particles

Weight painted particle emission.

Via Vertex Groups
in a particle system's configuration,
control density, length, etc. across mesh zones.

[Related references](INDEX.md).
