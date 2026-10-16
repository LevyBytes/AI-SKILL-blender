# Cloth Filter

## Cloth Filter

### Cloth Filter

Reference

Mode :

Sculpt Mode

Tool :

Toolbar ‣ Cloth Filter

This tool mirrors the Cloth Brush behavior but applies cloth physics to all mesh vertices at once. Drag away from the object for positive effect or toward for negative effect.

Tip

Vertices can be "pinned" by masking regions that should stay stationary, or by using Face Sets.

### Tool Settings

Filter Type
Determines which operation gets applied to the mesh.

Gravity :

Applies gravitational force to the simulation.

Inflate :

Expands the fabric outward.

Expand :

Extends the fabric dimensions outward.

Pinch :

Compresses the fabric toward the cursor position where the operation started.

Scale :

Resizes the mesh using Soft Body dynamics, scaling based on distance from the object origin. This creates surface undulations. Control undulation orientation using Force Axis and Orientation settings.

Strength
Controls the intensity of the filter's effect on the mesh.

Force Axis
Restrict force application to a specific axis.

Orientation
Sets the axis alignment for force limitation.

Local :

Apply force and gravity along local axes.

World :

Apply force and gravity using global axes.

View :

Apply force and gravity relative to viewport orientation.

Cloth Mass
Mass value per simulation node.

Cloth Damping
How readily applied forces distribute through the cloth.

Use Face Sets
Restricts cloth forces to vertices within the Face Set under the mouse cursor.

Use Collisions
Activates collision detection with other scene objects during simulation. For the sculptable mesh to collide, the other object must have Collision Physics enabled.

[Related references](INDEX.md).
