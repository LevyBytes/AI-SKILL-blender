# Wave Modifier

## Wave Modifier

The Wave modifier adds a ripple-like motion to an object's geometry. It is available for meshes, lattices, curves, surfaces, and texts.

Options:
Motion: the wave deforms vertices/control points in the Z direction, starting from the given point and propagating along the object with circular wave fronts (when both X and Y are enabled) or rectilinear wave fronts (when only one axis is enabled), then parallel to the axis of whichever X or Y button is active.
Cyclic: repeat the waves cyclically rather than as a single pulse.
Along Normals - meshes only: displace the mesh along the surface normals instead of the object's Z axis.
X/Y/Z: restrict displacement along normals to the selected local axes.
Falloff: how fast the waves fade out as they travel away from the coordinates above (or those of the Start Position Object).
Height: the height or amplitude of the ripple.
Width: half the width between the tops of two subsequent ripples (when Cyclic is enabled); this indirectly affects amplitude, since if the pulses are too near each other the wave may not reach the zero Z position, so Blender lowers the whole wave to make the minimum zero, leaving the maximum lower than the expected amplitude (see Technical Details and Hints).
Narrowness — the actual width of each pulse: the higher the value, the narrower the pulse. The width of the area in which a single pulse is apparent is 4 / Narrowness — so if Narrowness is 1 the pulse is 4 units wide, and if Narrowness is 4 the pulse is 1 unit wide.
Vertex Group: the name of a vertex group used to control the modifier's influence; left empty, the modifier affects all vertices equally.
Invert: invert the influence of the selected vertex group, so the group now represents vertices that will not be deformed; the setting reverses the group's weight values.
Important: all the values above are in local object space, so they must be multiplied by the object's corresponding Scale values to get the real dimensions.

Start Position:
Object: use another object as the reference for the wave's starting position; you can then animate that object's position to change the wave's origin over time.
Start Position X/Y: coordinates of the center of the waves, in the object's local space.

Time: settings to control the animation.
Offset - time offset in frames: the frame at which the wave begins (if Speed is positive) or ends (if Speed is negative); use a negative frame number to prime and pre-start the waves.
Life: duration of the animation in frames; set to zero to loop the animation forever.
Damping: an additional number of frames over which the wave slowly damps from the Height value to zero after Life is reached; the damping affects all ripples and begins on the first frame after Life is over, with ripples disappearing over Damping frames.
Speed: the speed of the ripple, per frame.

Texture: finely control which vertices the wave affects, and to what extent, using a texture (see the common masking options for a complete reference).

Technical Details and Hints: to get a nice wave effect similar to sea waves and close to a sinusoidal wave, make the distance between following ripples and the ripple width equal — that is, set Narrowness equal to 2 / Width (e.g. for Width to be 1, set Narrow to 2).

[Related references](INDEX.md).
