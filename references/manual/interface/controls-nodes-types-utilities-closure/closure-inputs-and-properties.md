# Closure: Inputs, Properties, Input Items

## Closure

The Closure node defines a zone encapsulating a reusable node section functioning like a custom node. It specifies inputs, outputs, and internal logic executable elsewhere via Evaluate Closure nodes. Closures enable passing user-defined procedural logic into node groups, creating modular, adaptable tools without duplicating or editing existing groups.

Closures define their own inputs acting as parameters for internal logic, created by dragging the blank input socket or adding manually. Properties (Node tab, sidebar): no functional properties of their own, but the interface is configurable. Inputs and outputs add, remove, and rename to define the closure signature.

Sync Sockets updates the node to match connected nodes after renaming/adding/removing. Define Signature marks the closure as the signature source, ensuring consistent definitions across instances.

Input Items list input sockets (double-click to rename). Add Item creates a socket. Remove Item deletes one. Type defines data type (float/vector/geometry/object/bundle); value types show defaults. Shape specifies structure support (Single, Field, Grid; see Socket Shape).

Output Items (when closure output is selected) list output sockets (double-click to rename). Add Item creates a socket. Remove Item deletes one. Type and Shape work as input items.

Closures define outputs returning values to the evaluation node tree, created by dragging sockets from within the zone to the output's blank socket or by adding manually.

Usage: Closures define reusable logic injected into other trees, commonly in procedural systems where behavior remains user-defined. Use cases include custom scattering rules (terrain generators), procedural distribution/modification (instance nodes), adjustable mappings/field evaluation/transformation logic.

External-value capture: Closures capture values from outside their zone, stored as part of the definition and available in different contexts. Captured values preserve external parameters (scale, density, color) without explicit sockets, making closures cleaner and more reusable.

Example: Terrain generators can substitute custom procedural behavior for default tree scattering by using an Evaluate Closure node in place of fixed tree-distribution code. Expose the closure parameter through the group's interface, then build a Closure Zone in the main node tree that connects to this input. Within that zone, construct the desired tree-positioning logic. Upon evaluation, the generator runs the custom placement instead of the default behavior. A Closure Zone defining procedural distribution for tree scattering demonstrates this pattern.

### Closure

A closure encapsulates reusable node logic like a function.
Define inputs, outputs, and internal behavior executable elsewhere via Evaluate Closure.

Closures inject custom procedural logic into node groups—more modular, less duplication.
Instead of editing an existing group, expose user-defined behavior while preserving structure.

An empty closure zone.

### Inputs

Closures define their own inputs as function parameters.
Create them by dragging the blank input socket or adding in node properties.
Each input is a parameter the closure receives when evaluated elsewhere.

### Properties

No functional properties; configure via the Node tab in the Sidebar.
Add, remove, and rename inputs and outputs to set the signature.

**Sync Sockets**
Align the node to connected node signatures.
Use after socket rename, add, or remove.

**Define Signature**
Mark this zone as the closure signature source for reference by other nodes.
Ensures consistent input/output across instances.

### Input Items

**List of input sockets**
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

[Related references](INDEX.md).
