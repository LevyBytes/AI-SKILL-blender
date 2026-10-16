# bpy.types.FluidDomainSettings: sndparticle_combined_export

sndparticle_combined_export

Sets which particle systems get built from the secondary particles (default 'OFF' )

- OFF
Off – Create a separate particle system for every secondary particle type.

- `SPRAY_FOAM`
Spray + Foam – Spray and foam particles are saved in the same particle system.

- `SPRAY_BUBBLES`
Spray + Bubbles – Spray and bubble particles are saved in the same particle system.

- `FOAM_BUBBLES`
Foam + Bubbles – Foam and bubbles particles are saved in the same particle system.

- `SPRAY_FOAM_BUBBLES`
Spray + Foam + Bubbles – Create one particle system that contains all three secondary particle types.

Type :

Literal[‘OFF’, ‘`SPRAY_FOAM`’, ‘`SPRAY_BUBBLES`’, ‘`FOAM_BUBBLES`’, ‘`SPRAY_FOAM_BUBBLES`’]

[Related references](INDEX.md).
