# Apply: Visual Geometry to Objects, Make Instances Real, Options, Parent Inverse

### Visual Geometry to Objects

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Visual Geometry to Objects

Produces new objects from the evaluated geometry of the active object, incorporating all modifier, constraint, and instancing effects.

This operator differs from Make Instances Real in several ways:

- Instanced geometry is not realized. Shared data is maintained across objects using it.

- The source object remains unmodified, avoiding disruptions to object relationships.

- Instancing hierarchies are maintained through new objects and collections reflecting the evaluated structure.

Extracts visible results of geometry nodes, modifiers, or instancing setups without permanently changing the original scene.

Note

Instance attributes (e.g. custom per-instance data) are currently not preserved.

### Make Instances Real

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Make Instances Real

This operation generates a separate object for each instance produced by the selected objects and removes direct instancing from them.

Each instance becomes an actual object.

Warning

This applies to both direct (from verts or faces…) and indirect (from particle system…) instancing. With tens of thousands of instances (from particles for instance), Blender may slow considerably, as it struggles with large object counts.

### Apply

### Options

By default, new objects are added to the original instancer's collection without internal hierarchies. The following options alter this.

Parent
If Keep Hierarchy is not set, parents all generated objects to the original instancer.

Otherwise, parents generated objects not already parented to their instancer or its corresponding new copy (relevant for recursive instancing).

Keep Hierarchy
Maintains internal hierarchies (i.e. parent relationships) within newly generated objects.

Tip

Typically, to produce a new hierarchy matching the instancing arrangement, enable both options.

Note

Recursive instancing preservation (instancers instancing other instancer objects, etc.) is only partially supported.

Uncomplicated cases (like an empty instancing a collection with instances of other collections) typically function well, but complex cases may fail to fully reproduce the complete hierarchy.

### Parent Inverse

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Parent Inverse

Applies the object's Parent Inverse transform to the object data.

[Related references](INDEX.md).
