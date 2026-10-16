# Boids: Goal Rule, Avoid Rule, Avoid Collision Rule, Separate Rule, Flock Rule, Follow Leader Rule, Average Speed Rule

### Goal Rule 

Navigate toward designated target.

Object

Identifies the goal reference. Defaults to negatively-charged Boid force fields without specification.

Predict

Estimates target trajectory.

### Avoid Rule 

Retreat from adversaries.

Object

Identifies the avoidance reference. Defaults to positively-charged Boid force fields without specification.

Predict

Estimates adversary trajectory.

Fear Factor

Evasion commences when threat level surpasses this value.

### Avoid Collision Rule 

Prevents Deflection-configured obstacles.

Boids

Prevents boid-boid contact.

Deflectors

Prevents contact with deflector surfaces.

Look Ahead

The temporal forecast window (seconds).

### Separate Rule 

Boids maintain interpersonal distance.

### Flock Rule 

Boids mimic neighboring motion while maintaining interpersonal spacing.

### Follow Leader Rule 

Boids pursue a leader entity instead of another boid.

Distance

The following distance position relative to the leader.

Line

Establishes linear pursuit arrangement.

Queue Size

The maximum linear follower count.

### Average Speed Rule 

Boids keep baseline movement rate.

Speed

The velocity goal expressed as a percentage of capability.

Wander

The arbitrary change magnitude in movement orientation.

Level

The degree that vertical movement stays consistent.

[Related references](INDEX.md).
