# Troubleshooting Linux -- Other GPU

## Troubleshooting Linux – Other GPU

### Troubleshooting Linux – Other GPU

Blender uses OpenGL for the 3D Viewport and interface. GPU and driver
significantly shape Blender function and speed.

Solutions for glitches, EEVEE/Cycles issues, and GPU crashes follow.

### Drivers

Latest GPU drivers often remedy issues. Updates patch problems improving Blender execution.

On Linux, packages supply GPU drivers from distributions. Installation usually happens via package/OS upgrades. Many distros provide several packages for multiple versions, letting you select.

### Laptops

Portable systems typically pack dual GPUs for efficiency. A slower built-in GPU in the processor (Intel/AMD,
lower power) coexists with speedier discrete GPU (AMD/NVIDIA, higher power).

Top performance comes from the discrete option for Blender. GPU preference per application is set via
driver or OS controls.

Discrete GPU glitches suggest trying built-in instead. Built-in problems suggest the opposite.

### Common Problems

### Unsupported Graphics Driver Error

Your GPU lacks minimum OpenGL 3.3 that Blender needs.

Latest driver version might raise OpenGL capacity; some hardware simply ages beyond modern Blender. Try Blender 2.79 previously. Post-2.8 Blender (introducing EEVEE) curtails older hardware backing.

### Crash on Startup

Try command-line launching to spot helpful debugging output.

Windows GPU drivers occasionally damage or get replaced by OS updates. Uninstall all (multiple vendors' sets exist) and reinstall clean from maker sources.

### Poor Performance

- Refresh GPU drivers (prior section).

- Laptops: confirm active dedicated GPU (earlier section).

- Dial down quality Preferences ‣ System ‣ Memory & Limits .

- Revert GPU setting changes if made.

### Render Errors

Consult EEVEE and Cycles material
individually.

### Wrong Selection in 3D Viewport

Reference Invalid Selection, Disable Anti-Aliasing.

### Virtual Machines

Inside VMs, OpenGL forwarding to hosts causes complications.

PCI passthrough setup solves this.

Certain hosts activate GPU sharing. Some makers limit to higher tiers.

### Information

View active GPU and driver via Help ‣ Save System Info in
Blender. OpenGL section reveals GPU, vendor, driver version.

[Related references](INDEX.md).
