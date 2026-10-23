# Supported Video & Audio Formats

## Supported Video & Audio Formats

Blender uses FFmpeg for video encoding and decoding; these formats mostly serve to compress rendered image sequences into playable movies. A video file usually consists of: a container (wraps video, audio, and metadata into one file), a video codec (which compresses the video stream), and an audio codec (which compresses the audio stream, and is optional).

Supported Video Containers: the container holds the encoded streams but doesn't dictate how they're compressed.
MPEG-4: also the name of a codec family, but as a container it can hold video and audio encoded with various codecs, and it's widely supported across modern software and hardware. Extensions: .mp4, .mpg, .mpeg.
Matroska: a free, open-standard container that can hold multiple video, audio, subtitle, and metadata tracks in one file. Extension: .mkv.
WebM: a free, open-standard container aimed mainly at web streaming, supporting VP9 or AV1 video and Vorbis or Opus audio. Extension: .webm.
AVI: one of the earliest and most widely used container formats, derived from the Resource Interchange File Format (RIFF). Extension: .avi.
DV: a digital-video container used by many legacy camcorders; it enforces the DV video codec and stores audio uncompressed. Extension: .dv.
Flash: a container once used to deliver internet video through Adobe Flash Player; it enforces specific codecs. Extension: .flv.
MPEG-1: a container for lossy video and audio that locks in the MPEG-1 codec family. Extensions: .mpg, .mpeg.
MPEG-2: a container for DVD and broadcast video; it enforces MPEG-2 encoding for the video and its audio streams. Extensions: .dvd, .vob, .mpg, .mpeg.
Ogg: a free, open-standard container that can hold multiple video, audio, subtitle, or metadata streams. Extensions: .ogg, .ogv.
QuickTime: a multi-track container that shares many codecs with MP4; the two are largely interchangeable in some workflows, but MP4 has wider support. Extension: .mov.

Supported Video Codecs: codecs compress video and audio data to cut file size and keep playback smooth. Lossy codecs shrink files by discarding some data, trading image or audio quality for size; lossless codecs still compress but keep all the original data, giving larger files at full fidelity. Some codecs suit distribution and streaming (H.264, AV1), others editing and intermediate work (ProRes, DNxHD). Because codecs are needed to both encode and decode, they must be present on the machine making the file and the device playing it, and not every codec works in every container.
No Video: for audio-only encoding.
AV1: a free, open-standard lossy format meant as a successor to VP9; high compression efficiency with HDR output.
H.264 — a widely used lossy codec that balances size against quality well, common in streaming and general delivery.
H.265 / HEVC — a step up from H.264, with tighter compression, HDR output, and deeper color bit depths.
WEBM / VP9: an open, royalty-free lossy codec popular for internet streaming; handles alpha-channel transparency.
DNxHD: meant as an intermediate editing format; can run lossy or lossless.
DV: see Containers.
FFmpeg video codec #1: a lossless intra-frame codec; supports alpha-channel transparency.
Flash Video: see Containers.
HuffYUV: a lossless codec built to supplant uncompressed YCbCr capture formats.
MPEG-1: see Containers.
MPEG-2: see Containers.
MPEG-4(DivX): a lossy codec extending the MPEG standards with extra compression features.
ProRes: a high-quality, visually lossless codec common in professional post-production; offers a configurable Profile.
PNG: stores each frame as its own image in the stream; lossless, with alpha-channel transparency.
QuickTime Animation: a legacy lossless QuickTime codec with alpha-channel transparency.
Theora: a free, open-standard lossy codec built for the Ogg container.
Supported Features:
- AV1: Lossy; 8, 10, 12bit; Alpha ✗; HDR ✓
- H.264 — Lossy; 8, 10bit; Alpha ✗; HDR ✗
- H.265 / HEVC — Lossy; 8, 10, 12bit; Alpha ✗; HDR ✓
- WEBM / VP9: Lossy; 8bit; Alpha ✓; HDR ✗
- DNxHD: Lossy / Lossless; 8bit; Alpha ✗; HDR ✗
- DV: Lossy; 8bit; Alpha ✗; HDR ✗
- FFmpeg video codec #1: Lossless; 8, 10, 12, 16bit; Alpha ✓; HDR ✗
- Flash Video: Lossy; 8bit; Alpha ✗; HDR ✗
- HuffYUV: Lossless; 8bit; Alpha ✗; HDR ✗
- MPEG-1: Lossy; 8bit; Alpha ✗; HDR ✗
- MPEG-2: Lossy; 8bit; Alpha ✗; HDR ✗
- MPEG-4 (DivX): Lossy; 8bit; Alpha ✗; HDR ✗
- ProRes: Visually Lossless; 8, 10bit; Alpha ✗; HDR ✗
- PNG: Lossless; 8bit; Alpha ✓; HDR ✗
- QuickTime Animation: Lossless; 8bit; Alpha ✓; HDR ✗
- Theora: Lossy; 8bit; Alpha ✗; HDR ✗

FFmpeg Audio Codecs:
No Audio: for video-only encoding.
AAC: a standardized lossy codec that beats MP3's quality at comparable bit rates.
AC3: Dolby Digital audio compression.
FLAC: a free lossless codec that shrinks files while keeping full fidelity.
MP2: a lossy audio format.
MP3: a widely supported lossy audio format.
Opus: a modern lossy codec for speech and general audio, meant as a successor to Vorbis.
PCM: uncompressed digital audio.
Vorbis: a free, open-standard lossy codec comparable to AAC or MP3.

HDR Support: videos can be rendered in wide-gamut and HDR color spaces.

To export HDR video:
- Set Color Management Display to Rec.2100 PQ or HLG.
- Set Video Codec to H.265 / HEVC or AV1.
- Set Bit Depth to 10 or 12.
HDR videos are written with 100 nits diffuse white to match common video-player conventions. Compatibility varies by player and device; 10-bit PQ is generally the most compatible HDR setup.

Known Limitations — Video Output Size: some codecs cap output size — H.264, for instance, needs both width and height divisible by 2.

[Related references](INDEX.md).
