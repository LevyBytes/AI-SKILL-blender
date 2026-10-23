# Interface

## Interface

Header - Display Mode: this dropdown sets what the Outliner shows.
Scenes: the view layers, collections, and objects across every scene.
View Layer: the collections and objects in the current scene's current view layer.
Video Sequencer: the images and videos used in the Video Sequencer.
Blender File: all data in the current blend-file; a shield icon on the right shows the user count, and clicking it adds or removes a fake user.
Data API: every data-block in the file plus any properties it has.
Library Overrides — the library overrides, split into two view modes: Properties (the data-blocks with overridden properties, listed by type and expandable to view and change them) and Hierarchies (the overridden data-blocks in a tree showing their hierarchy, including parents overridden implicitly — override a material, say, and the tree shows object > mesh > material — with a right-hand column of icons toggling each override's editability).
Unused Data: the data-blocks that are unused or have only a fake user; the shield icon on the right adds/removes a fake user. Unused data-blocks auto-delete on save and reload, or you can remove them now with Purge in the header.

Search: the textbox filters the tree by a typed substring; focus it with Ctrl-F or clear it with Alt-F.

Filter: the header's funnel icon gives finer control over what's shown, with some options unavailable depending on the Display Mode.
Restriction Toggles: sets which Restriction Toggles are visible.
Sort Alphabetically: sorts the entries alphabetically.
Sync Selection: whether to sync the Outliner selection to and from the 3D Viewport and Video Sequencer.
Show Mode Column: shows the column for toggling object interaction mode.
Search: Exact Match (show only items whose name fully matches, not merely contains, the search text) and Case Sensitive (weigh upper/lower case when comparing).
Filter:
  All View Layers: shows every view layer in the scene rather than just the active one; with the Objects filter off, this gives a compact overview of all collections against the view layers.
  Collections: shows the collections in the scene hierarchy; off, only the collections themselves hide while their objects stay visible.
  Objects: shows the objects in the scene hierarchy; off, you get a collections-only overview.
  Object State: lists objects by state or restriction, invertible with the Invert toggle: All (every object), Visible (only those visible in the 3D Viewport, accounting for both Hide in Viewports and Disable in Viewports), Selected (only the currently selected ones), Active (only the active object, usually the last selected), Selectable (only those that can be selected in the viewport).
  Object Contents: lists relevant materials, modifiers, mesh data, and so on as each object's children.
  Object Children: shows child objects as child nodes; off, they appear as siblings instead (the exception: a child in a different collection from its parent isn't shown under the parent's collection at all).
  Meshes/Lights/…: filters objects out by type.
  System Overrides: shows the data-block properties defined or controlled automatically (to point data-blocks at overridden data rather than the original, say); available only in the Library Overrides Display Mode.

Miscellaneous: some header options appear only when they fit the active Display Mode.
New Collection (View Layer): adds a new collection inside the selected one.
Filter by Type (Blender File, Unused Data) — restricts which data-block types the Outliner shows.
Keying Sets (Data API): adds/removes the selected property to/from the active Keying Set.
Drivers: adds/removes Drivers on the selected item.
Purge (Orphan Data) (Unused Data): opens a dialog to remove unused data-blocks from the current blend-file or any Linked Data (can't be undone).
  Local Data-Blocks: clears unused data-blocks out of the current blend-file.
  Linked Data-Blocks: clears unused data-blocks out of Linked Data.
  Recursive Delete: removes data-blocks used only by unused data-blocks, leaving no orphans behind.

Main Region - Object Interaction Mode: when a selected object sits in some interaction mode besides the default Object Mode, the Outliner draws an icon for it on the left. When the active object carries such an icon, a dot also appears next to objects of the same type; click a dot to switch to another object while staying in the mode, or Ctrl-LMB a dot (where Multi-Object Editing is supported) to add an object to the mode. Click the active object's mode icon to send it (and, under Multi-Object Editing, the others) back to Object Mode, or Ctrl-LMB the mode icon on a selected (but not active) object to return only that one to Object Mode.

Restriction Toggles: the Outliner's right side carries a row of toggle icons for every collection, object, bone, modifier, and constraint, used to make the item invisible, unselectable, and so on.

Note: only a few icons show by default; use the Filter pop-over to reveal more.
Shift-LMB an icon to toggle it for the item and all its children. Ctrl-LMB a collection's icon to enable it for that collection (and its parent/child collections) while disabling it for the rest; click again to re-enable the rest.

Exclude from View Layer (Collections): toggles whether the collection is part of the current View Layer; when excluded, its contents vanish from the 3D Viewport, the render, and the Outliner (see Include).
Disable Selection: controls whether you can select the object or collection in the 3D Viewport, handy for, say, reference images you only want to display and never select or move.
Hide in Viewports: toggles the object's or collection's visibility in the 3D Viewport alone, for the current view layer, leaving the render untouched. Instead of this icon you can press H with the pointer over the 3D Viewport to hide what's selected, or Alt-H to bring everything back. It applies only within the current blend-file: Link or Append it elsewhere and everything is visible there. Objects hidden this way stay in the view layer, so they're still evaluated and still affect playback performance.
  See also: collections can be hidden per 3D Viewport (see Local Collections in the Sidebar).
Disable in Viewports — toggles the object's or collection's visibility in the 3D Viewport alone, for all view layers, leaving the render untouched. It's separate from Hide in Viewports — an object needs both enabled to show — and suits "long-term invisibility," keeping an object hidden even after Alt-H. It carries over to other blend-files when linking or appending, and objects hidden this way drop out of the view layer, so they're no longer evaluated and don't affect playback performance.
Disable in Renders: toggles the object's or collection's visibility in the render alone, for all view layers, leaving the 3D Viewport untouched; typically used for helper objects that aid modeling and animation but don't belong in the final image.
Holdout (Collections): flips the collection's Holdout property on or off, which makes its objects punch a fully transparent hole into the view layer's render output.
Indirect Only (Collections, Cycles): toggles the collection's Indirect Only property, so its objects contribute to the image only indirectly, through shadows and reflections.

[Related references](INDEX.md).
