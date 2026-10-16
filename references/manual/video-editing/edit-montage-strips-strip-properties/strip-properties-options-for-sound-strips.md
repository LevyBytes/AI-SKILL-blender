# Strip Properties: Options for Sound Strips

### Options for Sound Strips

Sound
Data-block selector for picking a sound.

File Path
Location of the audio file.

Pack
Embed the sound into the blend document.

Caching
Audio is decoded and cached in RAM.

Source Information
Displays media attributes.

Sample Rate
Samples per second in the audio encoding.

Channels
Audio channel count.

Instead of adjusting these offsets in the Sidebar, you can also drag the strip's handles.
Hold Offset Start/End — trim frames off the start/end of the source material. At first glance this matches the Strip Offset properties, but you can in fact combine the two to hold (freeze) a frame other than the first or last: for example, with Hold Offset Start at 10 and Strip Offset Start at -20, the video first shows the source's 11th frame for 21 frames, then plays the remaining frames.
Current Frame — the Playhead's frame number relative to the start of the strip.

Source (Panel: Sidebar ‣ Strip ‣ Source): shows (and lets you change) the file the strip points to, as well as how that file is displayed.
Directory — the folder containing the strip's source file.
Filename — the name of the source file; note that file names are limited to 256 characters.
Color Space — the source file's color space; the available list depends on the active OCIO config, with the default supported color spaces described in detail under Default OpenColorIO Configuration.
Alpha Mode — if the source file has an Alpha (transparency) channel, choose between Straight Alpha and Premultiplied Alpha.
Stream Index (Movie Strip) — which video stream to use, in case there are multiple.
Deinterlace — apply deinterlacing to analog video.
Source Information — displays information about the strip's media.
Resolution — the resolution of the active strip's image output.
FPS (Movie Strip) — the frame rate encoded into the video file; if it doesn't match the scene's Frame Rate, the perceived speed of the media will be wrong unless the speed is changed to account for the difference.

Options for Image Strips:
Directory — the directory that contains the source file(s).
Filename — the name of the source file; for image sequences this differs for each frame.
Change Data/Files — opens a File Browser to select a new set of images (an alternative to editing the textboxes above); same as Strip ‣ Inputs ‣ Change Paths/Files.

Options for Sound Strips:
Sound — a data-block menu to select a sound.
File Path — the path to the file used by the selected sound data-block.
Pack — pack the sound into the blend-file.
Caching — the sound file is decoded and loaded into RAM.
Source Information — displays information about the strip's media.
Sample Rate — the number of samples per second the audio is encoded at.
Channels — the number of audio channels encoded into the audio stream.

[Related references](INDEX.md).
