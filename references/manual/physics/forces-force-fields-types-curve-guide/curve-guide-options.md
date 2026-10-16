# Curve Guide: Options

## Curve Guide

### Curve Guide 

Reference

Panel :

Physics ‣ Force Fields

Type :

Curve Guide

The Curve Guide constrains particles to follow a trajectory defined by a Curve Object. Common applications include transporting a red blood cell along a vein or animating particle movement within a motor. Additionally, this guide can shape specific hair strand paths.

Note

Particle Edit Mode offers an alternative path definition approach.

Curves can animate like soft bodies or any standard method, allowing elaborate animations with minimal computational overhead. Such flexibility maintains fine control while keeping simulation time reasonable.

To orient particles along the curve direction, set their Orientation Axis to Velocity / Hair, enable Dynamic, and configure Angular Velocity Axis to Velocity in the particle system rotation settings. The Follow Path Constraint and curve's legacy Follow mode prove incompatible with this approach.

A Curve Guide affects all particles on the same layer irrespective of their distance to the curve. Stacking multiple guides combines their field effects additively (following classical physics principles). Adjust the Minimum Distance to cap their influence radius.

Particles follow a Curve Guide throughout their existence. Their traversal speed depends on lifetime duration and path length.

Note

The Curve Guide does not influence soft bodies.

### Options 

UI for a Curve Guide force field. 

Free

The fraction of particle lifetime spent outside the curve path.

Falloff Power

Regulates guide strength between Min Distance and Max Distance thresholds. A value of 1 produces linear degradation.

Additive

When used, particle speed evaluation incorporates falloff as well.

Weights

Leverage Curve weights to modulate particle influence progression along the path.

Clumping Amount

Particles converge at the curve end (1) or scatter apart (-1).

Shape

Governs convergence form. A value of +0.99 concentrates particles at the curve terminus. Zero gives linear distribution. A value of -0.99 gathers particles at the curve origin.

Min Distance

Specifies the distance within which the field maintains complete strength. Zero falloff negates this since the field works fully to Max Distance (or infinitely). Circles at curve endpoints indicate this radius in the 3D Viewport.

Max Distance

Sets the upper boundary for field reach, denoted by circles in the viewport.

[Related references](INDEX.md).
