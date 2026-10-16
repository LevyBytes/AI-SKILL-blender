# Separate Bundle Node

## Separate Bundle Node

The Separate Bundle node extracts individual values from bundles, with each output corresponding to a named bundle element. It's the Combine Bundle counterpart, typically retrieving previously grouped structured data.

Bundle inputs the source bundle with grouped values. Properties (sidebar Node tab): Sync Sockets updates the node to match connected nodes; Define Signature locks the list/types for stable interfaces when publishing.

Bundle Items displays per-element entries (double-click to rename). Add Item creates a socket. Remove Item deletes one. Type selects data type (float/vector/geometry/object/bundle); value types show default-value controls.

Outputs are dynamic; each socket outputs the corresponding bundle-item value using the item's name and type.

### Separate Bundle Node

Unpacks individual values from a Bundle.
Each output corresponds to a bundle element by socket name.
Counterpart of Combine Bundle; retrieves grouped data.

### Inputs

**Bundle**
Grouped value source.

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

Dynamic output set: each socket outputs the corresponding bundle item by name and type.

### Separate Bundle Node

This node pulls individual values out of a
Bundle. Each output maps to one element in the bundle, keyed by its socket name.

It is the counterpart to the
Combine Bundle node and typically serves to fetch back structured data that was grouped together earlier.

### Inputs

Bundle
The input bundle that holds all the grouped values.

### Properties

You will find the properties under the Sidebar's Node tab.

Sync Sockets
Realigns this node so its sockets match the signature of whatever it is wired to. Trigger it after any rename, addition, or removal among the sockets.

Define Signature
Locks down today's item list and their types, holding interfaces steady as node groups get published. With it on, you cannot add or drop items until it is switched back off.

### Bundle Items

List of bundle items
One row shows up for each element the bundle holds; rename a row by double-clicking it.

Add Item
Attach a fresh socket to the bundle.

Remove Item
Drop the socket you have selected.

Type
Data type carried by the chosen item (e.g. Float, Vector, Geometry, Object, Bundle). Value types surface a default-value control, which kicks in whenever that socket is left unlinked.

### Outputs

This node carries a dynamic set of output sockets. Each one outputs its matching bundle item's value, taking that item's name and type as set in the bundle.

[Related references](INDEX.md).
