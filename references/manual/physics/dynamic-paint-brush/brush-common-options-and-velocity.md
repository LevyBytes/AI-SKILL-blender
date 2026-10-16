# Brush: Common Options, Velocity

### Common Options

Paint Distance
Max distance to mesh surface for paint influence.

Project
Projects brush to canvas from a direction. "Direction-aligned" proximity.

The Project option limits brush canvas effect to normal direction. 

Falloff

Sharp :

Solid paint within distance.

Smooth :

Linear fade-out to maximum distance.

Color Ramp :

Custom falloff behavior.

### Velocity

Reference

Type :

Brush

Panel :

Physics ‣ Dynamic Paint ‣ Velocity

Velocity panel. 

Velocity-based brush options appear here.

A color ramp and settings sit above. The ramp represents velocity: left = zero, right = "Max velocity". Speed is units per frame.

Checkboxes set ramp influence.

Multiply Alpha
Uses ramp alpha per current velocity, multiplying brush alpha.

Replace Color
Substitutes brush color with Color Ramp values.

Multiply Depth
Multiplies "depth intersection" effect. Adjust displace and wave per speed.

Do Smudge
Smudging "smears" surface colors as the brush travels. Smudge Strength controls intensity.

Brush still paints normally. Erase can pair with smudge. Zero alpha gives pure smudging.

[Related references](INDEX.md).
