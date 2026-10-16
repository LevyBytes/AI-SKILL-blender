# Emission: Particle System ‣ Emission, Particle Emission settings.

## Emission

### Emission 

Reference

Panel :

Particle System ‣ Emission

The Emitter system operates as its designation suggests: it produces particles across a time window. Particles discharge from the target object beginning at Start through End frames, possessing specified lifespan duration. Rendering defaults to Halos, though configuration allows object-based rendering (based on particle system render settings, see Visualization).

Particle Emission settings. 

The Emission panel buttons manage temporal particle generation patterns:

Number

The aggregate of parent particles deployed in the simulation.

Seed

Blender applies this as the initialization point for random number production throughout the simulation.

Frame Start

The initiation frame for particle release. Negative values initiate simulation before actual rendering commences.

End

The termination frame for particle release.

Lifetime

The duration (in frames) each particle persists.

Lifetime Randomness

Random variation in individual particle lifetimes. Shortest potential lifetime calculates as Lifetime × (1 - Random). Values exceeding 1.0 are prohibited. Illustration: with standard Lifetime of 50 and Random at 0.5, particles exist between 50 frames and \\(50 × (1.0 - 0.5) = 25\\) frames. At Random 0.75, lifespans range from 50 to \\(50 × (1.0 - 0.75) = 12.5\\) frames.

[Related references](INDEX.md).
