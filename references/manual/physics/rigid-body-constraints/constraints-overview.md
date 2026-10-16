# Introduction

### Introduction 

Rigid body constraints (also termed joints) couple two rigid bodies.
Physics constraints attach to Empty objects, with fields pointing to the constrained physics-enabled objects.

The Empty hosting the constraint provides a location and axis set distinct from the two objects. Its position marks the constraint location; its axes define the constraint orientation.
These two anchor points establish themselves at animation start and stay fixed in each object's local space throughout the animation.
Objects move freely from the constraint, yet constraint anchors travel with them.
For greater freedom, use multiple objects with non-physics Child of constraints and animate relative positioning.

### Connect 

The quickest constraint approach involves selecting two objects and clicking Connect in Object ‣ Rigid Body.
This generates an empty object (labeled "Constraint") with physics constraint already targeting both objects.

### Physics Menu 

Alternatively, create Rigid Body Constraint on one of the constrained objects using the Physics tab.
This constraint depends on the object's position and orientation—the object itself provides the constraint anchor, eliminating empty-object creation.
Setting the constrained object as Passive type improves constraint control.

The Rigid Body Constraint panel appears in the Physics tab for the selected empty or the one constrained object with the created constraint.

### Common Options 

Reference

Panel :

Physics ‣ Rigid Body Constraint

### Settings 

Enabled
Toggles constraint activity during simulation.

Disable Collisions
Allows constrained objects to interpenetrate.

Breakable
Allows constraint failure during simulation (unavailable for Motor constraints).
Enables destruction simulation.

Threshold
Impulse magnitude required for constraint failure.

### Limits 

Limits constrain objects further by specifying translation/rotation ranges on one axis. Set both limits to 0 to lock an axis.

### Objects 

First
Primary constrained object.

Second
Secondary constrained object.

### Override Iterations 

Makes constraints stronger (higher iterations) or weaker (lower iterations) than the rigid body world specification.

Iterations
Constraint solver iterations per simulation step for this constraint.

[Related references](INDEX.md).
