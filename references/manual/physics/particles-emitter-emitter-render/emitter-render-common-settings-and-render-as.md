# Render: Common Settings, Render As, None, Halo, Path, Timing

## Render

### Render 

Reference

Panel :

Particle System ‣ Render

The Render Panel configures rendered particle appearance.

Note

Cycles exclusively facilitates Object and Collection render modes.

### Common Settings 

Scale

Scale Randomness

Material

Determines which material property governs particle shading.

Coordinates System

Designates an alternate object's coordinate framework for particle generation point calculation.

Show Emitter

When deactivated, the emitter stays out of rendered output. Enable Emitter to incorporate mesh rendering.

### Render As 

### None 

None designation prevents particle rendering. Useful when particles drive object duplication instead.

### Halo 

Halos display as glowing spots or light concentrations. They lack genuine light emission since they don't illuminate the surrounding scene like light objects. Halos remain visible but physically insubstantial.

### Path 

The Visualization panel for Path visualization. 

Path visualization requires Hair particle systems or Keyed particles.

B-Spline

Routes hair through B-spline curves. Appropriate for lower Render settings, trading control for smoother geometry.

Steps

Sets the path subdivision depth (value represents base 2 exponent). Adjust cautiously; Render doubling quadruples memory demand. Rendering velocity increases with reduced render values (sometimes dramatically). Practical minimums depend on hair waviness. Zero steps yield one subdivision, 1→2, 2→4, 3→8, 4→16, … 𝓃 → 2 𝓃.

### Timing 

Reference

Panel :

Particle System ‣ Render ‣ Timing

Type :

Hair

Absolute Path Time

Path timing uses absolute frame numbering.

End

Terminal moment for the practical path.

Random

Applies length randomization to paths.

[Related references](INDEX.md).
