# Inspection

## Inspection

### Inspection

Intermediate socket values and tree behavior are useful to understand during node-tree building or debugging. Blender offers multiple tools for this.

Note: Inspection tools generally show data from the most recent tree evaluation. If not yet evaluated, no information is available.

### Socket Inspection

Displays socket values from the last evaluation. For primitive types (integers, vectors, strings) the exact value is shown; for geometry, metadata such as data types and element counts are stored.

Socket values log only when the tree executes (so nodes must connect to Group Output), not during rendering (for performance).

### Attribute Search

Triggered by clicking an attribute input in the modifier. Lists all attributes available at that point in the execution.

### Viewer Node

Displays intermediate geometry in the Spreadsheet Editor and viewport. See Viewer Node for details.

### Node Warnings

Invalid node inputs trigger a warning icon in the title bar. Hover to see the error. Warnings only appear after node execution (nodes must connect to Group Output).

### Node Timings Overlay

Execution time for each node during the last evaluation. Enable from the overlay popover (top-right, node editor). When a node group runs in multiple contexts, timing reflects the current editor context (shown in the top-left path).

Frame nodes show combined time for all contained nodes; Group Output shows total tree time.

Timings are approximate (copying/deleting geometry inputs may be included). When nodes use multiple cores, the evaluation system may work on other nodes simultaneously. Field nodes typically contribute no direct time—their cost rolls into the data-flow nodes they feed.

### Named Attributes Overlay

Shows which custom named attributes are in use by nodes or groups. Named attributes (Capture Attribute Node, Named Attribute Node, Remove Named Attribute Node) can be written, read, or removed.

Named attributes (unlike anonymous ones) risk overwriting input-geometry attributes with the same name, potentially corrupting essential data. The overlay simplifies detection.

The same information appears in the Named Attributes panel within the modifier UI.

### Geometry Randomization

Many nodes do not guarantee output-element order. For example, Triangulate produces deterministic but undocumented ordering, which may shift across Blender versions. Setups depending on specific indices may break on updates.

"Geometry randomization" temporarily shuffles result elements to expose index-order dependencies. Enable it to verify long-term stability of complex setups.

To enable: turn on Developer Extras in preferences, then search for "Set Geometry Randomization." The popup toggles it on/off.

[Related references](INDEX.md).
