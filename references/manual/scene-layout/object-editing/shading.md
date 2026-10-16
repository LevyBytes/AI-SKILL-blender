# Shading

## Shading

### Shading 

### Shade Smooth 

Reference

Mode:
Object Mode

Menu:
Object ‣ Shade Smooth

Makes an object display with soft or jagged appearance.
This enforces the "smoothing" property on all faces in the mesh,
including during geometry addition or removal.

This function will also strip out any Smooth By Angle Modifiers.

The edge of the object still appears distinctly faceted despite smoothing.
Activating smoothing doesn't alter the mesh structure;
it changes normal computation across surfaces (normals blend together),
creating a smoother appearance.

To revert to faceted shading, use Shade Flat (normals become flat)
as shown in the first comparison below.

Keep Sharp Edges
Do not strip marked edges (which are unneeded for flat-shaded objects).
This toggle helps preserve data for future reversals.

### Shade Auto Smooth 

Reference

Mode:
Object Mode

Menu:
Object ‣ Shade Auto Smooth

Attaches a Smooth By Angle Modifier that automatically sets
edge sharpness according to the difference between adjacent face normals.
Note, the modifier is anchored to stay the last modifier.

Auto Smooth
When off, any Smooth By Angle Modifiers get removed.

Angle
Largest angle difference between adjacent face normals before they stop being treated as smooth.

### Shade Flat 

Reference

Mode:
Object Mode

Menu:
Object ‣ Shade Flat

Instructs the object to display and output all faces uniformly,
using each face's normal orientation.
This is often preferred for polygonal forms.

This function will also strip out any Smooth By Angle Modifiers.

Keep Sharp Edges
Do not strip marked edges (which are unneeded for flat-shaded objects).
This toggle helps preserve data for future reversals.

[Related references](INDEX.md).
