# Parenting Objects: Vertex Parent from Object Mode, Make Parent without Inverse, Clear Parent, Known Limitations, Non-Uniform Scale

### Vertex Parent from Object Mode 

Vertex parenting can be set from Object Mode;
this works like standard object parenting,
press Ctrl - P in Object Mode and pick Vertex or Vertex (Triangle).

Vertices nearest to each object are selected, which is typically the expected behavior.

| Description | Description | Description |
| --- | --- | --- |
| The small cubes can individually snap to triads of neighboring vertices on the icosphere using the "Vertex (Triangle)" option in the set parent menu.  | Reshaping the parent in Edit Mode causes each cube to follow its vertex parent independently.  | Resizing the parent icosphere in Object Mode likewise scales each cube as anticipated.  |

The parent context option lets creators rapidly establish many vertex parent
connections,
avoiding manual setup of each relationship.

Note

It resembles a "reversed" hook effect.

### Make Parent without Inverse 

Reference

Mode:
Object Mode

Menu:
Object ‣ Parent ‣ Make Parent without Inverse

This applies the parent and then resets the Parent Inverse matrix along with the object's local location.
Consequently, the object shifts to the parent's position but retains its rotation and scale.

Keep Transform
The object's existing world position (its absolute location, rotation, and size in the world) is captured.
The new parent relationship is applied, and the object's local transform values are adjusted to keep
its current world position even after the new parent is set.

### Clear Parent 

Reference

Mode:
Object Mode

Menu:
Object ‣ Parent

Shortcut:
Alt - P

Parent relationships can be severed using Alt - P.

Clear Parent
If the parent is among the selection, no change occurs.
If a child or children are chosen, they are separated from the parent,
become independent, and return to their original location, rotation, and proportions.

Clear and Keep Transformation
Separates the children from the parent while maintaining the location, rotation, and size that came from the parent.

Refer to Non-Uniform Scale which may be pertinent.

Clear Parent Inverse
Instead of severing the parent-child structure, this eliminates
the Parent Inverse matrix from the chosen objects. With a null matrix,
the location, rotation, and scale of the children are interpreted
in the parent's coordinate space.

### Known Limitations 

### Non-Uniform Scale 

When a parent has unequal scaling and is rotated relative to its child, shearing can occur.

Although parenting accommodates this, the shear gets lost if the parent is removed since it
cannot be stored as simple location, scale, and rotation values.

If Clear and Keep Transformation causes an unexpected object movement, non-uniform scale is likely the culprit.

[Related references](INDEX.md).
