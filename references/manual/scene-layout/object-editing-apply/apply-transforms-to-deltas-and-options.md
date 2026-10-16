# Apply: Transforms to Deltas, Options, Animated Transform to Deltas, Visual Transform, Visual Geometry as Mesh

### Transforms to Deltas

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Location / Rotation / Scale to Deltas

Moves the object's primary transforms (Location, Rotation, Scale) into Delta Transforms. Existing delta transforms are added to the new values.

This enables "baking" current transforms into the delta channels while freeing primary transform channels for new adjustments or keyframes.

Available options:

- Location to Deltas – Shifts the object's location to Delta Location.

- Rotation to Deltas – Shifts the object's rotation to Delta Rotation.

- Scale to Deltas – Shifts the object's scale to Delta Scale.

- All Transforms to Deltas – Performs all three simultaneously.

### Options

Reset Values
Clear primary transform values after transfer to deltas.

When enabled, primary Location, Rotation, and Scale reset (to 0 or 1 respectively) while the appearance remains unchanged because deltas hold the prior values.

### Animated Transform to Deltas

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Animated Transform to Deltas

Converts existing animation keyframes from primary transforms (Location, Rotation, Scale) to Delta Transforms.

Animation data shifts from main transform channels to the delta equivalents while main transforms remain at their current values.

### Visual Transform

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Visual Transform

Applies each selected object's constraints to its own transformation. Objects retain their position, rotation, and scale even if their constraints are later disabled or removed.

### Visual Geometry as Mesh

Reference

Mode :

Object Mode

Menu :

Object ‣ Apply ‣ Visual Geometry to Mesh

Applies the visual state of all selected objects (modifiers, shape keys, hooks, etc.) to their data. This freezes object data as static geometry and converts non-mesh types to mesh.

For details, consult the Convert mesh documentation.

[Related references](INDEX.md).
