# Light Objects: Common Settings, Renderer Settings, Point Light, Spot Light

## Light Objects

### Light Objects

Reference

Panel :

Properties ‣ Object Data
and Shader Editor ‣ Sidebar ‣ Options

### Common Settings

Type
Specifies the light category.

Temperature
Heat rating in Kelvin, for ordinary illumination hues.

Color
Tone tint of the released illumination.

Exposure
Scale the light strength by \\(2^{exposure}\\) .
This streamlines handling a broad variety of output ranges using a single variable.

Normalize
By default, complete light output stays constant as light shape and scale change.
Deactivating this option releases more illumination as the light gets bigger.

### Renderer Settings

- EEVEE specific settings

- Cycles specific settings

### Point Light

Point light.

A point light projects uniform luminescence outward in all directions.
It gets shown by a vacant, encircled mark.
Since the light originates from a point, the path of the light striking an item's surface
stems from the trajectory joining the light and the surface location.
It approximates the behavior of (for instance) a filament bulb.

Light intensity/energy weakens proportional to (along other influences)
spacing from the point light to the item. Stated differently,
distant matter gets shown darker.

Power
Output measure of the light. Larger quantities raise the light's brightness.
Sub-zero quantities are permitted, however should get avoided for authentic plus unbiased outcomes.

Radius
When beyond zero, the light emits from a round shell with the designated spacing.
Greater light range softens shadows plus specular effects, yet reduces perceptual brightness
because strength distributes across larger region.

Soft Falloff
Employ falloff to prevent harsh transitions where the light form meets additional things.

### Spot Light

A spot light sends a narrowing column of light from the point, aimed in one trajectory.

Power
Output measure of the light. Greater amounts boost the light's strength.
Negative quantities are permitted, however should get sidestepped for authentic plus unbiased outcomes.

Radius
When surpassing zero, the light emits from a round shell with the chosen spacing.
Greater light range generates gentler shadows plus specular effects.

Soft Falloff
Employ falloff to prevent harsh transitions where the light form meets additional items.

[Related references](INDEX.md).
