# Fluid: Options, Fluid Properties, Advanced

## Fluid

### Fluid 

Reference

Panel :

Particle System ‣ Physics

Type :

Fluid

Fluid Physics settings. 

Fluid particles share similarities with Newtonian ones yet experience influence from internal mechanisms like pressure, surface interaction, internal friction, linking, and more. Applications range from viscous substances, gels, sandy materials, and misty smoke to countless additional scenarios.

Blender leverages SPH methodology for solving particle fluid mechanics. Smoothed-particle hydrodynamics represents a numerical approach for modeling fluid behavior. Applications span astrophysics, weapons science, volcanic processes, and hydrography. It embodies a coordinate-following, grid-independent Lagrangian formulation, with spatial fidelity tuneable through parameters including density.

### Options 

Fluid physics share configurations with Newtonian Physics. Comprehensive coverage appears on that documentation page.

### Fluid Properties 

Stiffness

The fluid's resistance to compression.

Viscosity

Viscous resistance to deformation. Lower settings model thicker liquids.

Buoyancy

Synthesized upward thrust resulting from density gradients, acting opposite gravity.

### Advanced 

Reference

Panel :

Particle System ‣ Physics ‣ Advanced

Repulsion Factor

Governs how vigorously fluid resists clumping (scaled as a stiffness multiple). Checkbox ties repulsion to stiffness value.

Stiff Viscosity

Introduces viscous opposition when fluid expands. Checkbox couples this to standard viscosity.

Interaction Radius

Sets the range of fluid force exchange. Checkbox couples this to 4 × particle size.

Rest Density

Establishes baseline fluid density. Checkbox couples this to standard density.

[Related references](INDEX.md).
