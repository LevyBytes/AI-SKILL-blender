# Alembic

## Alembic

From the Alembic home page: Alembic is an open framework for computer-graphics interchange that distills complex, animated scenes down to a non-procedural, application-independent set of baked geometric results — a "distillation" of scenes into baked geometry exactly analogous to distilling lighting and rendering scenes into rendered image data. Alembic concentrates on efficiently storing the computed results of complex procedural geometric constructions; it deliberately doesn't concern itself with storing the complex dependency graph of procedural tools that made those results. It will, for example, efficiently store the animated vertex positions and transforms produced by an arbitrarily complex animation and simulation process — enveloping, corrective shapes, volume-preserving sims, cloth and flesh sims, and so on — but won't try to store a representation of the computation network (the rigs, basically) needed to produce those final positions and transforms.

In short, Alembic can save an animated mesh to disk and load it back fast and efficiently, so a mesh animated with a very CPU-heavy rig can be "baked" to an Alembic file and later loaded into the shot file for shading and lighting with only moderate CPU use. Thanks to the open-source nature of both the Alembic standard and its C++ implementation, Blender fits into a hybrid pipeline: other software such as Houdini or Maya can export to Alembic for loading, shading, and rendering in Blender, and you can equally animate characters or other models in Blender, export to Alembic, and load them into other software for further work.

Importing Alembic Files — on import, Mesh Sequence Cache modifiers are added automatically to time-varying meshes, and for time-varying object transforms (animated rotation, location, or scale) the Transform Cache Constraint is used.
General — Scale: how much to enlarge or shrink the objects about the world's origin.
Options:
Relative Path — pick the file relative to the blend-file.
Set Frame Range — if checked, updates the scene's start and end frame to match the Alembic archive's.
Is Sequence — set true when the cache is split across separate files.
Validate Meshes — checks the imported mesh for corrupt data and repairs it if needed; with it off, bad data may crash display or editing. It slows importing but is recommended, since data errors aren't always obvious.
Always Add Cache Reader — adds cache modifiers and constraints to imported objects even when they aren't animated, so they can update when the Alembic archive is reloaded.

Exporting to Alembic Files — this section covers what the export options do.
General — Scale: sets the Alembic file's global scale; keep it at the default 1.0 to use Blender's units.
Include – Selection Only — on, exports only the selected objects; off, all objects.
Scene — Frame Start, End: the frame range to export, defaulting to the current scene range.
Sub-frame Sampling — controls sub-frame sampling of animations.
  Samples Transform — Transform Samples sets how many times per frame animated transforms are sampled and written.
  Geometry — Geometry Samples does the same for animated geometry.
  Shutter Open, Close — define the [open, close] interval the samples span, valid from -1 to 1, where -1 is the previous frame, 0 the current, and 1 the next. To capture detailed mesh motion blur, for instance, you can write subframes around the current frame with a sample count of 5, Shutter Open set to -0.25 and Shutter Close to 0.25 — mimicking a "180 degree" shutter that opens 90 degrees before the frame and closes 90 degrees after.
Use Instancing — exports duplicated or instanced objects as Alembic instances, speeding the export; disable it for compatibility with other software.
Custom Properties — on by default, exports custom properties to Alembic too. Supported types:
  - Numbers (int, float) and strings, exported as single-element arrays, so 47 exports as [47] and "Agent" as ["Agent"], matching many other DCCs.
  - Lists of numbers and strings, exported as-is, so [327, 47] stays [327, 47].
  - Matrices and nested number arrays, flattened into one long list, so a 3×2 matrix becomes 6 numbers and nested [[1, 2, 3], [4, 5], [6]] becomes [1, 2, 3, 4, 5, 6].
  - Numbers can be animated too.
Flatten Hierarchy — off, parent/child relations are exported too, and any unexported parent with exported children is replaced by an empty; on, those relations aren't exported and all transforms are written in world coordinates.
Settings — sets which visibility, modifier, and other viewport-versus-render settings to use. Render (use Render settings) or Viewport (use Viewport settings).
Geometry — UV Coordinates: on, exports UV maps; although Alembic itself supports just one UV map, Blender exports all of them in a way other software should read.
Merge UVs — on, UVs sharing a vertex and location merge into one, shrinking the file slightly.
Normals — on, exports an object's Normals. See Custom Split Normals of Meshes below.

Color Attributes — on, exports Color Attributes.
Face Sets — exports the material name per face (only the names, not the material data).
Subdivisions:
Apply — bakes in any Subdivision Surface modifiers before the write to Alembic.
Use Schema — writes polygonal meshes with the "SubD" Alembic schema instead of "PolyMesh", setting an import hint for the opening program to apply its own non-destructive subdivision.
Triangulate — triangulates the mesh before writing; for the specific option, see the Triangulate modifier.
Particle Systems — Alembic has no Particle System support, just as it has none for armatures.
Export Hair — hair goes out as animated zero-width curves.
Export Particles — particles go out as animated points.

Custom Split Normals of Meshes — Blender can import and export custom normals to Alembic files. As a rule of thumb, a fully smooth mesh exports without normals and so makes the smallest Alembic file, and the importer mirrors this: an Alembic mesh with no normals loads as smooth.
On export, for each mesh: with Custom Loop Normals, those loop normals are written; if any polygon is flagged flat, loop normals go out too; otherwise none are.
On import, when the Alembic mesh holds: loop normals (kFacevaryingScope) become custom loop normals; vertex normals (kVertexScope or kVaryingScope) convert to loop normals and are handled as above; no normals means the mesh is marked smooth; and unsupported normal types (kConstantScope, kUniformScope, kUnknownScope) are treated as no normals. When an imported mesh has no normals, the final look can be steered with the Normal's Shading.

Handling Time — unlike Blender and many other apps and formats, Alembic files have no notion of frames; Alembic works purely in time and values sampled over time, so there's no way to tell 30 FPS with 2 samples per frame apart from 60 FPS with 1 sample per frame, which has led many developers to simply hard-code 24 FPS when reading Alembic files. Blender instead leans on the current scene's frame rate to turn a frame number (in Blender) into a time in seconds (in Alembic), so you can import a 120 FPS Alembic file into a 30 FPS Blender scene and still see no time stretching.

[Related references](INDEX.md).
