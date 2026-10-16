# Brush Settings: Unified Settings, General

### Brush Settings

Each mode and brush has unique brush settings. But there is also a lot of overlap or similar settings. This page explains general and mode specific settings that are used across various brushes in more detail.

Changes to the settings of a brush asset are temporary and will be discarded when Blender is closed. To preserve settings, save them to the currently active brush asset using Save Changes to Asset , or create a new brush asset using Duplicate Asset , see Asset Operators. Loading a different file while Blender remains open does not discard the settings.

### Unified Settings

Some settings (e.g. size, strength, color), indicated with , allow for using a per-mode setting instead of the individual brush setting. These settings are shared across all brushes of a given mode (e.g. Sculpt Mode) but do not overwrite the individual brush value.

### General

Size
This option controls the size of the brush, measured in pixels. F allows you to change the brush size interactively by dragging the mouse from left to right and then LMB to accept. Meanwhile the texture of the brush will be visible inside the circle. You can also enter the size numerically with the number keys.

The size can be decreased/increased using [ and ] respectfully.

(Size Pressure)
Adjusts the size based on the stylus pressure when using a Graphics Tablet.

(Use Unified Size)
Use the same brush Size across all brushes.

/ (Expand/Collapse)
Show or hide the customizable pressure curve.

Custom Curve
By default this is a straight line with positive slope such that increased pressure results in a larger brush size.

For the curve controls see: Curve widget.

Size Unit Sculpt Mode
Controls how the brush Size is measured.

View :

The Size is measured based on how the cursor appears on the monitor i.e. "screen space".

Scene :

The Size is measured based on real world units. This means that the brush size stays consistent, independently from zooming in and out in the viewport. The unit type and scaling can be configured in the Scene Units.

Strength
For painting brushes the Strength defines the maximum effect of each brush stroke. For example, higher values cause a Paint brush to give each stroke a higher opacity. The opacity is never stronger than the set Strength , no matter how often the same surface is painted during the same stroke.

For sculpting brushes on the other hand the Strength relates to how strong each step of the stroke is, resulting in a slower/faster buildup towards the full brush effect during the stroke.

You can change the brush strength interactively by pressing Shift - F and then moving the brush and then LMB . You can also enter the strength numerically with the number keys.

(Strength Pressure)
Adjusts the strength based on the stylus pressure when using a Graphics Tablet.

(Use Unified Strength)
Use the same brush Strength across all brushes.

/ (Expand/Collapse)
Show or hide the customizable pressure curve.

Custom Curve
By default this is a straight line with positive slope such that increased pressure results in a stronger brush deformation.

For the curve controls see: Curve widget.

Blend
Set the way the color or value is applied over the targeted Color Attribute, Vertex Group or Image Texture. See Color Blend Modes.

- Add Alpha: makes the image more opaque where painted.

- Erase Alpha: makes the image transparent where painted, allowing background colors and lower-level textures to show through. As you "paint", the false checkerboard background will be revealed. Using a tablet pen's eraser end will toggle on this mode.

Tip

In order to see the effects of the Erase and Add Alpha mix modes in the Image Editor, the Display Channels must be set to Color & Alpha or Alpha . Transparent (no alpha) areas will then show a checkered background.

[Related references](INDEX.md).
