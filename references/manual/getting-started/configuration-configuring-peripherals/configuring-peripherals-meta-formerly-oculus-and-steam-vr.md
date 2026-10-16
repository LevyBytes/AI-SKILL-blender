# Configuring Peripherals: Meta (formerly Oculus), SteamVR, Varjo, Windows Mixed Reality

#### Meta (formerly Oculus)

Meta (formerly Oculus) gained full OpenXR support with the Oculus v31 Software Update.

- Grab and install the Oculus Rift/Oculus Link software.

- Make Oculus the active OpenXR runtime from the General tab of the Oculus App Settings.

- Turn on Blender's VR Scene Inspection add-on.

Passthrough Support

Over OpenXR, passthrough is off by default in the Quest Link app and must be switched on in that app's settings to use it.

Passthrough render performance tracks the connection quality between headset and computer. For better results, wire the headset straight to the PC over USB, or at least put the computer on the local network via Ethernet.

#### SteamVR

SteamVR has had full OpenXR support since SteamVR 1.16.

- Make SteamVR the active OpenXR runtime from the Developer tab of the SteamVR Settings.

- Turn on Blender's VR Scene Inspection add-on.

Note

The SteamVR runtime also covers HTC Vive Cosmos, Oculus, and Windows Mixed Reality HMDs.

#### Varjo

Varjo ships full OpenXR support through its required Varjo Base software.

- Turn on Blender's VR Scene Inspection add-on.

#### Windows Mixed Reality

Windows Mixed Reality has full OpenXR support.
To see whether a PC can run it, Microsoft offers the
Windows Mixed Reality PC Check
application.

- Confirm the Windows 10 May 2019 Update (1903) is installed.

- If the system qualifies, the Mixed Reality Portal is probably already installed. It's also in the Microsoft Store.

- Open the Mixed Reality Portal. Click the ... menu button at the lower left. In the menu that opens, choose Set up OpenXR .

- Turn on Blender's VR Scene Inspection add-on.

Note

To move to Windows Mixed Reality from another OpenXR runtime (SteamVR, say), pull the OpenXR Developer Tools off the Microsoft Store, then make Windows Mixed Reality the active runtime.

[Related references](INDEX.md).
