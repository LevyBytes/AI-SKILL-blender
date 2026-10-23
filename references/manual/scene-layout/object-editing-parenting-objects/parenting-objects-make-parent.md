# Parenting Objects: Make Parent

## Parenting Objects

### Parenting Objects 

When building intricate structures—such as a chronograph—you might model individual sections as distinct objects.
To coordinate the sections so they move together (as the "watch"), assign one as the parent of the rest.
These child objects inherit its position shifts, rotations, and size changes.

Unlike most living systems, every object or skeleton in Blender has one parent at most.
When you give an object a different parent while one already exists, the previous connection breaks.
The phrase "parents" when plural denotes the succession of ancestry: immediate parent, grandparent, great-grandparent, and so on.

### Make Parent 

Reference

Mode:
Object Mode

Menu:
Object ‣ Parent

Shortcut:
Ctrl - P

To establish parent-child bonds, pick at least two objects
(designate the child objects first, then select the parent object last),
then press Ctrl - P. The Set Parent To dialog appears, presenting
several parenting strategies to pick from.
Confirming an option applies the parent-child relationship.
All chosen objects will have their 'parent' property set to the active object,
becoming 'siblings' to each other.

The Set Parent To popup is context-aware: the number of choices shifts depending on the selection state
when Ctrl - P is triggered.

When the parent moves, rotates, or changes size, child objects typically transform identically.
However, the inverse is not true: modifying child objects leaves the parent unchanged.
The effect flows strictly downward: parent to child, not vice versa.

Tip

You can "relocate" a child back to its parent's location by resetting its origin.

Type
Blender provides numerous parenting approaches, listed here.
Along with linking the chosen objects, some approaches attach a Modifier or Constraint to the child,
with the parent as the destination, or activate a parent behavior like Follow Path.

- Object

- Armature Deform

- Bone

- Curve Deform

- Follow Path

- Path Constraint

- Lattice Deform

- Vertex

- Vertex (Triangle)

Keep Transform
The object's existing world position (its absolute location, rotation, and size in the world) is captured.
The new parent is established, and the Parent Inverse matrix is calculated to ensure
the object maintains its previous world position after parenting.

Hint

Refer to the Outliner

An alternative way to observe the parent-child structure and groupings is through the Outliner panel.

[Related references](INDEX.md).
