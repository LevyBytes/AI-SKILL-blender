# Configuring Peripherals: Touchpad, NDOF (3D Mouse), Head-Mounted Displays (Virtual Reality), Supported Platforms, Getting Started, HTC Vive Cosmos, HTC Vive Focus 3, Monado

### Touchpad

Touchpad controls work on Windows, macOS, and Linux with Wayland. On a laptop without a mouse, you can emulate controls through multi-touch trackpad gestures, set in the Preferences.

| Gesture | Effect |
| --- | --- |
| Pan | Drag two fingers on the pad while holding Shift . |
| Zoom | Drag two fingers on the pad while holding Ctrl or OSKey . |
| Orbit | Drag two fingers on the pad. |
| Emulate right-click | Tap the pad with two fingers. |

### NDOF (3D Mouse)

3D mice, or NDOF devices, are hardware for navigating a Blender scene. Only 3Dconnexion units, such as the SpaceMouse™, are supported at present. They let you roam a scene and make Fly/Walk Navigation easier to steer. The NDOF device is set up in the Preferences, and those settings are also reachable straight from the viewport via the NDOFMenu button on the device.

See also

Input Preference covers configuring peripherals in more depth.

### Head-Mounted Displays (Virtual Reality)

HMDs drop the user into an interactive virtual environment. Worn on the head, they track head motion and project a seemingly all-around world onto small screens before the eyes. When it all works, the wearer feels genuinely inside that environment.

### Supported Platforms

Blender's virtual reality support is built on the cross-platform OpenXR standard. Being new, that standard still has limited support.

| Platform | Operating System | Notes |
| --- | --- | --- |
| HTC Vive Cosmos | Windows | Developer Preview |
| HTC Vive Focus 3 | Windows | Developer Preview |
| Monado | GNU/Linux | Not recommended for general use yet. |
| Meta (formerly Oculus) (Rift and Quest) | Windows | Requires Oculus v31 Software Update. Oculus Link required for Quest. |
| SteamVR | Windows, GNU/Linux | Requires SteamVR 1.16 or greater. |
| Varjo | Windows | – |
| Windows Mixed Reality | Windows | Requires Windows 10 May 2019 Update (1903). |

### Getting Started

The subsections below explain how to set up an HMD on each supported platform. Skip the setup and Blender will throw an error when you try to begin a virtual reality session.

#### HTC Vive Cosmos

Its dedicated platform is aimed at developers for now and may miss features other platforms have.

- Follow the steps on the
Vive Developer Forums.

- Turn on Blender's VR Scene Inspection add-on.

#### HTC Vive Focus 3

Its dedicated platform is likewise developer-focused for now and may lack some features.

- Follow the steps on the
Vive Developer Forums.

- Turn on Blender's VR Scene Inspection add-on.

#### Monado

Monado is a free, open-source XR platform for Linux. It isn't production-ready yet and should be used only for testing.

- Packages exist for these distributions:

- Ubuntu (Eoan, Focal)

- Debian (bullseye,
sid)

Elsewhere you'll have to build it from source — not advised if you have little experience compiling software. If you go ahead anyway, follow Monado's Getting Started Guides.

- Turn on Blender's VR Scene Inspection add-on.

[Related references](INDEX.md).
