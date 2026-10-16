# Particle Edit Mode: Usage, Setup for Hair Particles, Setup for Particle, Cloth, and Soft Body Simulations, Bake the Simulation, Edit the Simulation, Selecting

## Particle Edit Mode

### Particle Edit Mode 

In Particle Edit Mode you alter keyframe points and paths of Hair, Particle, Cloth, and Soft Body simulations. (You can also sculpt and style hair prior to baking.)

Particle Edit Mode shares similarities with vertex editing in the 3D Viewport.

Important

Particle Edit Mode for hair is deprecated; use the new Empty Hair object and associated Sculpt Mode instead.

Important

Cached cloth simulation editing currently does not function; see: blender/blender#77114.

### Usage 

Tip

Only Frames Baked to Memory are Editable!

Check that you're not baking to a Disk Cache if particle editing is unavailable.

### Setup for Hair Particles 

- Create a Hair particle system.

- Apply an initial velocity in the Normal direction.

- Create a simulation.

- Enable the Hair Dynamics checkbox.

Editing hair strands in Particle Edit Mode. 

### Setup for Particle, Cloth, and Soft Body Simulations 

- Use Emitter particles or a cloth/soft body simulation.

- Initialize the simulation: place objects and emitters, define time range (narrow range for experimentation), configure the simulation, preview through playback.

### Bake the Simulation 

Once satisfied with the general simulation, bake from Object Mode. Baking must occur before editing becomes available.

### Edit the Simulation 

Switch to Particle Edit from the Mode menu in the 3D Viewport header to modify particle paths and keyframes. Press T in the 3D Viewport to reveal the Particle Edit toolbox. Navigate to the target frame and apply editing tools.

### Selecting 

Tip

Switch to Point select mode in the 3D Viewport header to view and select keypoints.

- Select single: LMB .

- Add to/remove from selection: Shift - LMB .

- All: A .

- None: Alt - A .

- Invert: Ctrl - I .

- Box select: B .

- Circle Select: C .

- Lasso Select: Ctrl - Alt - LMB .

- Select Linked: Position the cursor over a path and press L to include all its points in selection.

- Unselect Linked: Position the cursor over a path and press Shift - L to exclude all its points from selection.

- Root/Tips: Select ‣ Roots / Tips .

[Related references](INDEX.md).
