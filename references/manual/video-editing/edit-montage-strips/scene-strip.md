# Scene Strip

## Scene Strip

### Scene Strip

Scene strips allow you to embed the render output from another scene into your edit. Rather than rendering to a file then importing it, you can reference the scene directly.

The strip duration matches the animation settings of the referenced scene.

Note

Scene strips cannot reference the Sequencer's own scene; a different scene is required.

### Adding Scene Strips

Scenes are added via Add ‣ Scene ‣ "Scene Name". Scene assets from the current project or an Asset Library also appear in Add ‣ Scene. Scene assets assigned to a Catalog show that hierarchy as submenus. When adding a scene asset as a strip, it is always duplicated.

New scenes are created directly through Add ‣ Scene ‣ Empty Scene.

Options

Start Frame
The frame where the scene strip begins playback.

Channel
The row location for the strip.

Replace Selection
Swap the current active strip with the new scene strip.

When creating a new scene, these options are available:

Type
Scene creation approach.

New:
Generates a new strip with a fresh, empty scene using default parameters.

Copy Settings:
Generates a new strip with an empty scene and transfers settings from the current scene.

Linked Copy:
Generates a strip and links in the current scene's collections (shallow copy).

Full Copy:
Generates a strip and duplicates the entire scene.

### Options

Scene
Data-block picker for selecting or generating the scene to render from.

Input
Source specification for the scene strip.

Camera:
Renders using the scene's 3D camera.

Sequencer:
Uses the scene's Sequencer timeline, enabling a scene to incorporate another scene's edit (similar to Meta Strips but with multi-instance support).

Camera
Override the default scene camera with any other object. Helps switch perspectives within the same scene setup.

Show

Annotations
Shows Annotations in non-render display modes (Solid, Wireframe).

Transparent
Generates transparency in the background, useful for overlay effects like exporting Grease Pencil compositions.

### Sound

Strip Volume
Controls the loudness of audio from the scene.

### Limitations

Scene strips do not produce individual Render Passes; only the Combined pass is output.

[Related references](INDEX.md).
