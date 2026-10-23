# Particle Info Node

## Particle Info Node

### Particle Info Node

*Cycles Only*

Retrieve particle data for instancing objects in Object or Collection Render mode. Adds variation to materials on instanced objects by accessing parent particle information.

Note: Currently supports parent particles only; child particle info is unavailable.

### Inputs

None.

### Properties

None.

### Outputs

- **Index**: Particle number (0 to particle count).
- **Random**: Per-particle random (0 to 1). Use with color ramps for color randomization.
- **Age**: Particle age in frames.
- **Lifetime**: Total lifespan in frames.
- **Location**: Particle position.
- **Size**: Particle size.
- **Velocity**: Particle velocity.
- **Angular Velocity**: Particle rotation rate.

[Related references](INDEX.md).
