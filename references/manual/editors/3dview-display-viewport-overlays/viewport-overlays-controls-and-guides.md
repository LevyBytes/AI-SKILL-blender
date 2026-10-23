# Viewport Overlays: Reference - Mode: All Modes. Location: Header ‣ Overlays., Guides

## Viewport Overlays

Reference - Mode: All Modes. Location: Header ‣ Overlays.

The Show Overlays button switches every overlay in the viewport on or off at once. Bear in mind that a camera's outline and passepartout aren't counted among the Viewport overlays. The drop-down opens a popover of finer settings described below, and depending on the active interaction mode a second button may add still more, also covered here.

General: these options are always present regardless of mode, and some can be tuned in the Viewport Preferences.

Guides:
Grid: shows the grid in an orthographic side view.
Floor: shows the ground plane in perspective view.
Axes: shows the X, Y, and/or Z axis lines.
Scale: the spacing between lines of the grid/floor.
Subdivisions: how many subdivisions sit between grid lines.
Text Info: places assorted readouts in the viewport's upper-left corner:
  View Perspective: the name of the View Perspective, e.g. "Top Orthographic" or "User Perspective."
  Playback Frame Rate (FPS): the frames-per-second the animation is running at. By default Blender plays every frame, which can drop the FPS below the target (so playback runs slower than realtime); when that happens the FPS reads in red. Adjust this in the Playback popover of an editor's playback controls.
  Object Info: the current frame in parentheses, after which it names the active object, its data-block, and the Collection that holds it. Where relevant it also lists the selected Shape Key and, in angle brackets, any Marker on the current frame. If the object is keyframed on the current frame the Object Info shows in yellow.
  Grid Resolution: when the view is squared to a world axis (see Viewpoint), the Text Info additionally reports the smallest gap between two parallel grid lines.
Statistics: reports counts of objects and geometry, with the figures keyed to the current selection: selecting a mesh yields vertex, edge, and face counts, while selecting a light reports how many lights the scene holds.
  Objects: how many objects are selected versus the total.
  Geometry: scene data that varies by mode and object type, such as a count of vertices, faces, triangles, or bones.
3D Cursor: shows the 3D Cursor.
Annotations: shows annotations.
Camera Guides: shows the camera guides (Safe Areas and Composition Guides); available only in camera view.
Reference Spheres: shows two spheres, one glossy and one diffuse, that respond to lighting to aid look development; available only in Material Preview shading, with their size set in the Viewport Preferences.

Objects:
Extras: shows objects that carry no geometry (empties, cameras, lights). It also governs the display of the Rigid Body Collision Shape and the Object Texture Space.
Light Colors: tints a light object's outline with the color that light emits.
Relationship Lines: shows dashed lines marking parent or constraint relationships.
Outline Selected: draws an outline around selected objects.
Bones: shows Bones.
Motion Paths: shows the motion-path overlay.
Origin: shows the origins of the selected objects.
Origin (All): shows every object's origin.
Bone Wireframe Opacity: the top opacity for bones drawn in Wireframe shading (or in Solid shading with X-Ray on); useful for cutting clutter so you can focus on the mesh rather than the bones.

Geometry:
Wireframe: draws mesh edges, like Wireframe Shading but layered over the existing shading. The slider sets which edges appear: low values hide edges across near-flat surfaces, while 1 reveals them all.
Opacity: how opaque those edges are, from 0 (invisible) to 1 (fully solid).
Fade Inactive Geometry: in any mode but Object Mode, dims objects you aren't currently working on, with the slider setting how strongly.
Face Orientation: paints the back side of faces red. As a rule, a face showing red on a mesh's exterior is probably facing the wrong way and needs its normal flipped, which you can do with the Flip or Recalculate operators on meshes, or with Switch Direction on Surface objects.

Viewer Node:
Visualizes Attributes: shows attributes wired into the Viewer Node.
Viewer Node: draws, as a grayscale shade, whatever value the attribute feeding the Viewer Node carries.
Color Opacity: the opacity of the attribute currently being shown.
Attribute Text: prints attribute values as text in the viewport.

Motion Tracking: shows the motion-tracking overlay.
Camera Path: shows the reconstructed camera path.
Marker Names: shows the names of the reconstructed tracking markers.
Tracks: changes how the tracking markers are drawn (plain axes, arrows, and so on).
Size: changes the drawn size of the tracking markers.

Mesh Edit Mode Overlays: available while in Mesh Edit Mode:
Faces: highlights selected faces, in every selection mode.
Center: shows face center points in solid shading modes (they always appear in wireframe shading). Applies only in face-selection mode.
Creases: shows edges marked with a crease for the Subdivision Surface Modifier.
Sharp: shows sharp edges used by the Edge Split modifier.
Bevel: shows the weights created for the Bevel Modifier.
Seams: shows the UV-unwrapping seams.
Indices: shows the indices of selected vertices, edges, and faces.

Shading:
Retopology: handy when you've sculpted a mesh into the shape you want and need to rebuild it with cleaner topology. It makes the edited mesh see-through (so the sculpt shows beneath it) and can optionally draw it in front of nearby geometry (so you can see it over the sculpt).
Offset: how far to pull the edited mesh toward the camera; use it to display the mesh ahead of objects that would normally hide it.

Vertex Groups Weights: shows the active vertex group's weights, much as Weight Paint mode does.
Zero Weights: paints unreferenced and zero-weighted regions black, helping you spot spots where very low weight has been applied.
  None: vertices appear as normal.
  Active: vertices read black if they carry no weight in the active vertex group.
  All: vertices read black if they carry no weight in any vertex group.

Mesh Analysis: shows the Mesh Analysis overlay.

Measurement: shows numeric measures of the selected elements, with Units set in the Scene properties.
Edge Length: the length of selected edges.
Edge Angle: the angle a selected edge forms between two faces.
Face Area: the area of selected faces.
Face Angle: the angle at selected face corners.
Tip: geometry attached to the selection is shown during a transform, so you can drag a vertex and watch the connected edge lengths update, for instance.
Note: these readings honor the Transform Space set in the Sidebar; choose Global if you want the object's scale folded into the measurements.
See also the Measure tool, which gauges whatever distances and angles you single out.

Normals - three independent toggles: one for vertex normals, one for split normals (face normals drawn at each vertex), and one for plain face normals.
Size: how large the chosen normals are drawn.
Constant Screen Size Normals: keeps the normals a fixed size regardless of zoom.

Freestyle: these settings target the Freestyle Line Art renderer.
Edge Marks: shows Freestyle edge marks.
Face Marks: shows Freestyle face marks.

[Related references](INDEX.md).
