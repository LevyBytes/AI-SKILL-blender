# Sound Strip

## Sound Strip

### Sound Strip

Beyond images and video, the Video Sequencer handles audio work. Load Waveform Audio format (WAV), MP3, and other sound files, or extract audio from movie files, then blend them using animation curves for volume management.

Example of sound editing.

### Working with Audio Tracks

A Sound strip operates like other strips in the Video Sequencer. Select and reposition it, adjust its starting offset by dragging the strip edges, and use K to divide it into segments. A practical use case is removing pauses or unwanted sounds.

Multiple Sound strips can overlap and mix during rendering. Assign each a name and volume via the sidebar. Overlapping strips automatically combine during output. For example, dialogue might sit on channel 5, background music on channel 6, and sound effects on channel 7.

See also

The Playback menu in the Timeline offers settings for audio playback behavior.

### Waveform

Audio waveform visibility depends on two factors:

Overlay
The Sequencer Overlay menu provides options to display all strip waveforms, none, or follow per-strip settings.

Strip
Each strip has a Display Waveform option, visible only when overlay is set to Use Strip Option.

Waveform clipping (amplitude above 100%) shows in red.

Further strip settings appear in the Sound Sidebar Panel.

### Animating Audio Track Properties

To animate Sound strips, press I over any property. Fading music in/out or adjusting levels are common use cases. Overlapping/crossed Sound strips combine together; lower channels don't suppress higher ones (unlike video/image strips), enabling Blender to function as an audio mixer. Layer tracks and animate curves to manage each sound level, creating an automated multi-channel mixer!

See also

Audio crossfading uses the Sound Crossfade effect.

### Output

Two rendering approaches are available. Encode audio into a video file, or render to a separate audio file. See documentation on audio format selection and rendering initiation.

### Add Sound Strip

Reference

Menu: Add ‣ Sound

Move Strips
Position using the mouse immediately after adding. When enabled, Start Frame and Channel don't display.

Start Frame
Timeline frame for the left edge.

Channel
Row assignment.

Relative Path
File location is stored relative to the blend document.

Replace Selection
Swap currently selected strips with the new sound strip.

Cache
Buffer the sound in RAM, activates Caching in Source properties.

Mono
Merge all channels into a single channel, activates Mono in Sound properties.

[Related references](INDEX.md).
