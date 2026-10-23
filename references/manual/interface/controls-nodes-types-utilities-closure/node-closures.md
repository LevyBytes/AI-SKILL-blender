# Node Closures

## Node Closures

### Node Closures

Handing custom functionality into a node group is what a closure is for. It behaves much like a function input: user-defined behavior gets evaluated inside some other node tree.

Flexibility and reuse are what closures buy you, because a slice of one node network can be injected into another. That opens the door to higher-level tools where a particular stage of a process stays customizable while the group is left untouched.

A terrain generator whose tree scattering is tailored through a closure.

### Overview
A closure is a socket type standing in for a callable node graph. It declares its own inputs and outputs, which then get evaluated inside a different node group by way of the Evaluate Closure node.

Connect a closure and its internal graph is woven into the evaluation of the node group hosting it. Procedural systems can thus stay flexible while still offering clear, customizable control points.

Picture closures as function parameters that node groups accept. Users get to define operations that run inside a controlled environment set by the parent node tree.

### Nodes
These are the nodes that create and evaluate closures:

### Socket Syncing
Closure nodes line their inputs and outputs up by socket name. Wire together two whose signatures clash, and a sync can be offered to you by Blender.

- The first connection of a node triggers syncing on its own.

- To keep from clobbering user data, no existing socket is altered automatically.

- Detect a mismatch and a button (Sync Sockets) button appears in the node header for manual synchronization.

### Example
Closures shine wherever a portion of a node group's logic ought to be left to the user. Take a terrain generator that relies on a closure to set tree placement:

- Drop an Evaluate Closure node at the point where tree instances get scattered.

- Surface a closure input on the group's interface.

- Wire up a Closure node that lays out whatever custom placement logic you like.

Evaluate the closure and the connected graph's contents run inside the terrain generator's context. The generator can therefore handle stable infrastructure (scattering, masks, attributes) while users contribute their own functional behavior.

A terrain-generator node group that drives custom tree placement with closures.

### Node Closures

Pass custom functionality into a node group—a function parameter for node graphs.
Closures inject part of a network elsewhere, enabling higher-level tools with customizable logic.

Using a closure to customize tree scattering.

### Overview

Closures: a socket type representing callable graphs.
Define inputs and outputs evaluated via Evaluate Closure in another group.

When connected, the closure's graph injects into the evaluation context.
Procedural systems stay flexible with clear control points.

Closures resemble function parameters: users define operations in a controlled parent context.

### Nodes

Creation and evaluation nodes for closures.

### Socket Syncing

Names match closure inputs to outputs.
Mismatched signatures prompt automatic sync.

- First connection syncs automatically.
- Existing sockets never change auto-sync to prevent data loss.
- A Sync Sockets button appears in the header when mismatch is detected.

### Example

User-defined logic for specific workflow parts.
Terrain with custom tree placement:

- Evaluate Closure at tree distribution point.
- Expose closure input on the group interface.
- Closure node connects with custom logic.

Connected graph executes in the terrain generator context.
Generator provides stable infrastructure (scattering, masks, attributes); user supplies behavior.

Terrain generator with custom tree placement via closures.

[Related references](INDEX.md).
