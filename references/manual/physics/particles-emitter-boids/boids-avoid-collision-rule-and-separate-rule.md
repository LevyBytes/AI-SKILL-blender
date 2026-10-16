# Boids: Avoid Collision Rule, Separate Rule, Flock Rule, Follow Leader Rule, Average Speed Rule, Fight Rule

### Avoid Collision Rule 

Prevents contact with Deflection-enabled geometries.

Boids

Mutual boid collision avoidance.

Deflectors

Avoidance of deflector geometries.

Look Ahead

The anticipation window in seconds.

### Separate Rule 

Boids increase separation from neighbors.

### Flock Rule 

Boids emulate neighbor motion while maintaining separation.

### Follow Leader Rule 

Boids pursue a leader object rather than another boid.

Distance

The positioning distance trailing the leader.

Line

Encourages linear leader pursuit formation.

Queue Size

The permissible boid count in linear formations.

### Average Speed Rule 

Boids preserve baseline velocity.

Speed

The target speed as a proportion of maximum capability.

Wander

The randomization magnitude applied to velocity orientation.

Level

The Z velocity component permanence degree.

### Fight Rule 

Boids advance toward neighboring boids.

Fight Distance

The maximum assault approach distance.

Flee Distance

The separation threshold during retreat.

In Air

This rule governs airborne behavior.

On Land

This rule governs ground behavior.

[Related references](INDEX.md).
