# Lighting

## Lighting

### Lighting

Workbench ignores scene lights, using settings from the Lighting panel instead.

Reference

Panel :

Properties ‣ Render ‣ Lighting

Flat :

Objects render in uniform color without highlights or shadows.

Studio :

A prepared studio lighting arrangement is applied, featuring a front-facing key light and a back-facing rim light. Click the sphere to select an alternative setup.

Studio lights can be customized in Preferences. By default they track the viewport camera, but this can be changed:

World Space Lighting
Fixes lights in place rather than following the viewport camera.

Rotation
The orientation of lights around the Z axis.

MatCap :

A Material Capture image is used, with texturing, lighting, and reflections prebaked. Objects are shaded by sampling colors from the image based on normal direction relative to the camera.

Click the sphere to choose a different MatCap, or use the double arrow button to flip it horizontally.

Custom MatCaps can be loaded in Preferences.

[Related references](INDEX.md).
