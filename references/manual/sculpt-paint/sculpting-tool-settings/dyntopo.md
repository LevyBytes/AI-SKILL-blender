# Dyntopo

## Dyntopo

### Dyntopo

Reference

Mode :

Sculpt Mode

Panel :

Sidebar ‣ Tool ‣ Dyntopo

Dynamic Topology (Dyntopo) can be enabled via the checkbox. When active, most brushes subdivide the mesh as you sculpt.

For background on dynamic topology, see the Introduction.

Detail Size/Percentage, Resolution R
The detail level for each Detail Type is configured here. Depending on which Detail Type is in use, this displays as a pixel measurement (px) or percentage value.

R enables interactive detail adjustment with real-time density visualization in the 3D viewport.

Sample Detail Size
When using Constant Detail mode, you can sample the detail value from a specific mesh region by clicking the pipette icon next to the detail field and then clicking on that area.

Refine Method
This setting determines the topology adjustment technique applied.

Subdivide Edges :

Like the Subdivide operation, this subdivides topology to match the specified detail level.

Collapse Edges :

When geometry becomes excessively dense and falls below the detail specification, edges are collapsed to match the detail size.

Subdivide Collapse :

This combines both approaches, subdividing edges smaller than the detail size while collapsing overly dense areas.

Detailing
Dyntopo offers multiple detail creation methods to establish dynamic surface detail.

Relative Detail :

This approach bases detail on pixel count; as you zoom out, details appear coarser; zooming in reveals finer details.

Constant Detail :

This maintains uniform detail across the entire mesh. The detail represents a Blender unit divisor—larger values produce finer results.

Brush Detail :

This grants greater control by using brush size as the basis for topology generation. Increase or decrease topology by changing brush size. Full detail creates topology matching the brush radius.

Manual Detail :

Comparable to constant detail, this percentage-based approach only applies detailing when using Flood Fill.

Detail Flood Fill Ctrl - R
With Constant or Manual Detailing, this option activates and fills your whole mesh uniformly using the configured resolution value.

[Related references](INDEX.md).
