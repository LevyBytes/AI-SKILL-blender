# Viewport Display

### Viewport Display 

Reference

Panel :

Particle System ‣ Viewport Display

The Display Panel governs how particles render in the 3D Viewport. Viewport appearance does not necessarily dictate final rendering results.

Display As

None
Particles vanish from the 3D Viewport and do not render. The emitter object may still render.

Rendered
Particles appear as they will render.

Point
Particles appear as square dots. Scaling stays independent from camera distance.

Circle
Particles appear as view-facing circles. Scaling remains independent from camera proximity.

Cross
Particles appear as 6-point crosses oriented to particle rotation. Scaling remains independent from camera distance.

Axis
Particles display as 3-point axis markers. Reveals orientation and rotation information within the viewport. Increase Display Size for clear axis visualization.

Note

Point, Circle, Cross, and Axis modes lack specialized options but prove valuable when multiple particle systems operate simultaneously, particularly for Boids physics simulations where distinguishing particle system membership becomes important.

Color

The Color Menu specifies particle coloration by chosen properties.

None
Particles render in black.

Material
Particles take coloration from their assigned material.

Velocity
Particles color-code by speed. A blue-to-green-to-red gradient represents velocity; blue indicates slowest movement, red indicates velocities matching or exceeding Max. Increase Max for wider velocity range visualization.

Acceleration

Particles color according to acceleration magnitude.

Amount

Specifies the viewport particle display percentage (all particles still render).

Show Emitter

Toggles emitter object visibility in the viewport.

[Related references](INDEX.md).
