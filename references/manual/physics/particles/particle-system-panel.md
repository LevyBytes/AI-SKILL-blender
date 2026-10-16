# Particle System Panel

## Particle System Panel

### Particle System Panel 

Reference

Panel :

Particle System ‣ Particle System

Particle System panel. 

These are the fundamental settings.

Active Particle System
The object's Particle Modifier(s) in list view.

Specials

Copy Active to Selected Objects
Duplicates the active particle system onto all selected objects.

Copy All to Selected Objects
Transfers all particle systems from the active object to all selected objects.

Duplicate Particle Systems
Replicates the particle system within the object.
Checking Duplicate Settings (in Adjust Last Operation) replicates settings too, giving the new system independent parameters.

Remove All Particle Systems
Eliminates all particle systems in the object.

Particle Settings
Data-Block selector for settings.

Type
Fundamental system-type selector.

Emitter
Particles originate from the object.

Hair
Strand-based hair rendering.

Regrow
Regenerates hair each frame, beneficial when animating properties.

Advanced
Unlocks advanced settings matching Emitter mode behavior.

Note

This manual assumes this option is enabled.

Segments
Specifies strand segment count.
Higher values enhance animation quality.

### Workflow 

Standard particle system workflow:

- Create the emitting mesh.

- Initialize one or more Particle Systems from the mesh. Multiple systems typically overlap or merge for the desired combined effect.

- Configure each system's parameters.

- Animate the emitter and other scene meshes.

- Define and refine particle flow and direction.

- For Hair systems: sculpt the emitter's appearance (cut hair length, comb, etc.).

- Perform final rendering and physics simulation, adjusting as needed.

### Creating a Particle System 

Adding a particle system. 

Attach a particle system to an object via the Particles tab in the Properties editor—click the button. An object may host numerous Particle Systems.

Each system maintains separate settings. Systems can share settings, avoiding manual duplication and enabling the same effect across multiple objects.

#### Types of Particle Systems 

Particle System Types. 

After initialization, the Properties panel fills with numerous controls.
Don't panic—two distinct particle system types exist, selectable via Type: Emitter and Hair.

Particle System tab settings vary partially by system type.

[Related references](INDEX.md).
