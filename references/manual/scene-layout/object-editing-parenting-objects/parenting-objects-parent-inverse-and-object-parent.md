# Parenting Objects: Parent Inverse, Object Parent, Example: Object Parent (Keep Transform)

### Parent Inverse 

Blender can set a parent without shifting the child object's location.
A hidden matrix called the Parent Inverse matrix manages this,
sitting between the parent's and child's transform data.

When objects are parented using Ctrl - P, the Parent Inverse matrix is recalculated.
The object's local position, rotation, and scale may also shift based on the Set Parent selection. See Object Parent for details.

The Parent Inverse matrix gets cleared by Clear Parent Inverse.

Note

Parenting via the Object Properties panel always resets the Parent Inverse matrix.
This can trigger an unexpected shift in the object's location.
To sidestep this, use Ctrl - P when assigning a new parent.

### Object Parent 

Object Parent represents the most versatile parenting method in Blender.
It takes the chosen objects and makes the active object
the parent of all selections. Each child receives
all position, rotation, and size modifications from the parent. The parent can be any object type.

If the object currently has a parent, it is removed first.
This repositions the object to its own location, rotation, and scale,
free from the previous parent's effect.

Three operators allow parenting. They differ in how they calculate the Parent Inverse matrix
and the object's local Transform.

### Example: Object Parent (Keep Transform) 

Parenting with Keep Transform preserves any modifications that child objects received from
the prior parent.

Imagine a scene with two empty objects called "EmptyA"
and "EmptyB", and a Monkey object. Fig. Scene with no parenting. displays the three without
active parent relationships.

Scene with no parenting. 

Choose the Monkey with LMB and then Shift - LMB
choose "EmptyA" and press Ctrl - P and choose Object
from the Set Parent To menu.
"EmptyA" now serves as the Monkey's parent.
With only "EmptyA" picked, transforming it (rotating/scaling/moving) also transforms
the Monkey correspondingly.

Resize the "EmptyA" object, causing the Monkey to shrink and shift leftward.

The monkey becomes the child of "EmptyA". 

Now pick only the Monkey using LMB and then Shift - LMB
choose "EmptyB" and press Ctrl - P and pick Object from
the Set Parent To dialog.
"EmptyB" is now the Monkey's parent.
Watch the Monkey's scale change when you switch parents.

The monkey becomes the child of "EmptyB". 

This occurs because the Monkey was never directly resized—the change came from being parented to "EmptyA" which was resized.
Switching the Monkey to "EmptyB" removes those indirect changes,
because "EmptyB" has not been modified.

This is frequently the desired result, yet it's also useful to preserve
earlier transformations the child acquired from the original parent when changing parents.
If, instead of switching the Monkey's parent from "EmptyA" to "EmptyB" plainly, you chose parenting type Object and toggle Keep Transform ,
the Monkey would retain its resizing from "EmptyA"
when assigned to "EmptyB".

The Object parent with Keep Transform setting. 

To follow this example, here is the demonstration file:

File: Parent_-_Object_(Keep_Transform)_(Demo_File).blend.

[Related references](INDEX.md).
