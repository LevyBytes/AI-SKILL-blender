# Explode Modifier

## Explode Modifier

### Explode Modifier

By shifting and spinning its faces so they loosely trail the particles its object throws off, the Explode modifier rearranges the mesh geometry, selling the illusion that the mesh is blowing apart, broken up and flung outward.

Nothing shows up from the modifier unless the object it's on has a particle system, since that system is what powers the explosion.

The granularity of the Explode modifier rides on two things together: how many particles get emitted and how many faces there are. Push either one up and you wind up with more separate fragments.

There's a
demo video
that runs through a cube carrying a particle system and an Explode modifier.
(blend-file).

Note

In the stack, place the Explode modifier below the Particle System one,
so the former can pull the data it needs from the latter.

### Options

The Explode modifier, with a Particle System above it.

Particle UV
When set, the U coordinate in that UV Map gets overwritten
with the age of the particle tied to the matching mesh face
(scaled from 0 for particles not yet born up to 1 for dead ones).

The V coordinate is pinned at a flat 0.5.

You could, for instance, shift a fragment's (face's) color across the explosion
by feeding it a texture whose color gradient runs along the U axis.

Show

Unborn
Reveals faces while their attached particles are still unborn.

Alive
Reveals faces while their attached particles are alive.

Dead
Reveals faces while their attached particles are dead.

Cut Edges
Splits the mesh by where particles emit rather than along the existing faces.
The break this gives tends to read as more random.

Size
Once a particle is alive, its size is used to scale the face it's attached to.

Vertex Group
Vertices placed in this group can be spared from the Explode modifier.
At full weight a vertex isn't touched at all,
whereas a lower weight raises the odds of it being affected.

Vertices at zero weight are treated as though they weren't in the group at all,
and explode as normal.

Invert
Flips which vertices the chosen vertex group covers, so the group instead
marks the vertices the modifier will leave undeformed.

The group's weight values are reversed by this setting.

Protect
Tidies the vertex group edges. According to the weights given to that vertex group, it
either shields those faces entirely from the Explode modifier
(which is what a face weight of 1 produces),
or strips protection from them altogether
(which is what a face weight of 0 produces).

Refresh
Reloads the data held in the Explode modifier.

### Known Limitations

### Dynamic Vertex Weights

The vertex weights this modifier draws on are the initial ones.
Modifiers that change weights on the fly won't sway the explosion, since these values are read just once.

[Related references](INDEX.md).
