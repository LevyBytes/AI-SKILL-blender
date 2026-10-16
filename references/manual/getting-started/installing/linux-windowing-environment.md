# Linux Windowing Environment

## Linux Windowing Environment

### Linux Windowing Environment

On Linux, official Blender releases support both X11 and Wayland.

If Wayland is detected it's preferred; otherwise X11 is used.

Hint

The active Windowing Environment shows under Topbar ‣ Blender ‣ About Blender .

### X11

Historically the most widely used windowing environment on Linux and Unix systems.

There's no near-term plan to deprecate or drop X11 support.

### Wayland

Wayland support is a newer addition, so some configurations may be untested. Please file a bug if you hit trouble.

Blender has been tested against Gnome-Shell (mutter), KDE (plasma) & SWAY (wlroots) based compositors.

### Requirements

Gnome-Shell
Under Gnome-Shell the libdecor library is required. It's packaged on most Linux distributions.

If libdecor isn't found, Blender falls back to X11.

### Troubleshooting

Verbose Wayland output helps pin down problems. Start Blender from the command line with extra arguments:

Blender's Wayland Logging

```console
blender --log "ghost.wl.*" --log-level 2
```

Wayland Built-In Logging

```console
WAYLAND_DEBUG=1 blender
```

Disable Wayland (forcing X11)

```console
WAYLAND_DISPLAY="" blender
```

Disable libdecor (forcing borderless windows under Gnome-Shell)
Remove libdecor , then start Blender with an empty X11 display variable.

```console
DISPLAY="" blender
```

### Environment Variables

`XCURSOR_THEME`
The cursor theme to use (must name a locally installed cursor).

`XCURSOR_SIZE`
The cursor size; defaults to 28, and you may want it larger on Hi-DPI displays.

### Known Limitations

Gnome Shell's Fractional Scaling (before version 44)
Gnome-Shell older than 44 doesn't fully support fractional scaling.

Using fractional scaling on those older versions can cause glitches such as an undersized cursor.

NVIDIA GPU
NVIDIA drivers don't yet fully support what Wayland needs. Graphical glitches and flicker are common, and startup crashes happen at times. It isn't Blender-specific, so NVIDIA users may prefer X11 until driver support improves.

### Feature Comparison

| Feature | X11 | Wayland | Notes |
| --- | --- | --- | --- |
| Smooth Scroll | ✗ | ✓ | Smooth track-pad scrolling. |
| Multi-Touch Gestures | ✗ | ✓ | Track-pad and tablet support for pinch-zoom, pan, and orbit. |
| Reliable Cursor Warping | ✗ *1 | ✓ | Cursor warping, used e.g. while transforming and orbiting the viewport. |
| Window Positioning | ✓ | ✗ *2 | Needed to drag between windows and to restore window positions on file load. |

Features both systems share — Hi-DPI, 3D-mouse, tablet input, … etc. — are left off this list.

*1 On X11, rapid cursor motion can leave the window bounds while the cursor is grabbed (during a transform, say).

*2 Wayland won't let an app set its window position; that's a deliberate design choice and unlikely to change (see issues for position).

[Related references](INDEX.md).
