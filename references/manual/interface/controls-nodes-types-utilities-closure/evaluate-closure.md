# Evaluate Closure

Evaluate Closure runs the node graph of a connected Closure Zone and returns its results.
It lets a reusable node group accept custom behavior, such as scattering, placement, or shading logic,
without hard-coding that behavior into the group.

## Inputs and interface

Connect a Closure Zone to the Closure input. Inputs and outputs pair by socket name.
You can add inputs manually; connecting a closure synchronizes the interface with its declared sockets.
Without a closure, the node uses the pass-through behavior described below.

## Properties and socket items

The node has no functional properties. Manage its interface in the Sidebar's Node tab.

- Sync Sockets aligns the interface with the connected closure after sockets are renamed, added, or removed.
- Define Signature makes this node define the signature that related closure nodes follow.
- Input Items and Output Items list the sockets, one row per socket. Double-click a name to rename it.
- Add Item adds a socket; Remove Item deletes the selected socket.
- Type chooses a socket's data type, such as Float, Vector, Geometry, Object, or Bundle.
- Value sockets expose a default value that is used when the socket is unconnected.
- Shape chooses the data structure, such as a single value, field, or grid, and affects evaluation. See Socket Shape.

## Outputs and evaluation

With a closure connected, outputs correspond to same-named outputs of its Closure Zone.
With no closure, define the outputs in the Sidebar's Output Items.

Evaluation passes input values into the closure by name and returns values through matching output sockets.
If the closure is missing or the node is muted, matching inputs pass directly to the outputs.
This makes the closure optional while leaving the surrounding group usable.
Evaluation uses the containing node tree's local fields, attributes, and geometry.

## Usage

For a customizable terrain generator, replace fixed tree-placement logic with Evaluate Closure,
expose the Closure input on the generator group, and connect a Closure Zone in the main node tree.
Each evaluation runs the supplied placement graph in the terrain generator's context.
The same pattern supports reusable effects and optional customization on higher-level tools.

## Synchronization and limitations

A mismatched socket signature produces a sync icon. Use it to align the interfaces.
The first connection synchronizes automatically. Later changes do not alter existing sockets automatically,
which protects existing data.

- Viewer and inspection results may be inaccurate across multiple evaluation contexts.
- Captured external values are read-only.
- Closures cannot access attributes or data beyond their evaluation context.

[Related references](INDEX.md).
