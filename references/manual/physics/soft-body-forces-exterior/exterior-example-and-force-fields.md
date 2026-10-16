# Exterior: Example, Force Fields, Soft Body Field Weights, Aerodynamics, Goal

## Exterior

### Exterior 

External forces apply to soft-body vertices (nearly exclusively).
Newton's Laws govern behavior:

- Unforced vertices remain stationary or move at constant velocity.

- Acceleration depends on mass and force magnitude. Heavier mass causes slower acceleration; larger forces yield greater acceleration.

- Every action has equal opposite reaction.

Computing introduces damping to prevent overshoot.

### Example 

Start with a default cube.

- Disable Goal initially to prevent vertex return to original positions, isolating external-force effects.

- Begin playback.

What occurs? The cube moves downward (negative Z).
Eight vertices experience constant global gravitation.
Gravity without friction proves mass-independent, so all soft-body objects fall identically.
The cube resists deformation because all vertices move identically.

### Force Fields 

Soft body vertices interact with all Force Fields applied (typically to particles): wind, force fields, physics field effects on shared layers.

### Soft Body Field Weights 

Reference

Panel :

Physics ‣ Soft Body ‣ Field Weights

The Soft Body Field Weights panel controls external force-field influence magnitude.

Effector Collection
Restricts effectors to a specified group. Only effectors in this group affect the current system.

Gravity
Adjusts Global Gravity influence.

All
Scales all effector weights.

### Aerodynamics 

Edges respond to wind, fluttering and sailing in breezes.
A flag catching wind demonstrates simple aerodynamics.

This specialized exterior force applies to edges, not vertices.
Technically, perpendicular-to-edge force applies.
Force scales with relative-speed projection along the edge (dot product).
Wind blowing and dragging an edge through air at identical speed produce equal force. An edge moving along itself experiences zero force; perpendicular motion experiences maximum force.

Angle and relative speed between medium and edge determine force.
This causes vertices with few edges (plane front) falling faster than those with many (plane center).
Identical edge counts per direction produce equal fall speed.

Soft Body Edges panel contains Aerodynamics settings.

### Goal 

A "goal" represents the target shape a soft body attempts to match.
It acts like a pin on specific vertices, controlling soft-body influence magnitude.

Enabling Soft Body Goal uses vertex position (including animation) in simulation.
Animate vertices through standard methods (F-Curves, armatures, parents, lattices, etc.) before soft-body simulation.
The "goal" specifies desired vertex position.
How strongly the soft body pursues this goal uses stiffness and damping controls.

See Goal Settings for details.

[Related references](INDEX.md).
