# Properties Editor

## Properties Editor

The Properties editor shows settings for the active scene, object, material, and other data types, giving access to a broad range of context-sensitive properties used across Blender.

Navigation Bar — properties are grouped into tabs shown as a vertical column of icons in the editor's Navigation Bar region. You can flip the Navigation Bar to the editor's left or right by RMB on the region and choosing Navigation Bar ‣ Flip to Left/Right, and hide it with RMB on the region then Navigation Bar ‣ Hide, or via the region toggle icon (see Changing the Size and Hiding Regions).
Active Tool and Workspace Settings — the first tab carries the active tool's settings (in the 3D Viewport) plus those of the current workspace.
Scene — tabs for the active scene: Render (EEVEE, Cycles, or Workbench settings), Output, View Layer, Scene, World.
Collection — settings for the active Collection.
Object — tabs for the active object, some shown only for certain types: Object, Modifiers (or Grease Pencil Modifiers), Effects, Particles, Physics, Object Constraints.
Object Data — the Object Data tab keeps its name but changes icon by object type. Geometry Objects: Mesh, Curve, Surface, Text, Metaball, Grease Pencil. Rigging and Deformation Objects: Armature, Bone, Bone Constraints, Lattice. Other Object Types: Empty, Speaker, Camera, Light, Light Probe.
Object Shading — tabs for an object's look, shown only when relevant: Material, Texture.
Strips — tabs for video-editing strips, shown only when relevant: Strip Modifiers, Strip Properties.
Visible Tabs — lets you hide specific tabs in the Properties editor, handy for tailoring it to a workflow: in the Video Editing workspace you might hide object and shading tabs to cut clutter, and in the Modeling workspace you might hide the strip tabs. Hidden tabs can be brought back anytime from this filter list.

Header:
Display Filter (Ctrl-F) — search for properties by name; matches stay visible while the rest gray out, and the editor highlights the first match and jumps to its tab automatically. Begin a search with Ctrl-F, and Alt-F clears it.
Data Context Path — shows the current data-block's name and icon (Object, Material, Scene, etc.) plus its place in the data hierarchy, e.g. Cube (Object) –> Mesh –> Material.
Toggle Pin ID — click the pin to lock the editor to the current data-block so it doesn't change with the selection; click again to unlock and return to context-based display.
Options — reached from the Options popover at the editor's top-right.
  Sync with Outliner — whether a click on an Outliner icon switches the active tab. Always (always heed the clicked Outliner icon), Never (ignore Outliner clicks), or Auto (heed it only when the Properties editor borders the Outliner).

[Related references](INDEX.md).
