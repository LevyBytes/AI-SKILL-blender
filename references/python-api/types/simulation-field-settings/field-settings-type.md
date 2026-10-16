# bpy.types.FieldSettings: type

type

Which kind of field this is (default 'NONE' )

- NONE
None.

- BOID
Boid – Make a force that behaves like a boid's predator or target.

- CHARGE
Charge – A spherical force field driven by particle charge, which only affects other charge force fields.

- GUIDE
Curve Guide – Make a force running along a curve object.

- DRAG
Drag – Make a force that slows motion down.

- `FLUID_FLOW`
Fluid Flow – Make a force derived from fluid-simulation velocities.

- FORCE
Force – A radial field pointing toward the object's center.

- HARMONIC
Harmonic – This force field originates at the zero point of a harmonic oscillator.

- LENNARDJ
Lennard-Jones – A force field built on the Lennard-Jones potential.

- MAGNET
Magnetic – A force field that responds to how fast the particles move.

- TEXTURE
Texture – A force field driven by a texture.

- TURBULENCE
Turbulence – Make turbulence from a noise field.

- VORTEX
Vortex – A spiraling force that twists about the force object's local Z axis.

- WIND
Wind – A steady force directed along the force object's local Z axis.

Type :

Literal[‘NONE’, ‘BOID’, ‘CHARGE’, ‘GUIDE’, ‘DRAG’, ‘`FLUID_FLOW`’, ‘FORCE’, ‘HARMONIC’, ‘LENNARDJ’, ‘MAGNET’, ‘TEXTURE’, ‘TURBULENCE’, ‘VORTEX’, ‘WIND’]

[Related references](INDEX.md).
