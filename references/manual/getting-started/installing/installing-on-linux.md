# Installing on Linux

## Installing on Linux

### Installing on Linux

If you haven't already, check the Downloading Blender page for the minimum requirements and the available versions.

### Install from blender.org

Download the Linux build for your architecture and unpack it wherever you like (e.g. ~/software or /usr/local ).

Double-click the executable to launch Blender.

Installed this way, several Blender versions can coexist.

For convenience you might add a menu entry and set up blend-file associations for the file browser, both done by Registering Blender.

For a completely self-contained install — configuration and all — arrange a Portable Installation.

### Install from a Package Manager

Some Linux distributions carry a Blender package in their repositories.

Going through the distribution's own machinery keeps Blender consistent with the rest of the system and can add niceties from the package manager — package listing, update notices, automatic menu setup. Bear in mind, though, that the packaged version may lag the latest official release or drop some features. Some distributions, for licensing or other reasons, build Blender without Cycles GPU rendering support.

Where your distribution has a package, pick whichever is handiest. Otherwise the official binary is on blender.org.

### Install from Snap

Snap is a universal package manager meant to span many distributions. With snap already present, install Blender via:

```console
snap install blender --classic
```

One perk here: Blender updates install themselves. The Snap build also tends to be more consistent than the various per-distro packages.

### Running from the Terminal

See Launching from the terminal.

### Graphics System (X11 & Wayland)

Blender supports both X11 and Wayland. See Linux Windowing Environment for details.

### Avoiding Alt-Mouse Conflict

Some window managers use Alt - LMB and Alt - RMB by default to move and resize windows.

Blender needs those combos for several things, notably:

- Emulate 3 Button Mouse.

- Select Edge Loops.

- Changing several properties at once.

To free up the full feature set, point the window manager at the Meta key instead (also called Super or the Windows key):

Gnome
Run this on a command line (takes effect at next login):

```console
gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier ' '
```

KDE
Under System Settings ‣ Window Management ‣ Window Behavior ‣ Window Actions ,
switch the key from 'Alt' to 'Meta'.

### Updating on Linux

There are two ways to update Blender on Linux. This section covers the common ones.

### Updating from blender.org

When a new release lands, download it from the Blender website and install it via the steps in Install from blender.org.

### Updating with a Package Manager

Many Linux distributions package Blender for their package manager. Once installed, you update it just like any other application.

See also

The Splash-screen Defaults page, on importing settings from earlier Blender versions and other quick options.

### Known Limitations

### Archive Extraction

Unpacking Blender's archive with 7-zip isn't supported. Use TAR instead. See issue #104070 for more.

[Related references](INDEX.md).
