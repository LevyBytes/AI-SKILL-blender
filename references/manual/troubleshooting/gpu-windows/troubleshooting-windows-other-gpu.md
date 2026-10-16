# Troubleshooting Windows -- Other GPU

## Troubleshooting Windows – Other GPU

### Troubleshooting Windows – Other GPU

OpenGL powers Blender's 3D Viewport and UI. Your graphics processor and drivers significantly influence Blender's stability and speed.

This section compiles troubleshooting options for visual artifacts, EEVEE and Cycles difficulties, and crashes caused by GPU problems.

### Drivers

Upgrading drivers regularly fixes many issues. Newer releases contain corrections that allow Blender to work reliably.

Windows GPU drivers come from the card manufacturer. Windows Update may install them automatically, or your computer manufacturer might provide versions.

### Laptops

Dual-GPU configurations are common in portable systems for efficiency. The first GPU resides on the processor (typically Intel or AMD) and uses less energy. The second is a standalone unit (AMD or NVIDIA) delivering faster performance at higher power cost.

For best Blender performance, the standalone GPU should be active. You can choose which GPU handles which application through your graphics driver or OS settings.

GPU-related crashes with the integrated version suggest trying the standalone; conversely, problems with the standalone might point toward using the integrated GPU.

### Common Problems

### Unsupported Graphics Driver Error

Your GPU and driver lack the required OpenGL 3.3 support that Blender needs.

Updating to the newest driver can boost OpenGL capability, but older cards may not support new Blender builds. In that case, Blender 2.79 or an earlier version is necessary. From version 2.8 forward (when EEVEE was introduced), older GPU support has decreased.

### Crash on Startup

Try launching Blender through a terminal window to view any debug output that appears during load.

Windows sometimes corrupts GPU drivers or replaces them incorrectly when updating the system. Removing all graphics drivers (there may be installations from Intel, AMD, and NVIDIA) and installing fresh copies from the vendor helps resolve this.

### Poor Performance

- Update graphics drivers (see above).

- On portable systems, make sure the standalone GPU is selected (see above).

- Lower quality via Preferences ‣ System ‣ Memory & Limits.

- Undo any settings changes you made in the graphics driver software.

### Render Errors

See EEVEE and Cycles documentation for details.

### Wrong Selection in 3D Viewport

See Invalid Selection, Disable Anti-Aliasing.

### Virtual Machines

VMs struggle when OpenGL drawing passes through the host system.

Set up PCI passthrough to fix this issue.

Some virtualization hosts require GPU paravirtualization support. Certain GPU vendors reserve this for high-end or professional cards.

### Information

To view your GPU and driver details, open Help ‣ Save System Info in Blender. Look at the OpenGL block for card name, maker, and driver version.

[Related references](INDEX.md).
