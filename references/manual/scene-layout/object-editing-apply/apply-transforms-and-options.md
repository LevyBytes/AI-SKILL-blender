# Apply: Transforms, Options

## Apply

### Apply

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply

Shortcut :

Ctrl - A

These operations apply multiple transformation types to selected objects. Transformation coordinates shift from objects to their data. If hierarchical children exist, transformations apply to them as well.

### Transforms

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Location / Rotation / Scale / Rotation & Scale

Applying transforms resets numerical Location, Rotation, or Scale values while preserving on-screen appearance.

Specifically:

- The object's position shifts to the global origin (for location).

- Rotation values zero out.

- Scale values reset to 1.0.

The geometry adjusts so the 3D Viewport and final render appearance remains identical.

For uncomplicated cases, you may perceive no difference, but applying transforms affects how modifiers, constraints, and parenting operate, as they often depend on object transform values.

Warning

Armature Objects

Transform application is supported for armatures but does not affect pose positions, animation curves, or constraints. Apply transforms prior to rigging and animation.

Important

When applying transforms to an object sharing Object Data with others, data must first become Single User. Blender prompts confirmation.

### Options

Location
Apply (set) the object's position. Blender designates the current position as 0 on each axis; the object remains in place but the location becomes the "default." The object origin moves to (0, 0, 0) (where the colored axis lines intersect).

Rotation
Apply (set) the object's rotation. The current rotation becomes 0 degrees on each axis; the object remains in place but the rotation becomes the "default."

Scale
Apply (set) the object's scale. The current scale becomes 1.0 on each axis; the object remains in place but the scale becomes the "default."

Rotation & Scale
Apply (set) both rotation and scale simultaneously.

Apply Properties
Modify attributes such as curve vertex radius, font size, and bone envelope according to the applied transformation. (Appears in the Adjust Last Operation panel)

Corrective Flip Normals
Inverts surface normals when applying negative scale, avoiding inverted shading from negative scaling.

[Related references](INDEX.md).
