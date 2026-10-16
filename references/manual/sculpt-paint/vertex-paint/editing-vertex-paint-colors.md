# Editing Vertex Paint Colors

### Editing Vertex Paint Colors

### Smooth Vertex Colors

Reference

Mode :

Vertex Paint Mode

Menu :

Paint ‣ Smooth Vertex Colors

Harmonizes colors throughout the vertex structure.

### Dirty Vertex Colors

Reference

Mode :

Vertex Paint Mode

Menu :

Paint ‣ Dirty Vertex Colors

Create a cavity-based dirt gradient map.

Blur Strength
Softening amount per pass.

Blur Iterations
Recurrence count for softening (higher = more blur).

Highlight Angle
Restricts angle for protruding geometry. Lower values sharpen distinctions but may cause clipping. 90 = flat, 180 = infinitely pointed.

Dirt Angle
Restricts angle for recessed geometry. Higher values sharpen distinctions but may cause clipping. 90 = flat, 0 = infinitely concave.

Dirt Only
Skips clean area computation when enabled.

Normalize
Optimizes contrast by automatically lessening Highlight Angle and raising Dirt Angle. Disabling maintains consistency across distinct meshes.

[Related references](INDEX.md).
