# Get Bundle Item Node

## Get Bundle Item Node

The Get Bundle Item node retrieves values from bundles using string paths. Bundles group heterogeneous data; this node accesses individual items. Non-existent paths return defaults with Exists set to false.

Bundle inputs the source bundle. Path identifies the item (slash-separated for nested bundles, e.g., settings/size, attributes/color). Remove (when enabled) deletes the item before passing the bundle through.

Socket Type (properties) sets the retrieved-item data type, determining Item output type. Shape (sidebar) specifies data structure (Single, Field, Grid).

Bundle outputs the resulting bundle (post-optionally-removing). Item outputs the value at the path or default if not found. Exists outputs True if found, False otherwise.

### Get Bundle Item Node

Retrieves a value from a bundle via string path.
Bundles group heterogeneous data; this node unpacks individual items.

If the path is absent, a default is returned and Exists outputs false.

### Inputs

**Bundle**
Input data source.

**Path**
Item location via slash-separated segments.
Examples: `settings/size`, `attributes/color`.

**Remove**
If on, delete the retrieved item before passing the bundle through.

### Properties

**Socket Type**
Item output data type.

**Shape**
Data structure (Single, Field, Grid).
Controls evaluation and passage through the network.
Sidebar option.

### Outputs

**Bundle**
Result after optional item removal.

**Item**
Retrieved value at the path, or the default if absent.

**Exists**
True if found; False otherwise.

[Related references](INDEX.md).
