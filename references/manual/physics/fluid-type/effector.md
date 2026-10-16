# Effector

## Effector

### Effector 

Effector objects direct and shape fluid behavior. To designate a mesh object as an effector, navigate to Properties ‣ Physics and click Fluid, then choose Effector as the fluid Type.

Tip

Force Fields

(such as wind or vortex) integrate with the system like other physics setups. Control over individual force type influence happens through domain object settings.

### Settings 

Reference

Panel :

Physics ‣ Fluid ‣ Settings

Type :

Effector

Effector Type

Collision :

Such objects interact with fluids through contact.

Guide :

These objects' velocity gets transferred during guiding bakes. Guiding effectors must move and possess velocity.

Velocity Factor

Multiplies guiding object velocities by this amount. Useful when coordinating multiple guiding objects with varying speed requirements.

Guide Mode

Specifies how guiding velocities merge into the global domain velocity field.

Maximize :

The guiding object compares its velocity magnitude against the field. When its absolute value exceeds the field's absolute value, its guiding velocity persists.

Minimize :

The guiding object compares its velocity magnitude against the field. When its absolute value falls below the field's absolute value, its guiding velocity persists.

Override :

The most straightforward approach. Guiding objects continuously replace the global guiding velocity field with their current velocity. Previous frame values or velocities from other guiding objects get superseded.

Averaged :

The guiding object writes the mean of its velocity and existing field velocity into the global guiding velocity field.

Sampling Substeps

Specifies how many substeps reduce gaps in fluid collision from quickly moving effectors.

Surface Thickness

Extends the effector region by this distance, expanding its interactive area.

Use Effector

Toggles whether the effector influences the fluid. This property facilitates animations that selectively engage or disengage effector impact.

Is Planar

Marks the effector as either a single-dimension object (such as a plane) or Non-manifold geometry. This declaration ensures accurate fluid simulation on these mesh types.

A manifold mesh can also be flagged as planar. The solver then disregards internal volume and treats the mesh sides as fluid emission boundaries.

[Related references](INDEX.md).
