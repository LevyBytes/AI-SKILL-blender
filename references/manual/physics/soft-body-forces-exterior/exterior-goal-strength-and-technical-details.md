# Exterior: Goal Strength, Technical Details

### Goal Strength 

Goal Strength defines animation-system influence magnitude.

Goal = 1.0 means no soft body—the object behaves as regular animated object (vertex stays at original position).
Goal = 0.0 (no goal) means vertices respond only to physical laws.

Goal values between 0.0 and 1.0 blend animation and soft-body effects.

Goal serves as memory, preventing excessive deformation from the unannotated soft-body state.
Vertex Group weight system defines per-vertex Goal weight. Weight Paint frequently adjusts these comfortably.
Non-mesh objects use control-point weights instead; use Edit Mode context menu or Sidebar Transform panel.
Hair particle weights paint in Particle Edit Mode.

### Technical Details 

Soft-body mesh vertices function as mass-bearing particles.
Forces determine movement. Particles interact along edges using physical models resembling automotive shock absorbers:

- A spring maintains specific particle distance.
Soft body parameter Stiffness controls spring effort.

- Damping dampens movement.
Soft body parameter Damping controls resistance.

[Related references](INDEX.md).
