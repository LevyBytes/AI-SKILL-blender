# Instance on Points Node

## Instance on Points Node

### Instance on Points Node

The Instance on Points node places instances on each point of input geometry. Instances are efficient duplicates that avoid copying underlying data. Works with any point-domain geometry (meshes, point clouds, curve control points).

Point attributes propagate to the instance domain.

Tip: Use the Make Instances Real operator to convert instances to objects.

Note: For non-geometry object types (lights), use Object Info Node. Metaball objects are not supported.

### Inputs

Points
Input geometry; point positions control instance transforms.

Note: If input contains instances, the node creates instances on points inside the instances (nested instancing). New instances inherit the Rotation and Scale from inputs but also the parent instance transforms.

Selection
Boolean: true = create instance, false = skip.

Instance
Geometry to place on each selected point. May contain real geometry or multiple instances (useful with Pick Instance).

Pick Instances
If enabled, select an instance from the geometry's instance list per point instead of copying all geometry. Intended use: Collection Info Node.

Instance Index
Which instance to pick (only when Pick Instances = true). Defaults to point ID or index. Negative/out-of-range values wrap.

Rotation
Euler rotation per instance. Accepts outputs from Distribute Points on Faces, Curve to Points, or direction vectors converted via Align Rotation to Vector Node.

Scale
Size per generated instance.

### Outputs

Instances
Output geometry. If the input's id attribute exists, it copies to result instances.

[Related references](INDEX.md).
