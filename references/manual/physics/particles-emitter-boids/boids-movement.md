# Boids: Movement

## Boids

### Boids 

Reference

Panel :

Particle System ‣ Physics

Type :

Boids

Boid Physics settings. 

Boid particle configurations operate under limited machine logic, programmable to heed fundamental behavioral guidelines. Ideal for recreating swarms, herds, schools of fauna or aquatic life, plus predator-prey dynamics. They respond to external objects and peer interactions. Boids absorb bounded information; therefore, Boid Brain rule ordering gains tremendous importance. In certain conditions, the system evaluates merely the foremost three parameters.

### Movement 

Reference

Panel :

Particle System ‣ Physics ‣ Movement

Boid Movement settings. 

Boids sidestep Collision-enabled entities, navigate toward mission targets, and escape from "predator" entities per Boid Brain logic. Flight versus ground locomotion shifts behavior characteristics.

Allow Flight

Grants airborne motion capability.

Allow Land

Grants terrestrial movement capability.

Allow Climbing

Activates goal-directed climbing.

Max Air Speed

The peak velocity boids attain during flight.

Min Air Speed

The threshold velocity boids preserve while airborne.

Max Air Acceleration

Governs how swiftly boids shift direction aloft, expressed proportional to peak velocity. Greater values enable sharper, more responsive aerial maneuvers.

Max Air Angular Velocity

Caps the turning rate of boids in flight as a percentage of 180 degrees. Lower magnitudes yield gradual arcs.

Air Personal Space

Airborne boid spacing radius as a percentage of body scale. Elevated values minimize crowding.

Landing Smoothness

Tunes touchdown softness. Higher settings produce gentle landings.

Max Land Speed

The peak velocity boids attain on terrain.

Jump Speed

The velocity magnitude boids achieve when leaving ground.

Max Land Acceleration

Governs how swiftly boids shift direction on terrain as a percentage of peak velocity.

Max Land Angular Velocity

Caps the turning rate of boids on ground as a percentage of 180 degrees. Lower values create fluid, unhurried turns.

Land Personal Space

Ground-based boid spacing radius as a percentage of body scale. Elevated values minimize congregation.

Land Stick Force

Governs the pressure needed to shift grounded boids. Lower magnitudes permit more spontaneous movement when responding to external forces.

Collision Collection

Filters collision engagement to a designated group exclusively. Beneficial for limiting interaction to target objects or surroundings.

[Related references](INDEX.md).
