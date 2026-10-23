# Sample Nearest Surface Node

## Sample Nearest Surface Node

### Sample Nearest Surface Node

Retrieves attribute values from closest surface points. Non-face attributes interpolate across surface.

Similar to Geometry Proximity Node but returns any attribute, not just position.

Warning: Samples surface; loose points/edges ignored.

### Inputs

Mesh: Source geometry.

Value: Source field for transfer.

Group ID: Face domain; splits input by id.

Sample Position - Sampling origin (default: Position Node equivalent).

Sample Group ID: Selects group for closest-point search.

### Properties

Data Type: Retrieved value type.

### Outputs

Value: Retrieved and interpolated attribute.

Is Valid: Success indicator; fails when group empty.

[Related references](INDEX.md).
