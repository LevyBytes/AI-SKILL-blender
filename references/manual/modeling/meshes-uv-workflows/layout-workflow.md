# Layout Workflow

## Layout Workflow

When unwrapping a complete model at once, the result often appears disorganized. Dense areas like facial structure may compress heavily, while appendages like necks and ears stretch disproportionately. Rather than correcting an unwrap manually, re-unwrapping the model in segments using appropriate projection methods typically yields better results.

Separate the visible head region—excluding eye details, ear protrusions, and neck—and apply Sphere Projection to it. For the ear section, align the viewport directly to its surface and use Project from View. The UV coordinates for already-unwrapped parts remain stored; if the editor shows only current selections, toggle Sync Selection to display all islands.

Unwrap the neck using Cylinder Projection. As an alternative workflow, use Seams to delineate cut boundaries around protruding features, then run Unwrap once to map all sections simultaneously.

After unwrapping separate pieces, individual UV islands often overlap. To remediate this: select a single vertex and press Ctrl-L to select its topologically connected region (or hover and press L, or switch to Island mode). Once selected, scale and reposition the island away from others. Alternatively, use Pack Islands to have the system arrange them automatically.

Consolidate separate islands by translating and scaling them to fit together, then merge them using either Merge or (preferably) Stitch operations.

Once basic unwrapping is done, manual adjustments often improve results. Scaling up a region allocates more texture resolution to it, enabling finer detail. The Minimize Stretch tool helps correct excessive distortion between the 2D UV layout and its corresponding 3D surface.

A single geometry can hold multiple UV layers, each assigning different coordinates to the same vertices. This enables separate maps for color textures and for pre-computed shading information.

UV maps can be transferred between geometries in various ways. For identical topologies with differing vertex locations, use Copy UV Maps. For approximately matching surfaces with different topology, apply Transfer Mesh Data.

[Related references](INDEX.md).
