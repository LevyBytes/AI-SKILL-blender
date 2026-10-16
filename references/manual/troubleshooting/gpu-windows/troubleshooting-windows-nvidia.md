# Troubleshooting Windows -- NVIDIA

## Troubleshooting Windows – NVIDIA

### Troubleshooting Windows – NVIDIA

Blender relies on OpenGL to render the 3D Viewport and interface elements. The GPU and its drivers play a significant role in how Blender performs and behaves overall.

This section offers practical solutions for visual glitches, EEVEE and Cycles issues, and GPU-related crashes.

### Drivers

Keeping graphics drivers current frequently resolves performance and stability issues. Bug fixes in newer drivers enable Blender to function properly.

On Windows, GPU manufacturers provide drivers directly through NVIDIA. Windows Update may install graphics drivers automatically, or your system manufacturer may supply its own versions.

These bundled versions are not necessarily the latest releases and may have degradation. Always install official drivers from the manufacturer.

Download Latest NVIDIA Drivers

### Laptops

Many modern laptops include two graphics processors. One is integrated into the CPU (commonly Intel or AMD) with lower power consumption, and a dedicated GPU (AMD or NVIDIA) that delivers stronger performance but draws more power.

For optimal results with Blender, the dedicated GPU should handle rendering. Configure which GPU runs which program in your driver settings or the operating system.

If you experience glitches or crashes tied to the integrated GPU, switching to the dedicated option often resolves them. Similarly, if the dedicated GPU causes problems, the integrated option may be more stable.

### Common Problems

### Unsupported Graphics Driver Error

Your graphics card and drivers do not meet Blender's minimum OpenGL 3.3 requirement.

Installing the latest driver version can upgrade your OpenGL support, though some older hardware simply cannot run current Blender versions. Blender 2.79 or earlier may be your only option. From Blender 2.8 onward (with EEVEE added), compatibility with legacy graphics hardware has declined.

### Crash on Startup

Run Blender from a terminal to see if error output provides clues.

On Windows, GPU drivers sometimes become corrupted or are incorrectly replaced during Windows Update. In these situations, removing all graphics drivers (which may include multiple copies from Intel, AMD, and NVIDIA) and performing a fresh installation from the manufacturer's website often helps.

### Poor Performance

- Keep graphics drivers updated (see above).

- On laptops, verify you are using a dedicated GPU (see above).

- Lower quality settings via Preferences ‣ System ‣ Memory & Limits.

- Revert any modifications you made in graphics driver settings.

### Render Errors

Check EEVEE and Cycles documentation for specific guidance.

### Wrong Selection in 3D Viewport

See Invalid Selection, Disable Anti-Aliasing.

### Virtual Machines

Running Blender in a VM frequently encounters problems when OpenGL commands route through the host OS.

Use PCI passthrough to resolve this.

Some VM platforms need GPU paravirtualization enabled. Certain GPU makers limit this to higher-end cards or specific models.

### Information

Find your GPU and driver version in Help ‣ Save System Info within Blender. The OpenGL section displays your card model, vendor, and driver version.

[Related references](INDEX.md).
