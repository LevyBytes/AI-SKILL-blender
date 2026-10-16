# Introduction

### Introduction 

Rigid body simulation models solid object motion, affecting position and orientation without deformation.

Unlike other Blender simulations, rigid body systems integrate closely with the animation framework.
This enables rigid bodies to behave like standard objects within parent-child relationships, animation constraints, and drivers.

### Creating a Rigid Body 

Reference

Mode :

All Modes

Panel :

Properties ‣ Physics ‣ Rigid Body

Menu :

Object ‣ Rigid Body

Only mesh objects participate in rigid body simulation.
Create rigid bodies via the Rigid Body button in Physics properties or through Add Active / Add Passive in Object ‣ Rigid Body.

Two rigid body types exist: active (dynamically simulated) and passive (animation-controlled). Both support the Animated option for animation-system control.

During simulation, the rigid body system overrides position and orientation of dynamic objects.
However, object location and rotation values remain unchanged—the simulation acts like a constraint.
Use Apply Object Transform to make rigid body transformations permanent.

The object's scale influences simulation but stays under animation control.

Remove rigid body physics via the Rigid Body button in Physics properties or Object ‣ Rigid Body.

### Working with Rigid Bodies 

Multiple object operators support rigid body workflows, available in the Rigid Body menu.
These include functions to add/remove rigid bodies, adjust properties, and add Rigid Body Constraints.

[Related references](INDEX.md).
