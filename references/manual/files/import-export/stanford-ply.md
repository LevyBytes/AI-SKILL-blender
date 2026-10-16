# Stanford PLY

## Stanford PLY

Reference — Category: Import-Export; Menu: File ‣ Import/Export ‣ Stanford (.ply).

Use the operator to import ASCII or binary PLY-files, picking several files at once; for export you can enable or disable the modifiers and choose which data to export (UV textures, Color Attributes, …).

Import — General — Scale: how much to scale the imported objects about the world's origin.
Scene Unit — applies the current scene's unit (per its unit scale) to the imported data.
Forward Axis, Up Axis — since many apps treat a different axis as "Up", these remap the Forward and Up axes to convert rotations between another app's default up/forward and Blender's. Blender itself uses Y Forward, Z Up (its front view looks along +Y); an app that uses Y as up needs -Z Forward, Y Up.
Options:
Merge Vertices — tries to combine co-located vertices where it can.
Import Vertex Colors — the color space the PLY's color data was saved in. None (skip vertex color data), sRGB (file's vertex colors are in sRGB Color Space), or Linear (file's vertex colors are in Linear Color Space).

Export — General — Format: ASCII: writes the file in the simple ASCII format, useful when the importing program lacks binary support.
Include: Selected Only — export only selected objects; instanced objects (a collection instanced in the scene, say) count as "selected" when their instancer is.
Scale — how much to scale the exported objects about the world's origin.
Forward Axis, Up Axis — as on import: these remap the Forward and Up axes to convert rotations between another app's default up/forward and Blender's. Blender itself uses Y Forward, Z Up (its front view looks along +Y); an app that uses Y as up needs -Z Forward, Y Up.
Geometry:
UV Coordinates — writes out the active UV layer's coordinates from Blender.
Vertex Normals — writes out Blender's face and vertex normals (per the faces' smooth setting); usually unneeded since most apps compute their own, but required to match Blender's normal-map textures.
Vertex Colors — the color space the PLY's color data was saved in. None (skip vertex color data), sRGB (in sRGB Color Space), or Linear (in Linear Color Space).
Triangulated Mesh — triangulates every N-gon of four or more vertices (the scene's meshes are untouched), behaving like the Triangulate Modifier set to N-gon Method "Beauty", Quad-method "Shortest Diagonal", Min vertices 4.
Apply Modifiers — exports objects as their evaluated mesh, i.e. the mesh that results once every Modifier has been computed.

[Related references](INDEX.md).
