# Introduction

### Introduction

Geometry Nodes is a node-based modifier system for altering object geometry. Add a Geometry Nodes Modifier and configure nodes in the Geometry Node Editor to use it.

Modifier properties in the modifier stack are shown visually.

A node tree linked to a modifier is a Node Group. Geometry from before the modifier (original or prior-modifier output) enters the Group Input node. The node group processes it and outputs to Group Output, feeding the next modifier.

Geometry Nodes works on multiple geometry types:

- Meshes

- Curves

- Point Clouds

- Volumes

- Instances

See Modifier page for modifier interface details.

For expanding Blender with operator-building nodes, see Node-Based Tools.

3D scenes require at least three key components: Models, materials, and lights. This section covers modeling—the art and science of creating surfaces that mimic real-world shapes or express imaginative abstractions.

Modeling Modes — Depending on object type, different modes apply. Cross-mode switching during modeling is common; some tools exist in multiple modes, others are mode-specific.

Edit Mode: Primary modeling context. Used to edit meshes, curves, surfaces, metaballs, text objects, lattices. Only mesh modification occurs; to edit other objects, exit Edit Mode, select, and re-enter, or use Multi-Object Editing.

[Related references](INDEX.md).
