# Collisions: Object Collisions, Self-Collisions

## Collisions

### Collisions

Reference

Panel :

Physics ‣ Cloth ‣ Collision

Fabric almost never floats isolated in space—it encounters other scene objects. Proper setup requires several interdependent components:

- The Cloth object must be configured to take part in collision detection.

- Optionally (though recommended) permit cloth to collide with itself.

- Other interacting objects must be visible to the Cloth object via shared layers.

- Other objects must be mesh-type.

- Other objects may move or be deformed by agents (armatures, shape keys).

- Other mesh objects must be enabled to deflect the cloth.

- The .blend file must be saved allowing simulation data storage.

- Execute Bake, computing cloth shape for the specified frame sequence.

- Edit the results or adjust the cloth mesh at individual frames.

- Adjust the surroundings or deforming objects, then re-run from the current frame.

Cloth Collisions panel. 

Quality
General parameter controlling simulation fidelity. Larger values consume more time but ensure fewer tears and penetrations.

### Object Collisions

When cloth needs deflection from another object, that object must activate collision physics (not on the cloth itself).

To permit objects to repel cloth, enable collision physics on the obstacle object.

Note

Non-mesh objects (NURBS surfaces, text) require Convert to mesh format.

Distance
How close another object must approach before the simulator repels the cloth. Smaller values risk errors but run faster; larger values become unrealistic and costly. Balance matters.

Impulse Clamping
Reduces explosions in tight, intricate collisions by constraining post-collision displacement.

Vertex Group
Faces where all vertices belong to this group avoid collision with objects.

Collision Collection
Only objects in this Collection participate in cloth collision. These objects must also have Collision physics active.

### Self-Collisions

Real cloth cannot pass through itself; enabling self-collision enforces this. Computation rises, but realism improves.

Tip

Distant flags skip this; close-ups of capes or shirts should have it on.

Friction
Controls cloth slickness during self-collision. Silk exhibits lower friction than cotton.

Distance
Cloth begins repelling itself at this separation. Smaller values risk errors but accelerate; larger values look wrong or slow. Finding balance is key.

Impulse Clamping
Constrains motion after collision in cramped situations to prevent instability.

Vertex Group
Faces with vertices entirely in this group exclude themselves from self-collision.

See also

Example blend-file:
Cloth self-collisions.

[Related references](INDEX.md).
