# Output: Rate, Audio, Tips

#### Rate 

Bitrate
Specifies average bit rate (quality) as the quantity of binary information per frame. Consult FFmpeg -b:v.

Minimum / Maximum
Video files can employ variable bit rate (VBR), distributing compressed data to allocate more to complex frames and less to simple ones. Configure this via Minimum and Maximum settings.

Buffer
The playback bitstream buffer capacity.

Mux Rate
Maximum transmission rate of the combined stream. Multiplexing merges separate video and audio tracks into one file, similar to packaging a video and MP3 into a container.

Mux Packet Size
Reduces muxer fragmentation or overhead based on input.

### Audio 

These controls govern audio export during rendering. For playback from Blender itself, refer to audio preferences in the Preferences menu.

Audio Codec
Codec selection for sound output. Consult video formats for all options.

Audio Channels
The quantity of audio output "locations" to encode.

Mono :

A single channel.

Stereo :

Two channels; usually left and right.

4 Channels :

Four output channels.

5.1 Surround :

Five channels with one LFE.

7.1 Surround :

Seven channels with one LFE.

Sample Rate
Audio frequency setting.

Bitrate
Control bit rate (quality) for each codec. Higher rates create larger files with inferior streaming but improved sound. Use powers of 2 for broad compatibility.

Volume
Output volume adjustment.

### Tips 

Tip

Video format selection depends on your intended use.

Direct video-format rendering is not advised initially. If issues occur during rendering, the file can become corrupted, necessitating a complete re-render. First produce a set of still images like the default PNG or high-fidelity OpenEXR (supporting HDR data), then combine them as an Image Strip in the Video Sequencer. This approach offers:

- Resumption from the interrupted frame if problems surface.

- Rapid codec testing in seconds versus minutes/hours, since encoding is quicker than 3D rendering.

- Full Video Sequencer capabilities, including compositing earlier renders, audio integration, and other clips.

Tip

Avoid post-processing lossy-compressed material as compression artifacts will be amplified. Employ lossy formats only for the final delivery stage.

[Related references](INDEX.md).
