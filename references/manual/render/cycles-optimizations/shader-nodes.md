# Shader Nodes

## Shader Nodes

### Shader Nodes 

Cycles runs a slate of shader node optimizations at compile time and run-time both.
Lean on them and you can put together elaborate "Uber Shader" style node groups whose unused features cost barely any render time.

### Node Optimizations 

Step one in readying a node shader for execution is expanding every node group, as the Ungroup tool would, while tossing UI-only bits like frames and reroute nodes.

That done, it works through a handful of plain transformations; the sampling below is far from complete:

- Where every input of a node turns out constant, swap the node for the constant its evaluation yields. This covers:

RGB, Value, Mix RGB, Math, Vector Math, RGB to BW, Gamma, Bright Contrast,
Invert, Separate/Combine RGB/XYZ/HSV, Blackbody, RGB Curves, Vector Curves, Color Ramps.

- Spot Mix RGB, Math and Vector Math nodes that go no-op (Clamp off), or collapse to 0, once an addition, subtraction, multiplication, division or dot/cross product meets a known 0 or 1 input, and stand in the right link or constant.

- Drop a Mix RGB Mix (Clamp off) or Mix Shader node the moment Factor is pinned at 0 or 1, putting the matching input value or link in its place.

- Drop no-op Mix RGB nodes (barring Color Burn, Color Dodge, Lighten, or an enabled Clamp), plus Invert, RGB Curves and Vector Curves nodes, whenever their Factor is a known zero.

- Drop Emission and Background shader nodes that throw off no light, along with Add Shader nodes missing one or both input arguments.

- Drop a Bump whose Height input is constant, reaching for its Normal input or Geometry Normal in its stead. That helps when a node group input defaults to normal by passing through a no-op Bump ahead of the math.

- Swap Attribute nodes of the View Layer kind for the evaluated attribute value, which holds constant over the entire Render Layer.

- Fold several copies of one node sharing identical inputs down to a single instance.

Finally, any nodes left unconnected to the Output node, directly or indirectly, are dropped.

### Run-Time Optimizations 

A special optimization fires for Mix Shader nodes while shaders run.
Should Factor land on 0 or 1, the nodes reachable only down the mix's unused branch go unevaluated.

That can sharply cut the performance toll of folding several materials into one shader where a Color Attribute, texture, or other input plays the switch.

### Open Shading Language 

With Open Shading Language set as the rendering backend, node shaders translate into OSL code that the OSL runtime then compiles and runs.
Along the way it brings its own broad battery of optimizations to bear, at compile time and run-time alike.

Open Shading Language may optimize a Script node away when its outputs go unused or stay constant, even where its OSL shader carries side effects such as debug tracing and message passing, a result that can mislead. For that reason, to move data forward through the graph, steer clear of message passing with setmessage and getmessage; route the information explicitly through sockets instead.

[Related references](INDEX.md).
