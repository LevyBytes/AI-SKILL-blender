# Keyed

## Keyed

### Keyed 

Reference

Panel :

Particle System ‣ Physics

Type :

Keyed

Keyed particles traverse paths determined by multiple particle systems. This enables constructing chains building extended strands or flowing animated sequences. Particles lack internal dynamics; interpolation between successive systems each frame governs movement.

Keyed setup demands a minimum of two particle system entries in the Keys register.

### Options 

Keyed Physics settings. 

Loops

Specifies how many times the complete Keys register cycles. Disabled upon Use Timing activation.

Use Timing

This option permits specifying individual timing for separate keys using Time and Duration controls. Without activation, particles traverse all keys over their lifespan. Shorter lifespans accelerate motion. The lifetime divides equally across keys, sometimes producing uneven inter-target speeds.

### Relations 

Reference

Panel :

Particle System ‣ Physics ‣ Relations

Key Targets

The Keys sequence (target particle system list view).

Object

A target object label for the chosen key. If blank, the current particle system gets used.

System

The target object's particle system position.

Time

The frame number marking particle arrival at the selected system site. The Keyed system Start frame offsets this calculation.

Duration

The timespan (in frames) particles remain at the system before advancing to the next.

[Related references](INDEX.md).
