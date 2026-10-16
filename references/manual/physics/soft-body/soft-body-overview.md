# Introduction

### Introduction 

Soft-body simulation models deformable-object behavior.
Originally designed for secondary-motion animation—character body jiggle—it extends to general soft objects that bend, deform, and respond to forces: gravity, wind, object collisions.

While soft-body simulation handles cloth to an extent, Cloth Simulation excels with dedicated solvers.

The simulation combines existing animation with acting forces—external (gravity, force fields) and interior (vertex connection forces).
This generates realistic object shapes as though possessing volume, internal fill, and external force effects.

Soft bodies interact with objects via Collision and with themselves via Self-Collision.

Convert soft-body simulation results to static objects or edit intermediate results and continue simulation.

### Typical Scenarios for using Soft Bodies 

The wind cone is a soft body, as the suspension. 

Animation

Soft bodies excel at:

- Character body jiggle.

- Elastic, deformable rubber or gelatin objects.

- Wind-blown tree branches, swinging ropes, etc.

- Flags, flowing sleeves, cushions, and fabric reacting to forces.

### Creating a Soft Body 

Soft-body simulation applies to objects with vertices or control points: meshes, curves, surfaces, lattices.

Activate soft-body simulation via Physics tab's Soft Body button.
Reference all settings here.

Start simulation with Alt - A playback; stop with Esc or Alt - A.

### Interaction in Real-Time 

The Timeline editor facilitates soft-body work.
Switch between frames; simulation displays current state.
Real-time interaction occurs: move collision objects, shake soft bodies.

While simulating, select the soft body and Apply the modifier in Properties Modifiers to permanentize deformation.

### Tips 

- Even vertex distribution optimizes soft bodies.
Sufficient vertices enable good collision. Add vertices in regions affecting stiffness deformation.

- Collision calculation may prove expensive. Skip invisible calculations.

- Accelerate collision calculation with simplified additional invisible larger objects.

- Apply soft bodies selectively.
Tight-cloth animation via soft-body alone typically fails. Self-collision for soft-body hair activates but requires careful handling.
Collisions appear later.

- Lattice or Curve Guide soft bodies often outpace object soft bodies significantly.

[Related references](INDEX.md).
