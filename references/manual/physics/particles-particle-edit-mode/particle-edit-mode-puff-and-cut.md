# Particle Edit Mode: Puff, Cut, Weight, Common Options, Options, Cut Particles to Shape, Viewport Display, Editing

### Puff 

Rotates hair around the root keypoint: adds vertical lift with Add or flattens with Sub.

Puff Volume
Applies puff to unselected endpoints, maintaining volume during root adjustment.

### Cut 

Scales segments until the final keypoint reaches brush position.

### Weight 

Particularly valuable for soft-body animation, where weight defines soft-body Goal.
A weight of 1 prevents motion; a weight of 0 allows full soft-body influence.
Soft body goal strength scaling multiplies this value.

### Common Options 

Brush settings appear below type selection:

Radius F
Set the brush radius.

Strength Shift - F
Establish brush effect magnitude (inapplicable to Add).

### Options 

Reference

Mode :

Particle Edit Mode

Panel :

Tool Settings ‣ Options

Auto-Velocity Emitter
Recompute particle velocities from edited paths; otherwise preserves original velocity regardless of actual displacement.

Mirror X
Enable symmetric editing along the local X axis.

Preserve

Strand Length
Keep keypoint spacing constant during combing or smoothing by adjusting other keypoints.

Root Positions
Lock the first keypoint to prevent hair transplanting.

### Cut Particles to Shape 

Shape Object
A mesh object whose boundary governs the Shape Cut tool.

Cut
A grooming operation that clips hair according to the Shape Object boundary. Avoids tedious manual cutting of protruding sections, especially on highly furred characters.
Works effectively for large areas compared to individual-plane cutting.

| Description | Description |
| --- | --- |
| Before.  | After.  |

### Viewport Display 

Path Steps
Number of steps used to render the path; increases smoothness.

Children Hair
Toggles display of child particles, enabling fine-tuning of effects while risking performance impact on high-child-count systems.

Particles Emitter
Overlays particles atop paths.

Fade Time
Fades paths and keys distant from the current frame.

Frames
Fade frame count.

### Editing

[Related references](INDEX.md).
