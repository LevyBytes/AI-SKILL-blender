# Introduction: Falloff

### Falloff 

This section lets you configure the force field's spatial profile (when falloff Power exceeds 0).

Shape

Cone :

Falloff adopts a cone shape. Additional options mirror Tube configuration.

Sphere :

Falloff distributes uniformly in all directions like a sphere.

Tube :

Falloff creates a tube profile. Adjust Radial Power and configure Minimum and Maximum distance limits.

Z Direction

Dictates force effect along the Z axis.

+Z :

Force impacts exclusively the positive Z region.

-Z :

Force impacts exclusively the negative Z region.

Both Z :

Force influences both positive and negative Z regions.

Power

Governs how force magnitude decreases with distance. Where r represents the distance from the object origin, force diminishes with 1/( r - min + 1) power. A falloff of 2 yields 1/( r - min + 1) 2, resembling gravitational decay.

Min Distance

Establishes the distance threshold within which the field operates at complete strength. At zero falloff, this lacks effect because the field maintains full strength to Max Distance (or indefinitely). A supplementary circle marks this distance in the viewport.

Max Distance

Defines the upper bound for field influence radius, indicated by an additional circle surrounding the object.

[Related references](INDEX.md).
