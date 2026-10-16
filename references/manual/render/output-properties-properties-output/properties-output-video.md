# Output: Video

### Video 

Video Codec
Selects the compression and encoding approach. See video formats for all available options.

Note

Standards

Some video containers and codecs prove incompatible. If errors occur, verify container-codec compatibility. Additionally, certain codecs function only with specific frame dimensions. Default to standard sizes or investigate codec limitations.

Color Depth
The exponent (base-2) representing color count within each color channel. Higher bit depths enable richer color representation, lowering banding artifacts and improving fidelity. However, bit depth increases memory consumption exponentially.

Notably, not all formats support every color depth configuration.

8 :

Supports 256 levels per channel, totaling approximately 16.7 million colors (RGB). The standard for on-screen content and conventional video.

10 :

Supports 1,024 levels per channel, totaling over 1 billion colors (RGB). Available for H.264, H.265, and AV1 codecs.

12 :

Supports 4,096 levels per channel, totaling over 68 billion colors (RGB). Available for H.265 and AV1 codecs.

Profile ProRes
Defines encoded video quality, compression, and transmission rate.

ProRes 422 Proxy :

Minimal bitrate and quality. Useful for offline work where speed and storage are priorities.

ProRes 422 LT :

Lower bitrate than standard ProRes 422 with reasonable fidelity. Appropriate for editorial and preview stages.

ProRes 422 :

Equilibrium between image precision and file size. Recommended for standard workflows.

ProRes 422 HQ :

Superior quality and bitrate versus standard ProRes 422. Preferred for broadcast and premium post-production.

ProRes 4444 :

Retains complete RGB and alpha channel data. Designed for effects and visual effects work.

ProRes 4444 XQ :

Maximum ProRes fidelity. Maintains peak color detail and tonal range, ideal for color work and high-end visual effects.

Output Quality
These represent preset Rate choices.

CRF Custom Quality
Constant Rate Factor (CRF). Reducing CRF enhances video fidelity but enlarges output. Permitted ranges depend on the codec: 0-51 for AV1, H.264 and H.265/HEVC; 0-63 for WebP/VP9 and 1-31 for MPEG-4/DivX. Values outside the range are clipped to the nearest valid value. A CRF of 0 creates lossless encoding.

Encoding Speed
Choices balancing fast encoding (larger files) with heavy compression (smaller files).

Keyframe Interval
The count of pictures per Group of Pictures. Set to 0 for "intra_only" mode, which disables between-frame video coding. Larger intervals typically reduce file size but require more computing power for playback.

Max B-frames
Allows B-frame usage.

Interval
Maximum B-frames separating non-B-frames.

[Related references](INDEX.md).
