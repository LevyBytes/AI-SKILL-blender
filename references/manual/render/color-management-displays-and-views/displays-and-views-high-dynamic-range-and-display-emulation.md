# Displays and Views: High Dynamic Range, Display Emulation

### High Dynamic Range 

To view high dynamic range (HDR) colors, choose the "Rec.2100 PQ" or "Rec.21000 HLG" display.

Under standard dynamic range (SDR), views drag bright colors way down to keep them in range.
HDR frees you to push beyond and show the scene more faithfully. Even HDR panels have a ceiling, so there are separate views for 500, 1000, 2000 and 4000 nits, each aimed at a different peak luminance.

In Blender, HDR content scales up and down with display brightness. Catching the whole range often means dimming the display to open headroom over SDR white.

Requirements:

- A HDR capable monitor.

- macOS: Any Apple Silicon device.

- Linux: Use Wayland, and set the Vulkan backend in the Blender system preferences.

- Windows: Enable "Use HDR" in the Windows display settings, and set the Vulkan backend in the Blender system
preferences.

### Display Emulation 

Automatic :

Shows images the way most other apps do, for previewing material headed to export. Blender works hard to emulate your chosen display on the actual device.

Off :

Sends the image straight out of OpenColorIO. Usually that misses, but it serves when you know your system and physical display already match the chosen display.

Emulation is not supported with older OpenColorIO configurations.

[Related references](INDEX.md).
