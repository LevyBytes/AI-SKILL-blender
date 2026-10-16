# Editing Outliner Data

## Editing Outliner Data

Context Menu — open it for a data-block with RMB on its icon or name; the options shown depend on the selected data-block type(s):
Copy/Paste — copies or pastes the selected data-blocks.
Delete (X, Delete) — wipes out every use of the selected data-blocks: objects leave all scenes, materials leave all meshes, and so on. Note: pressing these shortcuts over the 3D Viewport instead Unlinks the selected objects, removing them only from the current scene.
Delete Hierarchy — as above but also hits child collections/objects; run on a collection, child objects that also belong to another collection survive.
Select — adds the Outliner-selected items to the 3D Viewport selection, useful only when Sync Selection is off (with it on, the default, the Outliner selection syncs to the viewport automatically).
Select Hierarchy — adds the selected items' children to the Outliner selection; with Sync Selection on, also to the viewport selection.
Deselect — drops the Outliner-selected items from the 3D Viewport selection.
Unlink — removes the data-block's current use while keeping others: objects leave only the current scene, materials only the current mesh, and so on.

Collections — collections organize a scene's content and can hold objects as well as other collections.
New — creates a collection.
Duplicate Collections — makes a recursive copy of the collection, child collections, objects, and object data included.
Duplicate Linked — recursively copies the collection along with child collections and objects, but shares the object data.
Instance to Scene — creates a new collection instance.
Visibility — governs whether the collection appears in the 3D Viewport and in the final render.
  Isolate — shows the selected collection (plus its child and parent collections) and hides the rest.
  Show/Hide — flips the Hide in Viewports setting for the chosen collections.
  Show/Hide Inside — flips Hide in Viewports for the chosen collections and every child.
  Enable/Disable in Viewports — flips the Disable in Viewports setting for them.
  Enable/Disable in Renders — flips the Disable in Renders setting for them.
View Layer — governs the collection's interactions with the View Layer.
  Disable from View Layer — drops the collection from the active view layer; objects only in it won't render for that layer, handy for leaving out some object's influence on a particular view layer.
  Enable in View Layer — adds the collection to the active view layer so its objects render there.
  Set Holdout — turns on the Holdout property for the selected collections, so their objects cut a holdout/mask in the active view layer.
  Clear Holdout — turns that property off.
  Set Indirect Only (Cycles Only) — turns on Indirect Only for the selected collections, so their objects contribute to the image only indirectly, via shadows and reflections.
  Clear Indirect Only (Cycles Only) — turns that property off.
  Set Color Tag — applies or removes a color tag on the selected collection.

ID Data:
Unlink — removes the data-block's current use while keeping others (e.g. dropping a material from just the current mesh).
Make Local — converts an externally linked data-block into a local copy.
Make Single User — currently non-functional; use the Data-Block Menu's User Count button instead.
Delete — deletes the selected data-block.
Remap Users — points every use of the selected data-block at a different one — handy to swap one material for another everywhere, say.
Copy/Paste — copies or pastes selected data-blocks.
Add/Clear Fake User — adds or removes a fake user, which keeps unused data-blocks from being auto-deleted when you save and reload the blend-file.
Rename (F2) — renames the selected data-block.
Select Linked — selects the data-blocks that use the current one (e.g. every object using the selected material); see Select Linked.

Mark as Asset — see Creating an Asset.
Clear Asset — see Removing Assets.
Clear Asset (Set Fake User) — see Removing Assets.
Library Override — see Library Overrides.

View:
Show Active (Period) — centers the tree on the active item.
Expand/Collapse All (Shift-A) — expands or collapses every item in the tree.
Show Object Hierarchy (Home) — expands objects that have children and collapses those that don't.
Show/Hide One Level (NumpadPlus / NumpadMinus) — expands or collapses one level down/up the tree across all items.

[Related references](INDEX.md).
