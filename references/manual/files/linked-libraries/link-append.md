# Link & Append

## Link & Append

These functions let you reuse objects, materials, and other data-blocks from another blend-file, so you can build libraries of common content and share them across many referencing files. Tip: instead of the menu, you can also Link/Append a blend-file by dragging and dropping it into the Blender window. Note: data coming out of much newer blend-files can't be Linked or Appended.

Link — Reference: Editor: Topbar; Mode: All modes except Edit Mode; Menu: File ‣ Link…. Link makes a reference to data in a source file, so changes there show up in the current file the next time it's reloaded; in the File Browser, head to the external source blend-file and choose the data-blocks to reuse. Linked data-blocks carry a chain icon in the Outliner and are also listed in its Blender File Display Mode along with their source blend-file's path. Linked data-blocks start out non-editable — including a linked object's location/rotation/scale, locked to its transform in the source file — but there are ways around that:
- If you link a collection with Instance Collections on, or some object data with Instance Object Data on, the collection/object data is referenced through an object made inside the current blend-file, which you can transform. (That new object appears at the 3D Cursor.)
- You can also do some editing/animating on linked (normally locked) data-blocks via Library Overrides.
Warning: since it isn't editable, linked data can't be protected with the Fake User option; adding a custom property that points at an otherwise-unused linked data-block (a Text block, say) is a solid way to hold a reference to it through saves and reloads.
Options: these sit in the File Browser's right-hand panel.
Relative Path: references the external blend-file by a relative path rather than an absolute one.
Select: selects the newly added objects.
Active Collection: on, objects and collections go into the active view layer's active collection; off, they go into a new "Linked Data" collection in the active view layer.
Instance Collections: on, each linked collection is added to the scene as an instance collection (a single object standing in for the whole collection); add more with Add ‣ Collection Instance, or swap an instance for the collection's contents with Make Instances Real. Off, the collections are added as-is so you can see their contents in the Outliner and create Library Overrides.
Instance Object Data: on, an object is made for each directly linked object data; off, no object is made and the object data stays invisible in the scene until you make one yourself (by dragging the object data from the Outliner into the 3D Viewport, say).

Append - Reference: Editor: Topbar; Mode: All modes except Edit Mode; Menu: File ‣ Append…. Append copies data-blocks into your blend-file with no reference back to the originals, so you can edit your local copy freely while changes in the external source won't show up here. In the File Browser, open the source blend-file and tick the data-blocks you'd like to copy in. Note: appending data you already have linked adds the objects/collections to the scene but keeps them linked (and uneditable), so existing relationships with linked data stay intact.
Options: these sit in the File Browser's right-hand panel.
Select: selects the newly added objects.
Active Collection: on, objects and collections go into the active view layer's active collection; off, they go into a new "Appended Data" collection in the active view layer.
Instance Collections: on, each appended collection is added to the scene as an instance collection (a single object standing in for the whole collection); add more with Add ‣ Collection Instance, or swap an instance for the collection's contents with Make Instances Real. Off, the collections are added as-is so you can see their contents in the Outliner.
Instance Object Data: on, an object is made for each directly appended object data; off, no object is made and the object data stays invisible until you make one yourself (by dragging the object data from the Outliner into the 3D Viewport, say).
Fake User: marks the appended data-blocks as Protected.
Localize All: also copies all indirectly linked data rather than keeping the links.

Reload Library - Reference: Editor: Outliner; Menu: Context menu ‣ Reload. With the Outliner in Blender File Display Mode, right-click a linked blend-file and choose Reload to bring the current blend-file up to date with the newest version of the linked data-blocks at once, without reopening the file.

Relocate Library — Reference: Editor: Outliner; Menu: Context menu ‣ Relocate. With the Outliner in Blender File Display Mode, right-clicking a library (a linked blend-file) offers Relocate, which swaps it for a different file — handy either to fix a broken linked library (the file was moved or renamed) or to jump to a variant of the same data kept in another file.
Broken Libraries: if Blender can't find a library while loading a blend-file, it makes placeholder data-blocks in place of the missing linked ones, so references to the missing data aren't lost and relocating the missing library can restore the lost data automatically.

Relocate Linked ID — Reference: Editor: Outliner; Menu: Context menu ‣ ID Data ‣ Relocate. Right-clicking a linked ID offers Relocate in the ID Data sub-menu, which swaps a directly linked ID for another, from the same library or a different one — handy either to fix a broken linked data-block (the ID was renamed) or to jump to a variant of the same data.

Note: this only works on data-blocks that are directly linked and that nothing else linked depends on.

Make Local - Reference: Editor: 3D Viewport; Mode: Object Mode; Menu: Object ‣ Relations ‣ Make Local…. Also Reference: Editor: Outliner; Menu: Context menu ‣ ID Data ‣ Make Local. Turns the selected (or all) external objects into local copies in the current blend-file; links to the original library file are lost, but the data-blocks turn fully editable, just like ones created directly in the current file.
Options: the Outliner context-menu version has no options and touches only the selected data-blocks. The 3D Viewport version touches only the selected objects but can also make their dependencies local:
Type: whether to localize just the objects, or their data and materials too.

Known Limitations: for the most part linking works as you'd expect, but a few limits are worth knowing.
Circular Dependencies: dependencies shouldn't run both ways; trying to link or append data that links back to the current file will likely leave missing links.
Scene-Level Settings: scene-level settings like the Rigid Body World aren't copied when linking objects; instead, you can link the whole scene and use it as a Background Scene.
Compression & Memory Use: pointing at compressed blend-files can eat a lot of memory, since they have to load in full even when you only link/append a small part; once the data-blocks are loaded, though, memory use is the same.

[Related references](INDEX.md).
