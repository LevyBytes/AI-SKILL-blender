# Store Bundle Item Node

## Store Bundle Item Node

The Store Bundle Item node writes values into bundles at specified paths, replacing existing items or creating new paths automatically. Commonly used for incremental bundle building, grouping heterogeneous data for network passage.

Bundle inputs the bundle to store data into. Path identifies storage location (slash-separated for nested bundles, e.g., settings/size, attributes/color). Item is the value to store; data type/structure depends on node properties.

Socket Type (properties) sets the Item-input data type. Shape (sidebar) specifies data structure (Single, Field, Grid).

Bundle outputs the resulting bundle with the stored item.

### Store Bundle Item Node

Insert a value into a bundle location via a path string.
Replace existing items at that location.
Automatically create new paths.
Incrementally construct or alter bundles.
Consolidate heterogeneous data for passage through node networks.

### Inputs

**Bundle**
Data destination.

**Path**
Item storage location via slash-separated segments.
Examples: `settings/size`, `attributes/color`.

**Item**
Value to store.
Data type and structure defined by node properties.

### Properties

**Socket Type**
Item input data type.
Determines storable data type.

**Shape**
Data structure (Single, Field, Grid).
Controls how data evaluates and stores in the bundle.
Sidebar option.

### Outputs

**Bundle**
Bundle with the stored item.

[Related references](INDEX.md).
