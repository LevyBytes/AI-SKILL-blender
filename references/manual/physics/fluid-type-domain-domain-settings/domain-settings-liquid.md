# Settings: Liquid

### Liquid 

Reference

Type :

Domain

Panel :

Physics ‣ Fluid ‣ Liquid

Liquid settings govern the particles that comprise the simulation. Enabling the liquid checkbox automatically generates a particle system to visualize the simulation's flow. Displaying liquid particles remains optional; the simulation utilizes all fields regardless of whether an attached particle system exists.

Note

Unchecking the liquid checkbox removes the associated particle system and its configuration.

Simulation Method

Determines which particle simulation method governs the liquid behavior.

FLIP :

(FLuid Implicit Particle)
Generates highly splashy simulations with numerous particles suspended in air.

APIC :

(Affine Particle-In-Cell)
Yields an energetic yet more balanced simulation. This method retains vortices better compared to FLIP.

FLIP Ratio Simulation FLIP Only :
Specifies what proportion of FLIP velocity influences updates to liquid particle velocities. A setting of 1.0 enforces purely FLIP-based behavior. Entirely FLIP-based simulations exhibit more chaotic splashes and work well for large liquid volumes. Lower values produce less turbulent behavior with gentler splashes, making them suitable for small-scale scenarios.

System Maximum

Caps the total fluid particles allowed within the simulation. When nonzero, the simulation respects this limit. At zero, the solver continuously samples new particles as needed.

Particle Radius

Specifies the radius of an individual liquid particle in grid cell units. This dimension indicates the coverage area of each particle and determines how much surrounding space qualifies as liquid. Larger radii expand the coverage area, causing more grid cells to register as liquid rather than empty space.

When simulations leak or produce unphysical volume changes, this value warrants adjustment. Increasing it addresses disappearing liquid, while decreasing it handles excess production.

Sampling

Multiplier that determines particle sampling quantity. Higher settings yield more particles. Resampling occurs at every simulation substep.

Randomness

New particles receive randomized positioning within their source regions, with this field controlling the degree of randomization. Higher values generate particles with greater positional variation at inflow sites. A zero setting places all new particles uniformly throughout their grid cells.

This parameter proves valuable when establishing laminar inflows with minimal variation or turbulent flows with pronounced variation.

Particles Maximum

Establishes the upper particle count per grid cell. As simulation progresses, cell particle populations fluctuate through movement and removal. Resampling adds particles within this constraint.

This threshold indicates the peak particles per cell and facilitates pre-bake estimation of total particle count (grid resolution also factors into this calculation).

Minimum

Sets the lower particle count threshold per grid cell. Similar to the maximum value, this ensures each cell maintains a baseline particle population.

Narrow Band Width

Establishes the span in grid cell units of the narrow band confining liquid particles. Increased values thicken the band and may saturate inflow regions with particles. Unless particle visualization forms the primary objective, keeping the band narrow proves beneficial, since extra particles reduce simulation speed.

Increasing this value sometimes restores volume in leaking simulations. Otherwise, optimal performance results from the narrowest feasible band, as the liquid surface concentrates most geometric detail and computing resources are better spent there.

See also

The narrow band references Narrow Band FLIP for Liquid Simulations.

Fractional Obstacles

Activates higher resolution handling at fluid and obstacle boundaries, implementing second-order obstacle treatment. This reduces stepping artifacts that appear when inclined obstacles sit within the domain. Liquid movement flows more uniformly across obstacle surfaces.

Obstacle Distance

Determines the separation between fluid and obstacles. Increased values facilitate smoother liquid passage over inclined surfaces, with the adjustment depending on obstacle slope. Negative values permit fluid to penetrate obstacle interiors.

Obstacle Threshold

Manages the smoothness of fractional obstacle behavior. Lower values diminish stepping artifacts but risk particles adhering to obstacle surfaces.

Bake Data, Free Data

Available exclusively with Modular cache type. Bake Data calculates and archives the simulation foundation to disk. Both gas and liquid systems can layer refinements atop this base (noise for gas, mesh or secondary particles for liquids, or both).

The status bar displays progress. Pressing Esc pauses the simulation.

After completing the simulation bake, the cache becomes removable through Free Data. Bake All operations support pause and resume functionality.

[Related references](INDEX.md).
