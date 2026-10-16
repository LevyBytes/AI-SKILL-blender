# Instances

## Instances

### Instances

In addition to real data (meshes, curves), objects can hold instances—references to other geometry, objects, or collections. Instancing avoids duplicating data, letting render engines like Cycles handle repeated geometry efficiently.

Each instance tracks its source geometry and transformation relative to the source. Instances also store the id attribute for correcting motion blur during animation.

Use the Instance on Points Node to create instances.

Warning: Geometry-node instancing cannot combine with the Instancing panel in the property editor.

### Nested Instancing

Since instances hold geometry and geometry holds instances, nesting is possible—instancing instances, or collections of instances. The Instance on Points Node creates nested instances by default.

A node group creating nested instancing via chained Instance on Points nodes.

Here, nested instancing distributes geometry containing both mesh and instance data. Output holds a "real" mesh plus an instance group. Each instance contains a sphere mesh and many cone instances.

Instance hierarchy for the above example.

This approach helps because the output contains only three unique meshes (plane, sphere, cone), dramatically improving performance vs. unique copies.

Warning: Only eight levels of nested instancing render and display in the viewport. Deeper trees can exist in geometry nodes but must be realized at the tree's end.

### Realizing Instances

"Realizing" converts instances into unique geometry. Realized instances consume more memory and require per-instance manipulation rather than per-source-geometry processing.

Use the Realize Instances Node.

### Instance Processing

Nearly all geometry-processing nodes work on each unique geometry once, not on each realized copy. For example, placing a Subdivision Surface Node after the nested-instancing example above processes three meshes, not each instance separately. Similarly, processing String to Curves output handles each unique character once.

This boosts performance but means all instances of the same geometry change identically. To vary individual instances, use Realize Instances Node first.

[Related references](INDEX.md).
