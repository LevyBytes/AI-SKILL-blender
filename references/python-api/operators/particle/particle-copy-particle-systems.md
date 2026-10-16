# bpy.ops.particle.copy_particle_systems

bpy.ops.particle. copy_particle_systems ( * , space = 'OBJECT' , remove_target_particles = True , use_active = False ) 

Transfer particle systems from the selected active object to other chosen objects

Parameters :

- space ( Literal [ 'OBJECT' , 'WORLD' ] ) – Space, Space transform for copying from one object to another (optional)

- OBJECT
Object – Copy inside each object's local space.

- WORLD
World – Copy in world space.

- remove_target_particles ( bool ) – Remove Target Particles, Remove particle systems on the target objects (optional)

- use_active ( bool ) – Use Active, Use the active particle system from the context (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
