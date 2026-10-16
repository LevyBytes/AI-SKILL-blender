# Introduction

### Introduction

Simulating cloth is among the most challenging problems in computer graphics. At first glance, cloth seems straightforward—a daily-life object we ignore—yet its behavior involves intricate dynamics and environmental responses. Modeling fabrics, flags, and banners typically employs 2D meshes, though 3D representations work too for items like stuffed animals, cushions, inflatable objects, and spheres.

Fabric responds to forces, collisions, wind, and aerodynamic effects—all configurable to suit your needs.

| Description | Description | Description |
| --- | --- | --- |
| Cloth example.  | Cloth on carved wooden men (made by motorsep).  | Cloth example.  |

When cloth physics are activated on a mesh, the Cloth Modifier is appended to the object's modifier chain. As a modifier, it participates with others (Armature, Smooth) where the final shape results from the modifier sequence order. For instance, apply smoothing after the cloth computes its deformed state.

You can Apply the Cloth Modifier to finalize the mesh's current state at a specific frame, which removes the modifier itself. Suppose you drape cloth over a table, allow the sim to conclude, then apply the modifier—you've effectively used the simulator to reduce modeling work.

Simulation results store in a cache, so the mesh's calculated state at any frame needn't be recomputed. If changes are needed, you retain control over cache clearing and rerunning. The first simulation run is fully automatic—no baking step interrupts the process.

Background computation of mesh deformation at each frame occurs automatically, permitting continued work during calculation. Computation intensity depends on hardware and simulation detail; you'll notice lag corresponding to computational demand.

Note

Do Not Jump Ahead

If you create a cloth sim and Blender hasn't yet computed shapes through the duration, then advance many frames forward, the simulator may fail to show an accurate mesh state for that frame if prior frames haven't been processed.

### Workflow

A standard approach involves these steps:

- Model the cloth object with an initial shape.

- Classify the object as "cloth" in the Properties Physics tab.

- Design other objects that will obstruct the cloth.
Ensure the Deflection modifier appears last in the modifier chain, after any other deforming modifiers.

- Apply lighting, materials, textures, and unwrap UVs if needed.

- Optionally add particle effects such as steam from the surface.

- Execute the simulation and refine parameters until results satisfy you.
The Timeline editor's playback controls excel in this phase.

- Consider aging the mesh to a point in the sim to create a new default starting posture.

- Make frame-by-frame mesh adjustments to remedy minor defects.

Tip

To prevent unstable behavior, ensure the cloth object doesn't intersect any deflection objects beforehand.

### Springs

Internally, cloth simulation employs virtual springs linking mesh vertices. Four spring types regulate cloth bending, each detailed below and shown in the accompanying image:

Illustration of cloth springs; tension springs (blue),
compression springs (red), shear springs (cyan),
and angular bending springs (green). 

Tension Springs
Establish cloth rigidity against pulling.

Compression Springs
Determine resistance to collapsing or squashing.

Shear Springs
Like compression springs, but manage angular warping.

Angular Bending Springs
Govern resistance to folding and crumpling.

These four spring varieties can be tuned independently in the Physical Properties panel. While these handle surface springs, internal springs are an option for 3D meshes and behave akin to Soft Bodies.

[Related references](INDEX.md).
