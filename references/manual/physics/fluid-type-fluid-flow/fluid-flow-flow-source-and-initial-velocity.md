# Flow: Flow Source, Initial Velocity, Texture

### Flow Source 

Flow Source

Specifies the mechanism for fluid discharge.

Mesh :

Fluid releases directly from the object's mesh surface.

Is Planar

Marks the effector as either a single-dimension object (such as a plane) or Non-manifold geometry. This declaration guarantees accurate fluid simulation on these configurations.

Surface Emission

Sets the maximum voxel distance from mesh surface where fluid gets released. Since voxel-based calculation applies, results vary with domain resolution.

Volume Emission Fire or Smoke Only :
Specifies the fluid fraction to emit within the emitter mesh, with 0 as none and 1 as complete. Emitting fluid based on volume produces unpredictable outcomes when mesh topology lacks proper connectivity.

Particle System :

Fire or Smoke Only :
Generates smoke or fire from a particle system linked to the flow object.

Particle system selection uses a Data ID reference.

Note that only Emitter-type particle systems produce smoke. Consult Particles for particle system creation guidance.

Set Size

When activated, the Size parameter limits maximum voxel distance for particle-based smoke emission, mirroring Surface Emission behavior for mesh sources. Deactivated, particles fill the nearest voxel entirely.

### Initial Velocity 

When enabled, the fluid inherits the momentum of its source.

Source

Multiplier for inherited velocity. A value of 1 emits fluid at source speed.

Normal

Governs how much velocity fluid receives along a face Normal. Initial velocities always distribute along all face normals regardless of this setting. Thus, closed flow source geometry releases fluid in multiple directions. Achieving single-direction emission requires all normals pointing identically. A plane flow object accomplishes this naturally.

Initial X, Y, Z

Velocity components along X, Y, Z axes in world coordinate space. These augment velocity along the Normal direction.

### Texture 

Reference

Type :

Flow

Panel :

Physics ‣ Fluid ‣ Settings ‣ Texture

When activated, the specified texture and accompanying configuration control smoke or fire emission zones on the mesh. These parameters do not affect Outflow Flow Behavior.

Texture

A Data ID reference for the texture selection.

Mapping

Determines whether Generated UVs or explicit UV mapping governs texture application.

Size

Controls overall texture scaling.

Offset

Displaces the texture along the Z direction.

[Related references](INDEX.md).
