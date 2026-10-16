# Parenting Objects: Bone Parent, Relative Parenting, Vertex Parent, Vertex Parent from Edit Mode

### Bone Parent 

Bone parenting designates a specific bone in an armature as the parent of one or more separate objects.
When the armature is manipulated, the child object shifts
only when the designated bone moves.

Three armature images with four bones each. 

In Fig. Three pictures of armatures with four bones. the 2nd bone controls the child cube.
The cube transforms when the 1st or 2nd bones move.
Modifying the 3rd and 4th bones leaves the cube unaffected.

To employ bone parenting, first select all child objects, then Shift - LMB pick the armature
and move into Pose Mode and
pick the target bone by LMB.
Then press Ctrl - P and pick bone from the Set Parent To menu.

Now adjusting that bone during Pose Mode will also reposition the child objects.

### Relative Parenting 

Bone relative parenting is a per-bone toggle.
This behaves much like bone parenting with a single distinction.

With bone parenting, if you pick a bone with children and
shift to Edit Mode and reposition that bone;
Moving back to Pose Mode on that bone will
cause the child object to snap to the bone's Pose Mode position.

Single armature bone with a child cube parented via bone parenting. 

Picture 1 displays the initial setup. Picture 2 illustrates the state after modifying the bone in Edit Mode,
then returning to Pose Mode. Notice the child object shifts to align with the bone's new Pose Mode location.

Bone relative parenting operates differently;
Moving a parent bone in Edit Mode will not cause the child objects to shift to the bone's fresh Pose Mode position when you return to Pose Mode.

Single bone with bone relative parenting controlling a cube. 

Picture 1 illustrates the initial layout. Picture 2 demonstrates conditions after editing the bone in Edit Mode,
then switching back to Pose Mode.
The child retains its original spot and doesn't snap to the bone's fresh location.

Note

Setting parents with Ctrl - P and picking "Bone" or "Bone Relative"
will respectively deactivate or activate the bone's "Relative Parenting" feature.
Since "Relative Parenting" applies to individual bones, altering this affects
all children of that bone simultaneously.

### Vertex Parent 

For meshes, curves, surfaces, and lattices,
you can use a vertex or point as the parent of other objects.
You may parent objects to a solitary vertex or a trio of vertices;
doing so causes child objects to follow when the parent mesh deforms.

### Vertex Parent from Edit Mode 

In Object Mode, select the children and then the parent object.
Press Tab to enter Edit Mode and on the parent select either one vertex
to define a single anchor, or choose three vertices to define a zone
(the three vertices don't have to form a complete face;
any three from the parent work),
then press Ctrl - P and verify.

At this point, when a solitary vertex is chosen,
a line will appear linking the vertex to the child/children. When three
vertices are chosen, a line connects the child/children to the averaged position of
those three vertices (on the parent). As the parent mesh deforms and the parent vertex/vertices shift,
the child/children also shift.

[Related references](INDEX.md).
