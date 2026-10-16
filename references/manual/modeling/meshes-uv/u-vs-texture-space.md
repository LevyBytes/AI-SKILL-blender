# UVs & Texture Space

## UVs & Texture Space

UVs and Texture Space

UV Maps

Mode: All Modes
Panel: Properties ‣ Data ‣ UV Maps

For mesh objects, find UV maps in the Data tab of the Properties editor. After selecting a map, view and edit it in the UV editor.

One mesh can contain multiple UV maps (one per texture, for example), or a single UV map can serve multiple textures.

/ Active Render
Marks the UV map as the default for rendering. The Active Render UV map determines:

The UV Pass for compositing.

The Texture Coordinate Node for material shading.

The UV Map Node for material shading when no specific UV map is selected.

Add UV Map
Duplicates the selected UV map or creates a new one if the list is empty.

Remove UV Map
Removes the selected UV map.

Texture Space

Mode: All Modes
Panel: Properties ‣ Data ‣ Texture Space

This panel configures the object's Texture Space — a 3D box for generating texture coordinates without UV mapping. Visualize texture space via the Viewport Display panel option.

Texture Mesh (Mesh objects only)
Use another mesh for texture indices. Both objects' vertices must align precisely or UVs distort.

Auto Texture Space
Automatically calculates the texture space.

Location X, Y, Z; Size X, Y, Z
Manually define texture space relative to the object. You can also edit in the 3D Viewport (see Editing below).

Match Texture Space (Curve objects only)
Adjusts Location and Size to match the object's bounding box, disabling Auto Texture Space.

Editing Texture Space

Mode: Object Mode and Edit Mode
Menu: Object ‣ Transform ‣ Move/Scale Texture Space

Click a menu item, move the mouse to adjust texture space, and LMB to confirm. Use keyboard shortcuts to lock axes; see the status bar.

Accessing Texture Space

In material shader setup, use the Generated output of the Texture Coordinate Node to read the 3D coordinate within the object's texture space. Pass this to a texture node.

Texture spaces lack rotation support. Use a Mapping Node to manually rotate coordinates in the material shader instead.

[Related references](INDEX.md).
