# GPU Rendering: Metal – Apple (macOS), Limitations, Frequently Asked Questions, Why is Blender unresponsive during rendering?, Why does a scene that renders on the CPU not render on the GPU?, Can multiple GPUs be used for rendering?, Would multiple GPUs increase available memory?, What renders faster?, Error Messages, Error: Out of memory, The NVIDIA OpenGL driver lost connection with the display driver, Unsupported GNU version

### Metal – Apple (macOS) 

Metal drives GPU acceleration on Apple computers running Apple Silicon. The full feature set asks for macOS 13.0 or newer.

Apple Silicon picks up GPU accelerated ray-tracing and denoising.

### Limitations 

- No GPU backs Path Guiding.

- Among the backends only OptiX runs Open Shading Language, and the documentation notes some caveats there.

### Frequently Asked Questions 

### Why is Blender unresponsive during rendering? 

On older GPU generations a card can only render or paint the interface, not both, which is what can leave Blender frozen mid-render.
A heavy enough scene can stall Blender even on newer GPUs, where a flood of memory or pricey shaders is in play, though that worry is usually smaller.

The only full cure is one GPU dedicated to rendering and another to display.

### Why does a scene that renders on the CPU not render on the GPU? 

The reasons can be several, but the most common is the graphics card running short on memory.
As a rule a GPU is held to the memory aboard it
(see Would multiple GPUs increase available memory? for more information).
That is usually a far cry below the system memory the CPU reaches.
On CUDA, OptiX, HIP and Metal devices, Blender will reach for system memory on its own once GPU memory fills. That costs some performance but still tends to beat a CPU render.

### Can multiple GPUs be used for rendering? 

Yes. Head to Preferences ‣ System ‣ Compute Device Panel and set it up however you like.

### Would multiple GPUs increase available memory? 

As a rule no; a GPU reaches only the memory that belongs to it.

There is one exception: link NVIDIA GPUs over NVLink and they can pool memory, at a slight performance cost.
Switch this on through Distributed Memory Across Devices
in the preferences.

### What renders faster? 

It rides on the hardware at hand. Compute times also split between technologies according to the scene under test. For the freshest numbers on how various devices fare, browse the Blender Open Data resource.

### Error Messages 

When something goes wrong, be sure to fetch the official graphics drivers from the GPU maker's site, or via the package manager on Linux.
Drivers the computer maker bundles can run stale or come up short.

### Error: Out of memory 

Most often this signals that the GPU lacks the memory to hold the scene.

Note

Dropping texture resolution is one route to lighter memory use.
By way of example, 8k, 4k, 2k, and 1k image textures run 256MB, 64MB, 16MB and 4MB apiece.

### The NVIDIA OpenGL driver lost connection with the display driver 

When a single GPU serves both display and rendering, Windows puts a ceiling on how long that card may spend computing a render.
A heavy enough scene can let Cycles overrun the ceiling.
Trimming Tile Size in the Performance panel may take the edge off, though the real fix is separate cards for display and rendering.

Bumping the time-out up is the other route, though it does leave the interface draggier while a heavy scene renders.
Learn More Here.

### Unsupported GNU version 

On Linux this error can surface depending on the GCC version you run.
For the list of supported GCC versions, consult the NVIDIA CUDA Installation Guide for Linux. Two fixes are open to you:

Use an alternate compiler
Have an older GCC around that the installed CUDA toolkit version takes? Then swap it in for the default compiler.
You do that by setting the `CYCLES_CUDA_EXTRA_CFLAGS` environment variable as Blender launches.

Launch Blender from the command line as follows:

```text
`CYCLES_CUDA_EXTRA_CFLAGS`="-ccbin gcc-x.x" blender
```

[Related references](INDEX.md).
