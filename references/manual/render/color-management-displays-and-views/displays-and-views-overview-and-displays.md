# Displays and Views: Overview, Displays, Wide Gamut

## Displays and Views

### Displays and Views 

### Overview 

To put an image on screen, you carry it from scene linear over into a display color space, a move that mixes technical and artistic calls.

Which display color space fits is the technical call, hinging on the target device and its reach. sRGB serves every computer monitor, while digital cinema, HD TVs, and wide-gamut or HDR machines may ask for other picks.

No display covers the full color spectrum or lights up without bound, so colors must be tucked inside the device gamut. For that, Blender lays out a choice of views, each landing on its own look.

The artistic side stretches further through color management options like exposure and white balance, plus color grading back in the compositor.
.

Conversion from linear to display device space. 

### Displays 

This is the color space of whichever display your images and video are aimed at.

Ordinary computer monitors take sRGB, and most images and video live there.
Even so, today's panels often reach a wider gamut and carry high dynamic range content.

Standard Dynamic Range (SDR)

sRGB :

Basic display supported everywhere.

Display P3 :

Wide gamut for Apple devices and other modern displays.

Rec.1886 :

Used by many older TVs.

Rec.2020 :

Even wider gamut than P3 supported by some displays.

High Dynamic Range (HDR)

Rec.2100 PQ :

For HDR displays with Rec.2020 wide gamut, up to 10000 nits.

Rec.2100 HLG :

For HDR TVs with Rec.2020 wide gamut, up to 1000 nits.

### Wide Gamut 

To view wide gamut colors, choose the "Display P3" or "Rec.2020" display.

Run it alongside an "ACEScg" or "Linear Rec.2020" working space for your materials, lights, rendering and compositing.

Requirements:

- A P3 or Rec.2020 capable monitor.

- macOS: Any Apple Silicon device.

- Linux: Use Wayland, and set the Vulkan backend in the Blender system preferences.

- Windows: Enable "Automatically manage color for apps" in the Windows display settings,
and set the Vulkan backend in the Blender system preferences.

[Related references](INDEX.md).
