# System

## System

The System section lets you set graphics-card options, memory limits, and sound settings. Options your hardware doesn't support are either hidden or corrected at startup.

Cycles Render Devices — changes the Computing Device the Cycles render engine uses; Cycles can render on the CPU or certain GPUs (see GPU Rendering).
None — when set to None, or when None is the only choice, the CPU is Cycles' computing device.
CUDA — a compatible NVIDIA CUDA device becomes available for rendering with Cycles.
OptiX — a compatible NVIDIA OptiX device becomes available for rendering with Cycles.
HIP — a compatible AMD HIP device becomes available for rendering with Cycles.
oneAPI — a compatible Intel oneAPI device becomes available for rendering with Cycles.
Metal — a compatible Apple Metal device becomes available for rendering with Cycles.
Distribute Memory Across Devices — spreads resources over several GPUs instead of duplicating data, freeing room for larger scenes; it's available only when the GPUs are linked by a high-bandwidth protocol, currently just NVLink on NVIDIA GPUs.
Embree on GPU — turns on hardware ray tracing on Intel GPUs for better overall performance; supported only with oneAPI render devices.
HIP RT — speeds rendering by enabling AMD hardware ray tracing on RDNA2 and newer; available only with a HIP render device.
MetalRT — using MetalRT for ray tracing saves memory on curve-heavy scenes and can run faster in specific cases. Off (disabled, using the BVH2 layout for intersection queries), On (MetalRT for intersection queries), or Auto (pick the fastest intersection method automatically).

Display Graphics — settings governing how Blender draws its UI and other display graphics, which can affect performance and compatibility.
Backend — the graphics API used to draw the interface and render display content; changing it needs a Blender restart. OpenGL (the traditional backend, broadly compatible) or Vulkan (potentially faster with better support for modern GPU features, though compatibility varies by system and drivers).
Device (Vulkan) — which GPU handles display drawing, useful on multi-GPU systems (integrated + discrete) where you want a specific GPU for UI rendering; changing it needs a restart. Auto picks the most suitable GPU from your configuration and driver support.

Operating System Settings — set the in-use installation as your default Blender (MS-Windows & Linux only). On Linux, if Blender came from a package manager like Snap, file association is the package manager's job.
Register — makes the in-use Blender installation the default for generating thumbnails and opening blend-files.
Unregister — removes the file association and thumbnailer.
For All Users — registers Blender for everyone, which needs escalated privileges.
Linux Registration — setup files live under /usr/local for all users, otherwise ~/.local: a desktop file and icon make the app available in launchers, a file association for *.blend is set up, and the thumbnailer is installed so blend-file thumbnails appear in file managers (For All Users only).

Network:
Allow Online Access — lets Blender reach the internet; add-ons that respect this setting only go online when it's enabled, though Blender can't stop third-party add-ons from breaking the rule.
Time Out — how long (in seconds) online operations may wait before timing out; zero uses the system default.
Connection Limit — the most simultaneous connections an online operation may open; zero means no limit.

Memory & Limits:
Undo Steps — how many Undo steps are available.
Undo Memory Limit — the maximum memory use in Mb (0 is unlimited).
Global Undo — lets Blender record actions taken outside Edit Mode, such as duplicating objects, changing panel settings, or switching modes. Warning: switching it off saves memory but stops the Adjust Last Operation panel from working and, in some cases, prevents changing tool options, so it's best left on for normal use. See also Undo and Redo.
Console Scroll-back Lines — how many console-window lines are buffered in memory, handy for debugging and command-line rendering.
Texture Time Out — seconds since a GL texture was last accessed before it's freed; 0 keeps textures allocated.
Garbage Collection Rate — seconds between runs of the GL texture garbage collector.
VBO Time Out — seconds since a GL vertex buffer object (VBO) was last accessed before it's freed (0 keeps VBOs allocated).
Garbage Collection Rate — seconds between runs of the GL vertex-buffer-object garbage collector.
Shader Compilation Method — how GPU shaders compile in parallel. Not available on macOS, requires the OpenGL backend, and a change needs a Blender restart. Thread (several threads in one process compile shaders at once — more memory-efficient but possibly slower on some systems) or Subprocess:

(continued) several separate subprocesses compile shaders in parallel — potentially faster, especially with high core counts, but using far more RAM.
Threads / Subprocesses — how many shader-compilation threads or subprocesses to use, capped by the system's logical CPU cores; raising it can cut compile time at the cost of more memory, and 0 lets Blender choose a sensible number from your configuration. Not available on macOS, requires the OpenGL backend, and a change needs a restart.

Video Sequencer:
Memory Cache Limit — the upper limit (in megabytes) of the Video Sequencer and Movie Clip Editor memory cache; high values are recommended for best Clip editor and Sequencer performance.
Proxy Setup — when and how Proxies are made. Automatic (build proxies for added movie and image strips at every preview size) or Manual (set up proxies by hand). See also Sequencer Cache Properties.

Sound — this panel holds the sound settings for live playback within Blender and is available only with a device other than None; for export-sound settings see the Encoding Panel and Audio Panel.
Audio Device — the audio engine that processes and outputs audio.
  None — no playback support (audio strips still load and render normally).
  CoreAudio — macOS's native audio API, the default and preferred choice there.
  PulseAudio — the most common sound server on modern Linux, the preferred Linux choice when available.
  WASAPI — Windows's native audio API since Windows Vista, the default and preferred Windows choice.
  Jack — a high-quality professional engine needing a properly configured server running, with accurate sync to other professional audio apps via Jack.
  OpenAL — available on every platform as a fallback when the native engines fail; 3D audio played back may sound different from when rendered.
  SDL — uses the Simple Direct Media Layer API from libsdl.org, available on all platforms; possibly lower quality, so use it only as a backup.
Channels — how many audio source "locations" to output. Mono (one channel), Stereo (two, typically left and right), 4 Channels (four), 5.1 Surround (five plus one LFE channel), or 7.1 Surround (seven plus one LFE channel).
Mixing Buffer — how many samples the audio mixing buffer uses; bigger buffers can add latency, but if you hear clicks or other glitches, try raising it.
Sample Rate — the audio sampling rate.
Sample Format — the audio sample format.

[Related references](INDEX.md).
