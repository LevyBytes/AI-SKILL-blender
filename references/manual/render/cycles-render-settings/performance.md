# Performance

## Performance

### Performance

Reference

Panel :

Render ‣ Performance

Settings affecting render duration or memory requirements. Presets assist selection between speed-memory trade-offs:

Default :

Equilibrium between memory savings and faster rendering.

Faster Render :

Prioritizes rendering speed, increasing memory usage.

Lower Memory :

Decreases memory footprint, slowing renders.

### Threads

Threads Mode
Logic for determining maximum CPU cores during rendering.

Auto-Detect :

Automatically selects thread count matching logical processors on your system.

Fixed :

Manually specify maximum threads. Useful to reserve CPU capacity for other tasks—set below total logical processor count.

Threads
Maximum concurrent CPU cores during rendering.

### Memory

Tile Size
Render at high resolution in sections to cut memory usage. Sections cache to storage while rendering to preserve memory.

Note

In certain scenarios, Tile Size adjustment can improve performance. For instance, when a small object renders slowly relative to others, smaller tile sizes can accelerate performance.

### Acceleration Structure

Use Spatial Splits
Spatial divisions improve rendering with mixed polygon sizes. Downsides: longer BVH assembly and slightly elevated memory.

Use Curves BVH
Employ specialized BVH for curves. Bounding boxes adapt to curve shape more tightly than standard axis-aligned bounds. Disabling reduces memory at curve rendering cost.

BVH Time Steps
Subdivide BVH elements by this count to expedite rendering, consuming additional memory.

Use Compact BVH
Deploy tighter BVH design, shrinking RAM use but extending render time.

### Final Render

Persistent Data
Store render state post-rendering for quicker re-renders and animation sequences, consuming extra memory during other Blender work.

With multiple View Layers, one layer's data persists to limit memory; objects between layers still persist.

### Viewport

Pixel Size
Viewport rendering resolution management. Accelerates viewport, especially on high-DPI displays.

[Related references](INDEX.md).
