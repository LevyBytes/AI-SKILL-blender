# Solver

## Solver

### Solver 

Reference

Panel :

Physics ‣ Soft Body ‣ Solver

This panel holds the controls that set how exact the soft body simulation comes out.

Step Size Min
The fewest sub-steps run for any one frame. Bump it up when a fast collider slips past the soft body unnoticed.

Max
The most sub-steps run for any one frame.
Ordinarily the Error Limit picks the count for you on the fly, so override it only with cause.

Auto-Step
Pick step sizes from how quickly things are moving.
This hands the solver a way to gauge its workload off scene velocities.

Error Limit
The headline knob for solution quality.
It dictates how tightly collisions are tested, making it the most consequential control here.
Try half the mean edge length as a first guess.
Drop it when jitter, visible errors, or exaggerated reactions show up.
Tracking its own error level is what lets the solver shift to adaptive step sizing.

### Diagnostics 

Print Performance to Console
Reports the solver's running status to the console.

Estimate Transforms
Estimate matrix, split to COM , ROT , SCALE .

### Helpers 

The controls below shape a soft body's reaction as it approaches, or bites into, a fellow collider on its layer.

Choke
Once a vertex or edge digs into a collision mesh, this tames its exit speed.

Fuzzy
A collision fuzziness factor; turning it up trades stability for quicker handling.
You end up with a faster yet rougher result.

[Related references](INDEX.md).
