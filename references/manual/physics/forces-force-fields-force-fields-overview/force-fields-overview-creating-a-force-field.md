# Introduction: Creating a Force Field

### Introduction 

Force fields provide mechanisms to shape simulation behavior, introducing additional motion. Particles, Soft Bodies, Rigid Bodies, and Cloth entities all respond to force field influence. Force fields automatically affect compatible systems. Remove specific simulations or particle systems from their reach by reducing that force field type's influence through the Field Weights panel.

- Objects and particles of any type generate fields, yet only curve objects can produce Curve Guide fields.

- Particles themselves can generate force fields. Refer to Particle Physics.

- Objects need to occupy a shared layer to exert reciprocal effects.

You can constrain field influence on particles to specified object groups (consult Particle Physics documentation).

### Creating a Force Field 

Reference

Mode :

Object Mode

Menu :

Add ‣ Force Field

Panel :

Physics ‣ Force Field

To establish a force field instance, navigate to Add ‣ Force Field and select the desired type. This approach generates an empty object with the field attached.

| Description | Description | Description |
| --- | --- | --- |
| Vortex: force field.  | Wind: force field.  | Force: force field.  |

Starting with an existing object, navigate to the Physics tab and select the field category from the Fields menu to attach a field to that object.

Note

Recalculation of particle, soft body, or cloth systems becomes necessary after modifying Fields or Collision settings, accomplished by accessing Free Cache. This does not happen automatically.

Particles interact with any force field type. Soft bodies respond exclusively to Force, Wind, and Vortex (Harmonic fields have minimal useful effect on soft bodies).

[Related references](INDEX.md).
