# For Each Geometry Element Zone

## For Each Geometry Element Zone

### For Each Geometry Element Zone

Execute nodes per element of a geometry—each face, each instance, etc.

Ideal for generating large or complex per-element geometry.
Examples: unique tree per curve, unique building per face.

Less suited for small per-element work (e.g., individual hairs); slower than bulk operations.
Design node setups to avoid tiny sub-geometry iteration for performance.

The For Each Element zone.

### Inputs

**Geometry**
Elements to iterate.

**Selection**
Subset of Domain to process.

**Index**
Element position in source geometry.
Note: same index can repeat for multi-type iteration.

**Element**
Input split per element.
Single-element geometry for current iteration.
Unavailable for Face Corner (corners need faces).

**Note:** Splitting large geometries is inefficient.
Unused outputs skip computation, improving performance.

### Properties

**Domain**
Attribute domain for iteration.

**Inspection Index**
Element index for inspection tools (Viewer Node, socket inspection).

### Outputs

Main Geometry outputs create attributes on the first output.
Every single value inside the zone becomes an attribute at the current index.

Generated panel outputs (including default Geometry) join geometry from each element.
Non-geometry below a geometry output becomes an anonymous attribute on that joined geometry.
Input geometry attributes propagate to these outputs.

[Related references](INDEX.md).
