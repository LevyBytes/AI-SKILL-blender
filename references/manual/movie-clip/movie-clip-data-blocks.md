# Movie Clip Data-Blocks

## Movie Clip Data-Blocks

### Movie Clip Data-Blocks

The video files and image sequences you use for motion tracking, masking, and compositing are held in Movie Clip data-blocks.

Their main home is the Movie Clip Editor,
but nodes and other systems that accept video input can reference them too.

### Creating a Movie Clip

There are a few ways to make a Movie Clip:

- Open a video file or image sequence inside the Movie Clip Editor.

- Drop a clip into the Compositor with a
Movie Clip node.

- Reach for the data-block selector in any editor that accepts Movie Clip references.

Once a file loads, a Movie Clip data-block springs into being and is kept inside the current
Blend file.

### Properties

These are the main properties a Movie Clip data-block exposes:

File Path
Where the video file or image sequence lives on disk.

Start Frame
Which scene frame the clip's opening frame is pinned to.
That's how you line the footage up against the timeline.

Frame Offset
Slides the clip's own internal frame numbering while leaving its place
in the scene timeline alone. Useful for syncing footage that doesn't
begin at frame 1.

Color Space
States which color space the image file was stored under.
Blender uses that to convert the image correctly into its
internal linear color space, where all color math and rendering happen.

sRGB is the common storage choice for textures and finished renders,
whereas OpenEXR images are kept in a linear color space.
Certain images — normal, bump, or stencil maps, for instance — don't really hold "colors" at all,
so no color conversion should ever touch them.
Set the color space of those images to Non-Color .

Which color spaces show up in the list comes down to the active OCIO config.
For a detailed write-up of the ones supported by default, see
Default OpenColorIO Configuration.

### Usage

Where Movie Clips most often come into play:

- Motion Tracking to rebuild camera movement
or follow objects.

- Masking for rotoscoping and compositing.

- Input in the Compositor through Movie Clip nodes.

A single Blend file can hold several Movie Clip data-blocks,
so one project can draw on different footage sources.

### Data-Block Management

Being ordinary Blender data-blocks, Movie Clips can be handled from the
Outliner.

What they allow:

- Renaming.

- Fake User (keeps an unused clip from being cleaned out automatically).

- Unlinking from editors or nodes.

Note

Deleting a Movie Clip data-block from the Blend file leaves
the original media file on disk untouched.

[Related references](INDEX.md).
