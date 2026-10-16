# Introduction: Controls

### Controls

Reference

Menu :

Topbar ‣ Scene

The Scene data-block interface in the Topbar
allows scene selection and construction.

Scene data-block menu.

Scenes
A catalog of available scenes within the current blend-file.

Add

New
Generates a fresh scene with default settings.

Copy Settings
Generates a fresh scene inheriting output and planetary settings from the current scene.

Linked Copy
Generates a scene that references all information from the original.
The fresh scene incorporates pointers to matching collections, objects, and data-blocks as the original.
Adjustments in one automatically reflect in the other, as they reference matching resources.

Full Copy
Generates an autonomous scene with independent copies of all elements and their data.
This approach proves useful for differing approaches or alternate renditions that should remain independent.

Note

Add Scene options control which information gets replicated and which gets referenced.
Objects reference Object Data like meshes or lights, and scenes can reference or reproduce this linkage.

(Delete Scene)
Deletes the active scene data-block.
Note that Blender mandates a minimum of one scene in a document; deletion of the sole scene is impossible.

[Related references](INDEX.md).
