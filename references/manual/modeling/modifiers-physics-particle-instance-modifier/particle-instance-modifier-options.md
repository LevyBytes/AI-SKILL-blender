# Particle Instance Modifier: Options

## Particle Instance Modifier

### Particle Instance Modifier

Attach a Particle Instance modifier to an object and that object's mesh gets copied at every particle location belonging to the chosen particle system on a separate target object. So putting the modifier to use means you need at least one other object carrying a Particles System.

Since the Particle Instance modifier takes its cues from particle systems living on other objects, what it produces can look and act wildly different from case to case, hinging on how those underlying particle systems are set up. Bear that in mind any time the Particle Instance modifier's settings aren't giving you the results you were after.

### Options

The Particle Instance modifier.

Object
The target object that carries a particle system.

Particle System
Which of the target Object's particle systems this modifier acts on.

Create Instances

Regular
Switched on, the modifier copies the modified object's mesh onto the regular (parent) particles.

Children
Switched on, the modifier copies the modified object's mesh onto the child particles.

Size
Scales the instanced copies of the mesh by the particle's size attribute.
Switch it off and every copy comes out the same size as the original.

For the particle's size options, look to the particle system's Render
and Children panels.

Show

Unborn
Switched on, the modifier copies the modified object's mesh onto the unborn particles.

Alive
Switched on, the modifier copies the modified object's mesh onto the alive particles.

Dead
Switched on, the modifier copies the modified object's mesh onto the dead particles.

Amount
What fraction of the particles get used.
Lets you randomly drop particles to dial the instance count up or down.

Warning

As things stand the random algorithm only guarantees the relative amount statistically .
How many instances actually get made will stray from the theoretical figure,
governed by the Seed value of the target particle system (and the Offset value covered below, as well).

That gap stays minor when particle counts run high,
but it grows very obvious at low counts
(say the target system holds 100 particles and Amount is set to 0.1 :
you might end up with as many as 15 or as few as 5 instances rather than the 10 you'd expect).

Offset
A relative shift within the band of particles used for instancing.
Lets you keep the used particles from overlapping
when one particle system feeds several modifier instances.

Tip

To rule out overlaps entirely, set your Offset value no lower than your Amount value.

Coordinate Space

World, Local
Work in World Space, or in the Local Space of the target object the particle system sits on.

- World space means the copies of the modified mesh land at positions that depend
on where both the modified object and the target object are.

- Local space means the copies of the modified mesh land at positions that depend
on the modified object's location alone.

Axis
Picks which axis of the modified object serves as the pole axis for applying
the rotation taken from the instantiated particles.

[Related references](INDEX.md).
