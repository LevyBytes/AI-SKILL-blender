# Fluid domain gas and fire settings

Reference - Panel: Physics ‣ Fluid ‣ Settings; Type: Domain.
The domain object contains the entire simulation: fluid can't leave it, instead colliding with the edge or disappearing depending on the domain's settings. Larger domains need higher resolutions and longer bake times, so make it just big enough to fit the simulation but no larger than necessary. To create one, add a cube and transform it (translation, rotation, and scaling all allowed) until it encloses the simulation area, then click Fluid in the Properties ‣ Physics tab and set the fluid Type to Domain.
Note: you can use other mesh-object shapes as domain objects, but the fluid simulator uses the shape's Bounding Box as the domain bounds, so the actual domain stays rectangular.

Domain Type: a fluid domain controls either liquid or gas flows: liquid domains consider all liquid flow objects intersecting the domain, while gas domains consider all intersecting Smoke, Fire, and Smoke & Fire flow objects; the domain type can't be changed dynamically.
Resolution Divisions — the domain is subdivided into many "cells" called Voxels that form the fluid's "pixels," and this sets the number of subdivisions; more subdivisions is one way to make higher-resolution fluids. Since resolution is defined in "subdivisions," larger domains need more divisions for an equivalent resolution — for example, a one-meter cube at 64 Resolution Divisions needs 128 to match a 2-meter cube — with the base division taken from the longest dimension of the object's bounding box. To help visualize the voxel size, the Resolution Divisions can be previewed with a small cube shown in the 3D Viewport.
Time Scale - controls the simulation speed: low values give a "slow motion" sim, while higher values advance it faster (good for generating fluids for still renders).
Adaptive Time Steps: let the solver automatically decide when to run multiple simulation steps per frame, taking into account the maximum and minimum number of time steps, the current Frame Rate, and the Time Scale.
CFL Number: the maximum velocity per grid cell, measured in grid cells per time step; fluid may move only up to this velocity in one step, and exceeding the threshold makes the solver subdivide the step. In general, a greater CFL (Courant–Friedrichs–Lewy) number minimizes the number of simulation steps and computation time but yields less physically accurate behavior for fast flows, while a smaller CFL number means more steps per frame and longer simulation times but more accurate behavior at high velocities (e.g. fast fluid flow colliding with an obstacle).
Note: when lowering the CFL number it's recommended to increase the maximum number of time steps; similarly, when increasing the CFL number, adjust the minimum.
Timesteps Maximum: the maximum number of time steps allowed per frame; the solver divides a step up to this many sub-steps if needed.
Timesteps Minimum: the minimum number of time steps allowed per frame; the solver always performs at least this many per frame.
Gravity: by default the fluid solver uses the global scene gravity; disabling that (in the scene settings) enables the fluid gravity options.
Empty Space (Gas Only): voxels with values under this count as empty space; more empty space optimizes rendering and, with OpenVDB caching, also reduces cache sizes.
Delete in Obstacle: remove any volume of fluid that intersects an obstacle inside the domain.

Border Collisions (Panel: Physics ‣ Fluid ‣ Settings ‣ Border Collisions; Type: Domain (Gas)) — control which sides of the domain let fluid "pass through" (making it disappear without influencing the rest of the simulation) and which sides deflect fluid.

Gas (Panel: Physics ‣ Fluid ‣ Gas; Type: Domain (Gas)):
Buoyancy Density: buoyant force based on gas density: values above 0 make the gas rise (lighter than ambient air), values below 0 make it sink (heavier than ambient air).
Buoyancy Heat: how much temperature affects the gas, depending on each flow object's Initial Temperature: above 0, gas rises when the flow object's Initial Temperature is positive and sinks when it's negative; below 0, the opposite (gas from a positive Initial Temperature sinks, gas from a negative one rises). Gas from multiple flow objects with different temperatures mixes and warms up or cools down until an equilibrium is reached.
Vorticity: the amount of turbulence in the gas: higher values make lots of small swirls, lower values make smoother shapes (e.g. a vorticity of 0.0 vs 0.2).
Dissolve: allow gas to dissipate over time.
- Time: the speed of gas dissipation in frames.
- Slow: dissolve gas in a logarithmic fashion — quickly at first, but lingering longer.

Fire (Type: Domain; Panel: Physics ‣ Fluid ‣ Gas ‣ Fire):
Reaction Speed - how fast fuel burns: larger values give smaller flames (fuel burns before going far), smaller values give larger flames (fuel flows farther before being fully consumed).

Flame Smoke

Specifies the quantity of extra smoke created to replicate burnt fuel in flames. The resulting smoke becomes most apparent when a "Fire + Smoke" Flow Object is employed.

Vorticity

Contributes vorticity to flames in addition to the domain's baseline vorticity.

Temperature Maximum

Sets the upper limit for flame temperature. Higher temperatures cause flames to rise faster.

Minimum

Establishes the lower limit for flame temperature. Higher temperatures cause flames to rise faster.

Smoke Color

Defines the hue of smoke released from burning material.

[Related references](INDEX.md).
