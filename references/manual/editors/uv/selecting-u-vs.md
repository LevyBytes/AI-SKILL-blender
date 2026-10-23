# Selecting UVs

## Selecting UVs

As in the 3D Viewport, the UV Editor offers selection-mode buttons in its header plus a Select menu.

Sync Selection — when on (the default), the UV Editor and 3D Viewport share one synchronized selection: selecting components (vertices, edges, faces) in either editor auto-selects the matching elements in the other. With it on, all faces stay visible in the UV Editor at all times, since UV visibility follows the 3D Viewport's mesh selection; selecting a vertex, edge, or face in the 3D Viewport selects its UV counterparts, but where one 3D vertex or edge maps to several UV vertices or edges (along a UV seam, say) you can't pick them individually — selecting one selects them all. With it off, only the UVs of the faces currently selected in the 3D Viewport appear, UV Editor selections are independent (so individual UV vertices and edges can be selected even when they share a mesh vertex or edge), and selecting in one editor no longer touches the other.
Note: currently only some 3D Viewport selection operations keep per-UV selection data — basic picking, box, circle, and lasso; others, such as Select Random or Select Similar, reset the stored UV selection so all UVs tied to the selected mesh elements get selected. More operators may follow.
Hint: internally, UV selection data is kept per face corner and built on demand to avoid overhead; Python scripts that change mesh selections can call the API functions to sync or clear the UV selection state as needed.

Selection Mode: Vertex (1, select vertices), Edge (2, select edges), Face (3, select faces). With Sync Selection on, hold Shift while clicking a mode to turn several on at once. See also Mesh Selection.

UV Island Selection - Reference: Mode: Edit Mode; Menu: Header ‣ UV Island Selection; Shortcut: 4. Selects contiguous groups of faces connected in the UV map.

Sticky Selection Mode: options for auto-selecting extra UV vertices; available only in Face selection mode, or when Sync Selection is off.
Disabled: each UV vertex selects on its own.
Shared Location: auto-selects UV vertices that map to the same mesh vertex and share its UV coordinates; the default, it gives the illusion that several faces in a UV map share a vertex when really they have separate, overlapping ones.
Shared Vertex: auto-selects UV vertices that map to the same mesh vertex even at different UV coordinates; also how it behaves when Sync Selection is on.

Select Menu:
All (A): selects every UV element.
None (Alt-A): deselects every UV element.
Invert (Ctrl-I): flips the current selection.
Box Select (Alt-B): see Box Select.
Box Select Pinned (Ctrl-B): like Box Select but grabs only pinned UV vertices.
Circle Select: see Circle Select.
Lasso Select: see Lasso Select.
More/Less (Ctrl-NumpadPlus, Ctrl-NumpadMinus): grows/shrinks the selection to/from neighboring elements.

Select Similar - Reference: Mode: Edit Mode; Menu: Select ‣ Select Similar; Shortcut: Shift-G. Selects UV elements similar in some way to the active one; the Adjust Last Operation panel offers several options.
Type: the property to compare, with the choices depending on the Selection Mode:
  Vertex mode: Pinned (vertices with the same pinned state).
  Edge mode: Length (similar UV-map length), Length 3D (similar 3D-mesh length), Pinned (same pinned state).
  Face mode: Area (similar UV-map area), Area 3D (similar 3D-mesh area), Material (the same Material), Object (the same object — handy with several objects in Edit mode at once), Polygon Sides (a similar edge count), Winding (the same orientation, facing up or down in the UV map).
  Island mode: Area (similar UV-map area), Area 3D (similar 3D-mesh area), Amount of Faces in Island (a similar face count).
Compare - the comparison operator: Equal (values that match), Greater (values greater or equal), Less (values less or equal).
Threshold: the tolerance for values that are nearly but not quite the same; a higher threshold selects more elements.

Select Linked - Linked: Reference: Mode: Edit Mode; Menu: Select ‣ Select Linked ‣ Linked; Shortcut: Ctrl-L. Selects every UV element connected to the currently selected ones, expanding the selection across the whole connected UV island; connectivity goes by shared UV edges, not the underlying mesh topology. Handy for grabbing a whole island from a portion of it, as when adjusting layout, packing, or transforming an island. With Sync Selection on, linked selection rides the mesh's connectivity rather than the UV island's.
Shortest Path - Reference: Mode: Edit Mode; Menu: Select ‣ Select Linked ‣ Shortest Path; Shortcut: Ctrl-LMB. Selects every UV element along the shortest path between two elements: the two selected ones when run from the menu, or the active one and the clicked one when run via the shortcut.

Face Stepping: for vertices, lets the path cross faces along their diagonal rather than their edges; for edges, selects disconnected edges perpendicular to the path (an edge ring) rather than connected edges along it (an edge loop); for faces, lets the path pass through faces that share only a vertex rather than an edge.
Topology Distance: measures distance by counting edges rather than gauging their lengths.
Fill Region (Shift-Ctrl-LMB): selects every shortest path rather than just one.
The settings below select elements at regular intervals, making a "dashed line" instead of a continuous one.
Deselected: how many deselected elements sit in the repeating sequence.
Selected: how many selected elements sit in the repeating sequence.
Offset: how many elements to offset the sequence by.
See also Mesh edit Select Shortest Path.

Select Tile — Reference: Mode: Edit Mode; Menu: Select ‣ Select Tile. Selects the UV faces lying within a specific UV tile, mainly for UDIM workflows. The starting tile comes from the 2D Cursor's position, and every UV face whose coordinates fall inside it is selected. Useful with multi-tile UV layouts for quickly isolating and working on the UVs in one UDIM tile — for packing, transforming, or baking textures. To target a different tile, move the 2D Cursor there and run the operator again.

Select Pinned - Reference: Mode: Edit Mode; Menu: Select ‣ Select Pinned; Shortcut: Shift-P. Selects every pinned UV in the UV Editor. Pinned UVs are held fixed during unwrapping and certain transforms, staying put while other UVs move; this helps you quickly spot or tweak pinned regions, as when refining layouts or steering unwrap behavior.

Select Split — Reference: Mode: Edit Mode; Menu: Select ‣ Select Split; Shortcut: Y. "Detaches" the selected faces so you can move them elsewhere without disturbing their neighbors. Hint: unlike the mesh Split Selection, which truly disconnects faces, this is purely a selection operator — in UV space the faces were never joined to begin with; it only looked that way because Sticky Selection auto-selected neighboring faces' vertices, and Select Split deselects those again. As an alternative, set the Sticky Selection Mode to Disabled.

Select Overlap - Reference: Mode: Edit Mode; Menu: Select ‣ Select Overlap. Selects every UV face that overlaps another in the UV Editor. Overlapping UVs share, wholly or partly, the same texture space, which can cause rendering artifacts, texture bleeding, or wrong bakes, so this flags problem spots in a layout. It's commonly used when prepping UVs for texture baking, lightmaps, or game-engine export, where overlap is usually unwanted; once selected, overlapping faces can be moved, scaled, or repacked to fix it.

Select Edge Loop - Reference: Mode: Edit Mode; Shortcut: Alt-LMB, or Shift-Alt-LMB to extend the existing selection. Holding Alt while clicking an edge selects it and then runs the selection as far as it can in the two directions parallel to it; this works for edge loops that wrap a mesh and for partial loops too. Hold Shift as well to extend the current selection rather than replace it. See also Mesh edit Select Edge Loops.

Select Edge Ring - Reference: Mode: Edit Mode; Shortcut: Ctrl-Alt-LMB, or Shift-Ctrl-Alt-LMB to extend the existing selection. Holding Ctrl-Alt while clicking an edge selects it and then runs the selection as far as it can in the two directions perpendicular to it; this works for edge rings that wrap a mesh and even when no complete ring exists. Hold Shift as well to extend the current selection rather than replace it. See also Mesh edit Select Edge Rings.

[Related references](INDEX.md).
