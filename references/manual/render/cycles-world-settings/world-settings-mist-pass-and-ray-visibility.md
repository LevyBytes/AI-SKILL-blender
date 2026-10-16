# World Settings: Mist Pass, Ray Visibility, Tricks, Settings

## World Settings

### World Settings

### Mist Pass

Reference

Panel :

World ‣ Mist Pass

Note

Mist pass must activate in the View Layer Properties Editor tab before World tab settings appear.

Mist augments depth perception in renders. Blender creates a depth-mapped render layer (0.0–1.0) for compositor mist synthesis.

Start
Distance from camera where mist begins fading.

Depth
Start-relative mist fade span. Objects beyond Start + Depth disappear into mist.

Falloff
Mist intensity progression curve with distance.

Quadratic :

Light falloff calculation ( 1/{x^2} ), providing smooth 0.0 to 1.0 transition.

Linear :

Steeper start than quadratic ( 1/{x} ).

Inverse Quadratic :

Steepest start ( 1/{√x} ), approaches 1.0 faster.

Tip

Camera ‣ Viewport Display panel contains mist visualization activation.

Mist example
(blend-file).

### Ray Visibility

Reference

Panel :

World ‣ Ray Visibility

Like other objects, Ray Visibility manages which shaders perceive the backdrop.

### Tricks

Scenarios arise where different backgrounds suit direct versus indirect viewing. A Mix node solution: set Blend Factor to Is Camera Ray . First input becomes indirect color, second direct. Useful for high-res background images with low-res lighting.

Similarly, combining Is Camera and Is Glossy rays displays high-res images in reflections too.

Nodes for the trick above.

### Settings

Reference

Panel :

World ‣ Settings

[Related references](INDEX.md).
