# Closure: Output Items, Outputs, Usage, Using External Values, Example, Inputs, Properties

### Output Items

Available with closure output zone selection.

**List of output sockets**
One per socket.
Double-click to rename.

**Add Item**
Insert a socket.

**Remove Item**
Delete the selected socket.

**Type**
Data type (e.g. Float, Vector, Geometry, Object, Bundle).
Value types show default value control.

**Shape**
Data structure (Single, Field, Grid).
Controls evaluation and network passage.
See Socket Shape.

### Outputs

Closures return values to the calling node tree.
Create them by dragging a socket from inside the zone to the blank output, or add in properties.

### Usage

Reusable logic injected elsewhere: user-defined behavior in procedural systems.

Common scenarios:

- **Custom scattering:** Define terrain distribution rules.
- **Procedural distribution:** Modify or arrange instances.
- **Flexible mappings:** Provide adjustable transformations or field logic.

### Using External Values

Closures capture values outside their zone.
A captured value stores with the closure and persists across contexts.

External value capture avoids explicit sockets, simplifying reuse across trees.

Capturing external input inside a closure.

### Example

- Terrain generator: replace fixed distribution with Evaluate Closure.
- Expose closure input on the group interface.
- Main tree: create Closure Zone, connect to that input.
- Inside zone: define desired placement logic.

When evaluated, the custom logic executes instead of defaults.

Closure Zone with custom tree distribution.

### Closure

The Closure node marks out a zone that wraps a reusable group of nodes acting like a function. It declares inputs, outputs, and internal logic that can run elsewhere in the node tree by way of an
Evaluate Closure node.

With closures, users can feed custom procedural logic into node groups, which makes tools more modular and adaptable. Rather than duplicate or edit an existing group, a closure can expose user-defined behaviour while leaving the main system's structure intact.

An empty closure zone.

### Inputs

A closure declares its own inputs, which serve as parameters for the internal node logic. To make one, drag the empty input socket onto another socket, or place sockets manually from the node's properties. Every such input names a parameter the closure will accept wherever it later runs.

### Properties

The Closure node carries no functional properties of its own; you shape its interface from the Node tab over in the Sidebar, where inputs and outputs may be added, dropped, and renamed to set the closure's signature.

Sync Sockets
Realigns this node so its sockets match the signature of whatever it is wired to. Trigger it after any rename, addition, or removal among the sockets.

Define Signature
Flags this zone as the origin of a closure signature other nodes are free to cite, holding input and output definitions in step across every instance of the closure.

[Related references](INDEX.md).
