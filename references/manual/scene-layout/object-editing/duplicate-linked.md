# Duplicate Linked

## Duplicate Linked

### Duplicate Linked

Reference

Mode :

Object Mode

Menu :

Object ‣ Duplicate Linked

Shortcut :

Alt - D

You may create a Linked Duplicate instead of a simple Duplicate, called a deep link. A new object is created with all data linked to the source object. If you edit one linked object in Edit Mode, all linked copies update. Transform properties (object data-blocks) remain copied, not linked, so rotation, scaling, and movement are independent. Consult the Examples section for discussion.

If the source object was animated, the duplicate links to the same Action. Though each object has independent transform properties, the animation system assigns them the same values. If this is unwanted, create a single-user copy of the action in the Action or NLA Editor.

Linked
In the Duplicate Objects Adjust Last Operation panel, the Linked checkbox is checked, unlike with Duplicate.

Hint

To alter a linked duplicate independently of the source, manually transform the object to a "single-user" copy by pressing LMB in the Object Data panel of the Properties. (See Data-Block Menu.)

See also

Make Single User for decoupling data-blocks.

### Examples

The Cube object was linked duplicated.

The Cube was linked duplicated with Alt - D. Though both cubes are separate objects with distinct names (Cube and Cube.001), the single mesh named Cube is shared.

- When you edit the mesh in Edit Mode on one object, the other cube changes identically. Mesh data is linked, not copied.

- Conversely, rotating or scaling one cube in Object Mode leaves the other unchanged. Transform properties are copied, not linked.

- As in the prior example, the newly created cube inherited the source's material. Material properties are linked, not copied.

A typical table has a top and four legs. Design one leg, then create linked duplicates three times for the remaining legs. Later modifications to the mesh preserve all legs. Linked duplicates apply similarly to drinking glass sets, vehicle wheels, or any repetitive or symmetrical arrangement.

See also

Linked Library Duplication

Linked Libraries also use duplication. Any object or data-block from other blend-files can be reused in the current file.

Hint

To make transform properties (i.e. object data-blocks) "linked," consult the parenting documentation.

[Related references](INDEX.md).
