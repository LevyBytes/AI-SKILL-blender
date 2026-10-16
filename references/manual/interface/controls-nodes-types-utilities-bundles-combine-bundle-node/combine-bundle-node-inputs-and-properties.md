# Combine Bundle Node: Inputs, Properties, Bundle Items, Outputs

## Combine Bundle Node

The Combine Bundle node creates a bundle from multiple inputs, each becoming an element identified by socket name. Access values elsewhere using Separate Bundle.

Inputs are arbitrary in count and type, supporting Geometry, Objects, Values (float, integer, boolean, vector, color), Fields, and Nested Bundles. Properties (sidebar Node tab): Sync Sockets updates the node to match connected nodes after renaming/adding/removing; Define Signature locks the list/types for stable interfaces when publishing (disables adding/removing until toggled off).

Bundle Items displays per-element entries (double-click to rename). Add Item creates a socket. Remove Item deletes one. Type selects the data type (float/vector/geometry/object/bundle); value types show a default-value control. Outputs the resulting bundle containing all inputs.

### Combine Bundle Node

Bundle creation from multiple inputs: each becomes a named bundle element.
Access individual items using Separate Bundle elsewhere in the network.

### Inputs

Arbitrary input sockets, custom names and types.
Supported types: Geometry, Objects, Values (float, integer, boolean, vector, color), Fields, Nested Bundles.

### Properties

Properties appear in the Node tab of the Sidebar.

**Sync Sockets**
Align the node to connected node signatures.
Use after socket rename, add, or remove.

**Define Signature**
Lock items and types for stable publication.
Blocks add/remove until disabled.

### Bundle Items

**List of bundle items**
One entry per element.
Double-click to rename.

**Add Item**
Insert a socket.

**Remove Item**
Delete the selected socket.

**Type**
Data type (e.g. Float, Vector, Geometry, Object, Bundle).
Value types show default value control.

### Outputs

**Bundle**
All defined inputs packaged together.

### Combine Bundle Node

This node assembles a new Bundle out of several input values. Each input lands in the bundle as an element keyed by its socket name. Elsewhere in the node tree you can pull those values back out with the
Separate Bundle

### Inputs

You can give the node any number of input sockets. Each one takes a custom name and type. Supported types include (but are not limited to):

- Geometry

- Objects

- Values (e.g. float, integer, boolean, vector, color)

- Fields

- Nested Bundles

### Properties

You will find the properties under the Sidebar's Node tab.

Sync Sockets
Realigns this node so its sockets match the signature of whatever it is wired to. Trigger it after any rename, addition, or removal among the sockets.

Define Signature
Locks down today's item list and their types, holding interfaces steady as node groups get published. With it on, you cannot add or drop items until it is switched back off.

[Related references](INDEX.md).
