# STL

## STL

Reference - Category: Import-Export; Menu: File ‣ Import/Export ‣ Stl (.stl).

The STL-file format is handy when you mean to import/export files for CAD software, and it's also common for loading into 3D-printing software.

Importing — General — Scale: how much to scale the imported objects about the world's origin.
Scene Unit: applies the current scene's unit (per its unit scale) to the imported data.
Forward / Up Axis: since many apps point a different axis upward, these remap the Forward and Up axes to convert rotations between another app's default up/forward and Blender's. Blender itself uses Y forward, Z up (its front view looks along +Y); an app that uses Y as up needs -Z forward, Y up.
Options:
Facet Normals: uses (imports) facet normals (this still gives flat shading).
Validate Mesh: checks the imported mesh for corrupt data and repairs it if needed; with it off, bad data may crash display or editing. It slows importing but is recommended, since data errors aren't always obvious.

Exporting — General — Format: ASCII: exports the stl-file as ASCII rather than binary.
Batch: exports each object as its own STL file.
Include: Selection Only — when checked, exports only selected objects; instanced objects (a collection instanced in the scene, say) count as "selected" when their instancer is.
Scale: how much to scale the exported objects about the world's origin.
Scene Unit: applies the current scene's unit (per its unit scale) to the exported data.
Forward, Up: since many apps treat a different axis as "Up", these remap the Forward and Up axes to convert rotations between another app's default up/forward and Blender's. Blender itself uses Y Forward, Z Up (its front view looks along +Y); an app that uses Y as up needs -Z Forward, Y Up.
Geometry:
Apply Modifiers: exports objects as their evaluated mesh, i.e. the mesh that results once every Modifier has been computed.

[Related references](INDEX.md).
