# bpy.types.ParticleSystem: methods

co_hair ( object , * , particle_no = 0 , step = 0 )

Read back cached hair data

Parameters :

- object (Object) – Object (never None)

- particle_no ( int ) – Particle no, (in [-inf, inf], optional)

- step ( int ) – step no, (in [-inf, inf], optional)

Returns :

Co, Exported hairkey location (array of 3 items, in [-inf, inf])

Return type :

mathutils.Vector
uv_on_emitter ( modifier , particle , * , particle_no = 0 , uv_no = 0 )

Read back the uv for every particle

Parameters :

- modifier (ParticleSystemModifier) – Particle modifier (never None)

- particle (Particle) – Particle (never None)

- particle_no ( int ) – Particle no, (in [-inf, inf], optional)

- uv_no ( int ) – UV no, (in [-inf, inf], optional)

Returns :

uv, (array of 2 items, in [-inf, inf])

Return type :

mathutils.Vector
mcol_on_emitter ( modifier , particle , * , particle_no = 0 , vcol_no = 0 )

Read back the mcol for every particle

Parameters :

- modifier (ParticleSystemModifier) – Particle modifier (never None)

- particle (Particle) – Particle (never None)

- particle_no ( int ) – Particle no, (in [-inf, inf], optional)

- vcol_no ( int ) – vcol no, (in [-inf, inf], optional)

Returns :

mcol, (array of 3 items, in [0, inf])

Return type :

mathutils.Color
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
