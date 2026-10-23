# Introduction

The UV Editor is for editing UV maps, which describe how a 2D image should wrap onto a 3D object.

Image textures are usually needed when the look you want is hard to get from procedural textures, or when the texture isn't uniform — a car, for instance, would have scratches only in a few sensible spots, not scattered randomly over its body. Blender offers several projections (Box, Sphere…) that auto-apply a 2D image to a 3D object, but those tend to suit only simple meshes; for trickier ones you build a UV map instead — a flat layout where each face of the 3D object is placed on the 2D image, marking which part of the image textures it, giving you full control of the mapping. The name "UV" points to the map's axes — U for horizontal, V for vertical — letters chosen so they don't clash with "X" and "Y", which name axes in 3D space.

UVs Explained — the clearest analogy is cutting up a cardboard box: snip along its edges with scissors and you can spread it flat on a table; looking down at it, U is the left-right direction and V the up-down. Next, lay the flattened box on a poster, cut the poster to its shape, glue the poster to the box, and reassemble — now you have a 3D box textured with a 2D image. A UV map, then, describes how the mesh's faces sit on the texture, and you have complete freedom in doing it: you could cut each face loose and position, rotate, scale, even skew it on the texture independently, and faces can overlap in the UV map to share the same patch of texture.
Example — in the image, a dome in 3D space is flattened to a disc in UV space, and each 3D face then gets the slice of the image it overlaps in the UV map. It also shows a common UV problem, distortion: although the checkered squares in the 2D texture are all one size, they come out different sizes on the 3D dome (smaller at the base than the top), because the UV-map faces have different relative sizes than in 3D space — a side effect of flattening. You'll usually want to minimize this by guiding and tweaking the flattening, with seams for example, though it can't always be wiped out entirely.

Interface — Header — the header holds several menus and options for working with UVs.
Sync Selection: keeps the selection in step across the UV Editor and the 3D Viewport (see Sync Selection).
Selection Mode: the UV element type to select (see Selection Mode).
Sticky Selection Mode: which other vertices to select automatically (see Sticky Selection Mode).
View: tools for how content is shown in the editor (see Navigating).
Select: tools for selecting UVs.
Image: tools for opening and manipulating images (see Editing Images).
UV: tools for Unwrapping Meshes and Editing UVs.
Pivot (Period): see Transform Pivot Point.
Snap (Shift-Tab): see Snapping.
Proportional Editing (O): see Proportional Editing.
Image: a data-block menu for choosing images; once one is loaded or created here, the Image panel appears in the Sidebar.
Image Pin: when on, the current image stays visible regardless of the object selection; this switching only happens while the 3D Viewport is in Edit Mode or Texture Paint Mode, and it's handy when an image serves as reference.
(Show Gizmo) — toggle all gizmos with the button or specific ones via the drop-down. Navigate — turns the pan/zoom gizmos for the 2D viewport on or off (see Navigation Gizmos).
Show Overlays: toggle all overlays with the button or specific ones via the drop-down (see UV Overlays).
Active UV Map Layer: choose which UV map to use.
Display Channels — choose which color channels appear. Color & Alpha (enables transparency with a checkerboard behind the image), Color (the colored image, no alpha), Alpha (the alpha channel in grayscale — white opaque, black transparent), Z-Buffer (depth from the camera between Clip Start and Clip End per the Camera settings), or Red, Green, Blue (one channel as grayscale).

[Related references](INDEX.md).
