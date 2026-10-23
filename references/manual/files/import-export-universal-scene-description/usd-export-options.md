# Usd export options

Exporting to USD Files: USD files can hold complex layering, overriding, and references to other files, but Blender's USD Exporter takes a far simpler tack: on export it writes every visible, supported object in the scene, optionally narrowed by selection, and doesn't (yet) export invisible objects, USD layers, variants, and the like. These objects can be exported to USD:
- Meshes (of several kinds, see below).
- Cameras (perspective only for now, not orthographic).
- Curves.
- Text (written as meshes).
- Lights.
- Hair (written as curves, limited to parent strands).
- Point Clouds.
- Metaballs (written as animated meshes).
- Volumes.
- Armatures.
Exporting an animation writes the final evaluated mesh to USD, so these meshes can be exported: static meshes; deforming meshes, where the topology stays put while the vertices move over time (animated characters, or bouncing-but-not-cracking objects); and arbitrarily animated meshes, where the topology does change (a fluid sim where splashes break off the main body, say).
Note: to export the Blender scene as a USDZ archive, give the output file the .usdz extension; the resulting USDZ package is a zip archive holding the USD and its texture dependencies.

Export Options: these are available when exporting to USD.
General:
Root Prim: if set, adds a transform primitive at the given path as the parent of all exported data on the stage.
Include: Selection Only (when checked, only selected objects export; an instanced object, such as a scene-instanced collection, counts as "selected" when its instancer is) and Animation (checked, the whole scene frame range exports; unchecked, only the current frame).
Blender Data - Custom Properties: exports Custom Properties as USD attributes, with the Namespace property setting the namespace they're written to. Namespace: if set, prefixes that namespace onto exported custom-property names, but only those without a prefix already (so it'd apply to name bar, not foo:bar) and never to Blender object and data names, which always go in the userProperties:blender namespace; userProperties is the default. Blender Names: writes USD custom attributes carrying the original Blender object and object-data names. Allow Unicode: keeps UTF-8 characters in USD prim and property names (the resulting files need software on USD 24.03 or newer to open).
File References - Relative Paths: references external files (textures, volumes) by relative path in the exported USD, otherwise by absolute path.
Convert Orientation: converts the orientation axis to another convention to suit other apps. Blender uses Y Forward, Z Up (its front view looks along +Y); an app that uses Y as up, for instance, needs -Z Forward, Y Up.

Forward / Up Axis: remap these to different axes to convert rotations between another app's default up/forward and Blender's.
Units: sets the USD Stage metersPerUnit metadata to the chosen measure.
Meters Per Unit: the value to use for metersPerUnit when Custom Units is chosen.
Xform Ops: which transform operators carry a prim's transform. Translate, Rotate, Scale (export with translate, rotate, and scale Xform operators), Translate, Orient, Scale (translate, orient quaternion, and scale operators), or Matrix (a single matrix operator).
Use Settings for: whether export uses each object's Viewport or Render visibility, modifier settings, and other such properties.

Object Types:
Meshes: exports Mesh Objects.
Lights: exports Light Objects; the UsdLuxShapingAPI backs spot lights.
World Dome Light — converts the world material to a UsdLuxDomeLight; this works for now on simple materials — an environment texture wired to a background shader, optionally with a vector multiply of the texture color.
Cameras: exports Camera Objects; perspective cameras only.
Curves: exports Curve Objects.
Point Clouds: exports Point Cloud Objects.
Volumes: exports Volume Objects.
Hair: exports parent hair strands as a curve system; strand colors aren't exported.
Note: the USD schema type used on export mirrors the one read on import; see the Import section for details.

Geometry:
UV Maps: when checked, carries UV coordinates along for exported meshes, the USD UV map keeping the Blender name.
Rename UV Maps: exports UV maps under the USD default name (st) instead of Blender's default (UVMap).
Normals: when checked, includes normals for exported meshes, custom loop normals included.
Merge parent Xform: merges USD primitives with their Xform parent where possible; since USD forbids nested UsdGeomGprims, intermediary Xform prims are defined to keep the file valid across object hierarchies.
Triangulate: triangulates the mesh before writing; for the specific option, see the Triangulate modifier.

Rigging:
Shape Keys: exports shape keys as USD blend shapes; absolute shape keys aren't supported.
Armatures: writes Armatures, and meshes carrying Armature Modifiers, out as USD skeletons and skinned meshes. Limitations: modifiers beyond Armature modifiers aren't applied, and bendy bones aren't supported.
Only Deform Bones: exports only deform bones and their parents.

Materials: exports an object's material info; out of the box the exporter approximates the Principled BSDF node tree, recasting it into USD's Preview Surface format. When a mesh carries several materials, a geometry subset is made per material, and the first material, if there is one, also goes on the mesh itself no matter what subsets exist, because the Hydra viewport doesn't support materials on subsets (see USD issue #542). Note: with USD Preview Surface Network and MaterialX Network both off, the material is set to the meshes' viewport materials.
Displacement Support - displacement works with caveats: only object-space displacement (no vector displacement); Midlevel and Scale must be constants; and MaterialX isn't supported yet (see the feature commit).
USD Preview Surface Network — approximates a Principled BSDF node tree by recasting it into USD's Preview Surface format. Note: to support opacityThreshold (a.k.a. "Alpha Clip"), the node tree must either include a Math node set to Round (when the threshold is 0.5) or a pair of Math nodes computing 1 - (value < threshold), with the result plugged into the Principled BSDF's Alpha socket. Warning: not all nodes are supported — for now only simple trees of Diffuse BSDF, Principled BSDF, Image Textures, UVMap, and Separate RGB nodes work.
MaterialX Network: builds material shading graphs in the MaterialX standard, which is designed for high interoperability among DCCs &lt;Digital Content Creation&gt;; in Blender, MaterialX covers most shader nodes and their behavior, with a few caveats below. Implementation Caveats: with the Principled BSDF the resulting graph is very usable, but some of the other BSDFs produce graphs other DCCs find hard to read.
Export Textures: how textures are exported. Keep (use the textures' original location), Preserve (keep file paths of textures from already-imported USD files, and write the rest to a 'textures' folder beside the USD), or New Path (write textures to a 'textures' folder beside the USD).
Overwrite Textures: allows overwriting existing texture files on export.
USDZ Texture Downsampling: a maximum size for all exported textures. Keep (current sizes), 256, 512, 1024, 2048, or 4096 (cap at that many pixels), or Custom (a size you set).
USDZ Custom Downscale Size: the pixel size for Custom downsampling.

Accessibility:
Label: the accessibility label for the exported stage's default prim.
Description: the accessibility description for the exported stage's default prim.
See USD UI Accessibility for more.

Experimental:
Instancing: an experimental option. Unchecked, duplicated objects export as real objects, so a 100-particle system drawn with 100 meshes yields 100 individual meshes in the file; checked, duplicated objects export as a reference to the original, and if the original isn't part of the export, the first duplicate exports as a real object and serves as the reference.

Exporter Limitations:
Single-sided and Double-sided Meshes: USD appears to handle neither per-material nor per-face-group double-sidedness, so Blender takes the flag from the first material to mark the whole mesh single- or double-sided; with no material it defaults to double-sided.

Materials: with several materials, the mesh faces are stored as geometry subsets and each material is assigned to its subset; with only one material this is skipped. Note that the geometry subsets aren't time-sampled, so things may break if an animated mesh changes topology.
Hair: only the parent strands export, and only with a constant color: no UV coordinates and no normal information.
Camera: only perspective cameras export.
Particles: particles are written only while alive, meaning they're always visible; there's currently no code to mark them invisible outside their lifespan. Objects instanced by a particle system export with the object name suffixed by the particle's persistent ID, so every particle transform gets a unique name.
Geometry Node Modifiers — with Geometry Nodes, the node graph has to emit only the geometry components that match the original object type — to export a Mesh that uses a geometry-nodes modifier correctly, the modifier's output must hold only Mesh data, a Curves object only Curves data, and so on; any non-matching component yields a wrong export. The Separate Components Node is one way to make sure only the components you want export.
Instancing/Referencing — exporting instanced objects and collections is supported via an experimental USD-export option. Point instances made with Geometry Nodes are partly supported and export using the UsdGeomPointInstancer prim type; simple instancing through the Object Info Node or Collection Info Node works, but trickier cases — excluded collections, nested collections, or collections inside different Scenes — may come out wrong, so consider the Realize Instances Node where instances export incorrectly. Scene instances, made by directly instancing collections or objects, are written to USD as references to the original; supported types are Mesh, Curves, and Point Clouds.
USDZ: owing to a current USD-library limit, UDIM textures can't be included in the USDZ archive; this will likely be fixed in a future USD version (see USD pull request #2133).

[Related references](INDEX.md).
