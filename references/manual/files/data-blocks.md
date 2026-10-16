# Data-Blocks

## Data-Blocks

The basic unit of any Blender project is the data-block. Meshes, objects, materials, textures, node trees, scenes, texts, brushes, and even Workspaces are all examples. A data-block is a generic abstraction over very different kinds of data, sharing a common set of basic features, properties, and behaviors. Some common traits:
- They make up the bulk of the blend-file.
- They can point at one another for reuse and instancing (child/parent, object/object-data, materials/images, and within modifiers or constraints too…).
- Within a blend-file, each type keeps its own unique names.
- They can be added, removed, edited, and duplicated.
- They can be linked between files (only for a limited set of data-blocks).
- They can carry their own animation data.
- They can hold Custom Properties.
Usually you interact with the higher-level data types (objects, meshes, etc.); managing data-blocks matters more on complex projects, especially when inter-linking blend-files, and the main editor for that is the Outliner. Not everything in Blender is a data-block — bones, sequence strips, and vertex groups, for instance, aren't — they belong to the armature, scene, and mesh types instead.

Data-Block Types — for reference, here are the data-block types stored in blend-files. Link means it supports being linked into other blend-files; Pack means its file contents can be packed into the blend-file (not applicable to most data-blocks, which have no file reference).
- Action (Link ✓, Pack —) — stores animation F-Curves; used as data-block animation data and in the Nonlinear Animation editor.
- Armature (✓, —) — a skeleton for deforming meshes; used as armature-object data and by the Armature Modifier.
- Brush (✓, —) — used as brush assets in sculpt and paint modes.
- Cache File (✓, —) — used by Mesh Cache modifiers.
- Camera (✓, —) — used as data by camera objects.
- Collection (✓, —) — groups and organizes objects in scenes; used to instance objects and in library linking.
- Curve (✓, —) — used as data by curve, font, and surface objects.
- Curves (✓, —) — the new curve data type (replacing Curve).
- Font (✓, ✓) — references font files; used by the curve object-data of text objects.
- Grease Pencil (✓, —) — 2D/3D sketch data for Grease Pencil objects; also overlay helper info in the 3D Viewport, Image, Sequencer, and Movie Clip editors.
- Grease Pencil v3 (✓, —) — as above, for Grease Pencil objects, with the same overlay uses.
- Image (✓, ✓) — image files; used by shader nodes and textures.
- Key (Shape Keys) (Link ✗, —) — geometry shape storage that can be animated; used by mesh, curve, and lattice objects.
- Lattice (✓, —) — grid-based lattice deformation; used as lattice-object data and by the Lattice Modifier.
- Library (✗, ✓) — a reference to an external blend-file; reached from the Outliner's Blender File view.
- Light (✓, —) — used as object data by light objects.
- Light Probe (✓, —) — helps achieve complex real-time lighting in EEVEE.
- Line Style (✓, —) — used by the Freestyle renderer.
- Mask (✓, —) — 2D animated mask curves; used by compositing nodes and sequencer strips.
- Material (✓, —) — sets shading and texturing render properties; used by objects, meshes, and curves.
- Mesh (✓, —) — geometry of vertices/edges/faces; used as mesh-object data.
- Metaball (✓, —) — an isosurface in 3D space; used as metaball-object data.
- Movie Clip (✓, Pack ✗) — a reference to an image sequence or video file; used in the Movie Clip editor.
- Node Tree (✓, —) — groups of reusable nodes; used in the node editors.
- Object (✓, —) — an entity in the scene with location, scale, rotation; used by scenes and collections.
- Paint Curve (✓, —) — stores a paint or sculpt stroke; reached from the paint tools.
- Palette (✓, —) — stores color presets; reached from the paint tools.
- Particle (✓, —) — particle settings; used by particle systems.
- Point Cloud (✓, —) — a collection of points in 3D space.
- Scene (✓, —) — the primary store of all displayed and animated data; top-level storage for objects and animation.
- Screen (✓, —) — low-level user-interface storage.
- Sound (✓, ✓) — a reference to sound files; used as speaker-object data.
- Speaker (✓, —) — sound sources for a 3D scene; used as speaker-object data.
- Text (✓, ✗) — text data; used by Python scripts and OSL shaders.
- Texture (✓, —) — 2D/3D textures; used by brushes and modifiers.
- Volume (✓, —) — volumetric objects that hold grids of data.
- Window Manager (✗, —) — the overarching manager for all of Blender's UI, covering Workspaces, the notification system, operators, and keymaps.
- Workspace (✗, —) — a UI layout; each window has its own workspace.
- World (✓, —) — defines global render environment settings.

Life Time — each data-block keeps a tally of how many users it has (a reference count); when there's more than one, the current count shows to the right of its name in the interface. As a general rule, Blender eventually removes unused data.

Since you add and remove plenty of data while working, this saves you from hand-managing every single data-block; it works by skipping zero-user data-blocks when writing blend-files.

Protected — because zero-user data-blocks aren't saved, sometimes you want to force data to stick around regardless of its users. If you're building a blend-file as an asset library to link to and from other files, you'll want to make sure those assets aren't accidentally dropped from the library file. To protect a data-block, use the shield-icon button beside its name; Blender then never silently deletes it, though you can still remove it by hand. Note: linked data can't be protected this way.

Name & Rename — data-block names are unique within their namespace, where a namespace is set by the type and the blend-file it lives in. So an Object and a Mesh can share a name, but two local objects in one blend-file can't; you can, however, have one local and several linked Objects sharing a name. Names have a fixed length of 255 bytes — 255 basic ASCII characters, or fewer with diacritics or non-Latin glyphs, since UTF-8 then often uses more than one byte per character. When naming a new data-block or renaming one, Blender checks for collisions; if a data-block of that name already exists, the (re)named one gets a numeric suffix on its "root name", like .001, using the first free index (up to 999, after which the suffix just keeps incrementing until no collision remains). If the suffix would make the name too long, the root part is trimmed as needed. Blender never renames a different data-block during automatic naming, so adding a new Cube object when Cube and Cube.001 already exist locally names the new one Cube.002.
You can rename local data-blocks yourself in a number of UI spots (the ID selection widget, the Outliner, and so on). On a name collision from the UI:
- If the new root name differs from the original, the renamed data-block takes the first free numeric suffix — e.g. with objects Sphere, Cube, and Cube.001, renaming Sphere to Cube yields Cube.002.
- If the new root name matches the original, the renamed data-block gets the requested name and the conflicting one is renamed instead — e.g. with Sphere, Cube, and Cube.001, renaming Cube.001 to Cube makes it Cube and turns the other into Cube.001.
Dot-Prefixed Names (Hidden Data) — data-block names beginning with a dot (.) count as hidden. Hidden data-blocks aren't shown in File Browsers by default, hide in most data-block selection menus, and are commonly used for internal, temporary, or helper data; the convention marks implementation details users shouldn't normally pick or edit directly. You can reveal them through preferences: enable Defaults – Show Hidden Files/Data-Blocks to show dot-prefixed data-blocks in File Browsers and data ID selectors, and Search – Show Hidden to show them in search menus. Even while hidden from the interface, a dot-prefixed data-block still acts like any other for linking, usage counting, and saving.

Sharing — data-blocks can be shared among others. Common cases: sharing textures among materials, sharing meshes between objects (instances), and sharing animated actions between objects (to dim all the lights together, say). Data-blocks can be shared across files as well; see linked libraries.

Making Single User — when a data-block is shared by several users, you can make one user its own copy by clicking the user-count button to the right of its name; this duplicates the data-block and assigns the new copy to that use alone. Note: objects have more advanced routes to single-user status — see their docs.

Removing Data-Blocks — as Life Time explained, data-blocks normally vanish once unused; you can also unlink or delete them by hand. Unlinking means a user stops using it, done by clicking the "X" icon next to a data-block's name; unlink it from every user and Blender eventually deletes it as above (unless it's protected). Deleting erases it from the blend-file outright, unlinking it from all users at once, done with Shift-LMB on the "X" icon. Warning: deleting some data-blocks can delete their users, which would be invalid without them — chiefly, deleting object-data (mesh, curve, camera…) also deletes every object using it. Both operations are also in the context menu when you RMB a data-block in the Outliner.

[Related references](INDEX.md).
