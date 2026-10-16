# Goal

## Goal

### Goal 

Reference

Panel :

Physics ‣ Soft Body ‣ Goal

This enables Blender to incorporate animation (F-Curves, armatures, parents, lattices, etc.) into simulation.
The "goal" represents the animation-driven desired vertex position.

See exterior forces for details.

Vertex Group
Allows per-vertex goal weights, multiplying the Default goal.

### Settings 

Stiffness
Spring stiffness for Goal. Lower values create weak springs (flexible attachment); higher values create strong springs (stiff attachment).

Damping
Goal friction. Higher values dampen spring effects (reduced jiggle), ending motion quickly.

### Strengths 

Default
Goal weight/strength for all vertices without a Vertex Group.
With a vertex group, vertex weight specifies its goal.

Min/Max
Fine-tune vertex group weights via clamping.
Lowest vertex weight becomes Minimum; highest becomes Maximum.

[Related references](INDEX.md).
