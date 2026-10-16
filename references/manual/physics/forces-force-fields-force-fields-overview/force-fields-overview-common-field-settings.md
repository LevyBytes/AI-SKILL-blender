# Introduction: Common Field Settings

### Common Field Settings 

Most fields share identical settings, despite their different mechanisms. Field-specific configurations appear below. Curve Guide and Texture fields employ substantially different interfaces.

Shape

Determines the direction applied to compute effector force. Empty object fields support Point, Line, and Plane shapes, while 3D object fields additionally feature Surface and Every Point, plus Curve for curve objects.

Point :

Omnidirectional influence radiating from the object origin.

Line :

Force operates only within the local XY plane, utilizing the Z axis as the effector.

Plane :

Force affects solely the local Z direction, employing the XY plane as the effector.

Surface :

Force field acts on 3D object surfaces, where the Z axis represents the surface normal.

Every Point :

Each mesh vertex contributes independently as an effector point.

Strength

The intensity of field influence. Positive and negative values reverse the force direction. A force field's strength scales with the object's scale, enabling proportional scene adjustment.

Flow

Introducing nonzero values adds drag force proportional and opposite to point velocity. This reinterprets the force field so the Strength to Flow ratio at any location specifies the velocity of an "air flow" field, with objects drawn toward the flow through drag resistance.

Affect

Location
Influence the position of particles and additional physics entities.

Rotation
Influence the rotation of particles with Dynamic Rotation enabled. Not applicable to other physics systems.

Deactivating both options completely suppresses field influence.

Noise Amount

Adds random variation to force magnitude.

Seed

Determines the randomness seed for noise generation.

Absorption

Force dissipates when collision objects obstruct it.

Wind Factor

Specifies force reduction when directed parallel to a surface, such as cloth. At 1, only the normal component contributes.

[Related references](INDEX.md).
