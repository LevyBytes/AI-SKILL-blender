# Strip Properties: Time, Source, Options for Image Strips

### Time

Reference

Panel: Sidebar ‣ Strip ‣ Time

The Time panel adjusts source and timeline positioning.

Lock (padlock icon in panel header)
Prevents repositioning.

Show Retiming Keys
Toggle display and selection of Retiming Keys.

Channel
Alters the row number.

Start
Updates the strip's start frame; equivalent to selecting and moving it.

Duration
Changes the length in frames by adjusting the end position.

End
Displays the strip's conclusion time and frame.

Strip Offset Start/End
Positive values shift edges inward, starting later and stopping earlier than source bounds. Trim via the Offsets overlay to see the full source. Negative values shift outward, revealing the first or last frame extended as a freeze frame.

Hold Offset Start/End
Freezes frames at the start/end beyond simple trimming. You can combine Hold Offset and Strip Offset to hold a frame other than the first or last. For instance, setting Hold Offset Start to 10 and Strip Offset Start to -20 displays the 11th frame for 21 frames, then plays onward.

Current Frame
The playhead position within the strip, relative to its start.

### Source

Reference

Panel: Sidebar ‣ Strip ‣ Source

The Source panel displays and allows modification of the source file and its display handling.

Directory
The folder housing the source file.

Filename
The source file name. File names cap at 256 characters.

Color Space
Color space classification of the source media. Available spaces depend on the active OCIO profile. Default options are documented in Default OpenColorIO Configuration.

Alpha Mode
For sources with transparency, choose between Straight Alpha and Premultiplied Alpha.

Stream Index (Movie Strip)
Which video stream to play from when multiple exist.

Deinterlace
Removes interlacing from analog video.

Source Information
Displays media attributes.

Resolution
Output dimensions of the active strip.

FPS (Movie Strip)
Frame rate stored in the video file. Mismatch with scene Frame Rate may cause playback speed issues unless adjusted.

### Options for Image Strips

Directory
Folder holding the source file(s).

Filename
Source file identifier. For sequences, varies per frame.

Change Data/Files
Opens a File Browser to select new images, equivalent to Strip ‣ Inputs ‣ Change Paths/Files.

[Related references](INDEX.md).
