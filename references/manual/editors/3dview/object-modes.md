# Object Modes

## Object Modes

Modes let you edit different facets of objects: Object Mode handles position, rotation, and scale; Edit Mode changes geometry; Pose Mode handles posing; and so on.

Switch the active mode with the Mode selector in the 3D Viewport header. Which modes are offered depends on the object's type, and the full list appears below. Besides the selector, pressing Ctrl-Tab pops a pie menu around the cursor for faster access (with an Armature selected, that shortcut instead toggles Object Mode and Pose Mode), and Tab toggles Edit Mode for objects that support it.

Modes can change a lot in Blender:
Each mode swaps the header and Toolbar for its own menus and tools, which also alters the available keyboard shortcuts.
A mode can transform the viewport's appearance — Weight Paint mode, for instance, shades the object to expose its vertex weights, normally invisible.
A mode can reach into other editors — the UV Editor works only while the 3D Viewport is in Edit Mode, and in the Properties editor certain buttons and panels are restricted to particular modes.

Object Mode List:
Object Mode — the default mode, present for every object type; handles position, rotation, scale, duplication, and so on.
Edit Mode — for editing an object's shape (vertices/edges/faces on meshes, control points on curves/surfaces, points/strokes on Grease Pencil, etc.).
Sculpt Mode — an alternative toolset for reshaping an object (meshes only).
Vertex Paint Mode — a mesh-only mode for setting a mesh's vertex colors (i.e. "painting" them).
Weight Paint Mode — a mesh-only mode devoted to vertex-group weighting.
Texture Paint Mode — mesh-only; lets you paint a texture directly onto the model within the viewport.
Particle Edit Mode — mesh-only; geared toward particle systems, handy for editable ones such as hair.
Pose Mode — armature-only; used for posing.
Draw Mode — a Grease Pencil mode for laying down new strokes.
Sculpt Mode (Grease Pencil) — reshapes existing Grease Pencil strokes in a more organic fashion.
Edit Mode (Grease Pencil) — works on the individual points and strokes that make up a Grease Pencil object.
Vertex Paint Mode (Grease Pencil) — applies color straight to the vertices of strokes.
Weight Paint Mode (Grease Pencil) — assigns vertex weights onto strokes.
Note: the cursor turns into a brush in Paint and Sculpt Modes. The modes' actual usage is covered in their own sections rather than here.
Hint: if this manual mentions a button or menu option you can't find on screen, you may simply not be in the mode that makes that option valid.

Switching Objects — Reference: Mode: All Modes; Shortcut: Alt-Q. Say you switch into a mode like Weight Paint and then click a different object: Blender will usually revert to Object Mode, so weight-painting that second object means entering the mode again. There's a way around this: once you're in a mode, the Outliner shows a dot beside other objects that also support it, and clicking that dot moves you to the other object without leaving the mode. Alternatively, point the cursor at the other object in the viewport and tap Alt-Q. See also Lock Object Modes for guarding against accidental mode changes.

Multi-Object Editing — Edit Mode and Pose Mode go further, letting you keep several objects in the mode simultaneously. Two ways to do it: if you're not yet in the mode, just select all the objects and enter; if you're already in it, pull others in by Ctrl-LMB on their dot in the Outliner (removing objects works the same way). A few notes: the Properties Editor only ever shows the active object's details (shape keys, UV maps, …), not those of every selection; selecting any element of an object makes it active; and there are limits on what you can edit — you can't, for example, build an edge that joins vertices from two different objects.

[Related references](INDEX.md).
