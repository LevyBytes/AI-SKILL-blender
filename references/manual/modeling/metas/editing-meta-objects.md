# Editing Meta Objects

## Editing Meta Objects

Meta objects can contain multiple distinct elements within a single object rather than distributing them across separate objects. Each element has its own shape and control properties.

In Edit Mode, selecting an element and pressing X or Del removes it; no extended options are available.

To convert a metaball surface into a standard mesh, use the Convert command from Object Mode.

Meta objects are organized into "families" based on the object name before the first period. For example, "MetaPlane.001" belongs to the MetaPlane family. Objects in the same family interact with one another.

Each family is controlled by a base meta object—the one whose name contains no period. If you have MetaThing, MetaThing.001, and MetaThing.round, the base is MetaThing. The base governs overall surface properties, geometric resolution, the field threshold, and spatial transformation, and it holds material and texture settings. Other metas in the family operate as child elements dependent on the base.

When organizing across multiple scenes, ensure the base meta remains in the same scene as its child metas to avoid rendering anomalies.

The base meta is visually identifiable by its orange mesh outline; child metas display black selection rings. Selecting any meta in a family highlights the entire family's surface.

The base meta controls how the overall surface is polygonalized (converted to mesh geometry). Transforming the base alters the mesh structure for all children. Transforming children, however, does not change the overall mesh structure—only the base's transformations recalculate it.

When the base is scaled down, the mesh subdivision increases while the shape remains the same; child mesh structures intensify their vertex density without changing their physical size.

[Related references](INDEX.md).
