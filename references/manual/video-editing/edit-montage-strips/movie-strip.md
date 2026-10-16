# Movie Strip

## Movie Strip

### Movie Strip

To load a movie file (optionally containing sound) open the File Browser and pick a file, such as *.avi format videos.

Note

Media Files Can Be Large

A three-minute .mov file may reach 140MB. Loading it, even over network, requires time. Avoid assuming Blender has frozen if there's a delay.

Tip

Movie strips can show frame previews in the Sequencer through the Thumbnails overlay option.

### Add Movie Strip

Reference

Menu: Add ‣ Movie

Move Strips
Position the strip using the mouse immediately upon insertion. When enabled, Start Frame and Channel fields don't display.

Start Frame
Frame position for the left boundary of the strip.

Channel
Row assignment for the strip.

Relative Path
File location is stored relative to the blend document.

Replace Selection
Currently selected strips are replaced with the new strip.

Fit Method
Controls how media with mismatched aspect ratios fit into the render area.

Scale to Fit:
Adjusts the strip's Scale Transform for the content to fit the project area while maintaining proportions. Transparent bands may be added around the content edges.

Scale to Fill:
Alters the strip's Scale Transform to span the entire output while maintaining proportions. Parts of the original media may fall outside the visible area.

Stretch to Fill:
Resizes the strip to fill the full output without maintaining proportions. Distortion may occur.

Set View Transform
Chooses an appropriate View Transform based on the imported media's Color Space. Standard is typically correct; misalignment risks wrong colors or degraded rendering speed.

Adjust Playback Rate
Automatically scales playback velocity to match the original speed, accounting for scene frame rate differences.

Sound
Includes a Sound Strip containing the movie's audio track.

Set Scene Frame Rate
Updates the Scene Frame Rate to the frame rate stored in the video file.

### Example

Imported Movie strip with audio track underneath.

The strip itself shows its name, source file path, and duration.

[Related references](INDEX.md).
