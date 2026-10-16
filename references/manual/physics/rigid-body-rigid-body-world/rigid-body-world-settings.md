# Rigid Body World: Settings

## Rigid Body World

### Rigid Body World 

Reference

Panel :

Scene ‣ Rigid Body World

The Rigid Body World groups rigid body objects, holding settings applicable to all.

When rigid body physics gets added, the system creates a group—default name "RigidBodyWorld".
Rigid body objects join this group automatically.
Multiple Rigid Body World Collections exist; allocate bodies via the Collections panel.

Rigid body objects and constraints participate in simulation only when in the collection specified by Rigid Body World's Collection field.

### Settings 

Rigid Body World
Enable/disable rigid body simulation evaluation for participating objects in the specified collection.

Remove Rigid Body World
Eliminate rigid body simulation from the scene.

Collection
The collection housing rigid body objects in this simulation.

Constraints
The collection housing rigid body constraints in this simulation.

Simulation quality and timing:

Speed
Adjusts simulation tempo.

Split Impulse
Enable/disable reduction of extra velocity accumulating on collision.
(Reduces stability slightly; use when necessary.)
Limits collision-separation force, producing nicer results but reduced stability (especially with many stacked objects).

Substeps Per Frame
Simulation steps per frame (higher values increase accuracy at the cost of speed).
Affects accuracy only, not speed.

Solver Iterations
Constraint solver iterations per step (higher values increase accuracy at the cost of speed).
Higher iterations stabilize constraints and stacking.

[Related references](INDEX.md).
