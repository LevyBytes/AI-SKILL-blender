# 3D Viewport: Rendering, Depth Buffer Glitches, Objects Invisible in Camera View, Performance, Slow Rendering, Slow Selection, Viewport Playback Frame Rate Limited, Navigation, Lost in Space

## 3D Viewport

### 3D Viewport

### Rendering

### Depth Buffer Glitches

Setting broad clipping ranges shows near and far items but cuts depth precision, creating errors.

| Description | Description | Description |
| --- | --- | --- |
| Model with no clipping artifacts. | Model with clipping artifacts. | Mesh with artifacts in Edit Mode. |

Avoidance tactics:

- Increase near clipping for expansive scenes.

- Decrease far clipping when objects remain close.

Orthographic mode uses far Clip End alone; high values still risk errors. Universal across 3D apps.

### Objects Invisible in Camera View

Broad scenes may hide objects in Camera View. Low camera clipping could cause this. Cameras show only objects
inside clipping bounds.

### Performance

### Slow Rendering

Viewport sluggishness stems from multiple sources.

Old Hardware
Occasionally, your system—chiefly the GPU—struggles keeping pace with dense models.

Upgrade Graphics Driver
Updating drivers occasionally resolves sluggish selection.

### Slow Selection

OpenGL selection in Blender sometimes slows on certain GPU drivers.
Dense geometry intensifies problems.

Remedies:

GPU Depth Picking (Preferences)
Navigate Preferences ‣ Viewport ‣ Selection .

Off by default, disabling trades selection precision for speed.

Upgrade Graphics Driver
Newer drivers resolve performance in some scenarios. Modern versions suit 3D work.

Select Centers (Workaround)
Object Mode with Ctrl -held selecting targets centers. Helps on its own, avoiding OpenGL checks.

Change Display Mode (Workaround)
Wireframe mode accelerates object switching.

Note

These workarounds lack permanence, yet help if stuck with inadequate OpenGL hardware.

Ultimately, upgrade hardware if stuck.

### Viewport Playback Frame Rate Limited

Viewport playback capped near 60 FPS typically means VSync is on, found in GPU settings.
Disable for higher rates, though display limits may apply.

Varies per system and GPU.

### Navigation

### Lost in Space

Accidental scene navigation leaves you blank-screened. Two fixes:

- Click an object in the Outliner, then focus with
View ‣ Frame Selected or NumpadPeriod .

- Press Home to display all scene items.

[Related references](INDEX.md).
