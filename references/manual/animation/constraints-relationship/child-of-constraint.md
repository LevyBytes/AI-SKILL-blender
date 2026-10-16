# Child Of Constraint

## Child Of Constraint

The Child Of constraint transforms an object or bone as if it were the child of another object or bone, its main advantage over a normal parent-child relationship being an animatable Influence, so you can switch parents over time. That Influence can also mix several Child Of constraints into a weighted average of multiple parents (though for bone parents the Armature Constraint may be better). Note it can "parent" one bone to another but isn't well suited to building bone chains — notably it can't emulate connected bones (where the parent's tip always meets the child's base). Options: Target (the parent object or bone); Location, Rotation, Scale (which of the child's axes to affect); Set Inverse (click when the child's transform is right with the constraint off but wrong with it on); Clear Inverse (tell the constraint the child's current transform with it disabled is the correct relative transform, applied as an offset to the parent once re-enabled); and Influence.

[Related references](INDEX.md).
