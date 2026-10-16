# Sample UV Surface Node

## Sample UV Surface Node

Sample UV Surface Node

Queries values on a mesh's surface at specific UV coordinates. Internally, it performs a reverse UV lookup from 2D space—finding the corresponding face and its position for each coordinate.

Warning: Overlapping faces in the UV map cause issues. At locations with missing or overlapping faces, the node outputs the default zero value for most data types.

Inputs
Mesh: Geometry containing the mesh with the UV map to sample.
Value: A field to evaluate on the target geometry for later sampling at surface positions.
UV Map: The mesh's UV map to sample, evaluated on the Mesh input. Should not have overlapping faces.
Sample UV: The coordinates to sample within the UV map.

Properties
Data Type: The format for retrieved values.

Outputs
Value: Retrieved and interpolated data from the geometry, mapped per the node settings.
Is Valid: Whether the node successfully found a single face to sample at the coordinate.

[Related references](INDEX.md).
