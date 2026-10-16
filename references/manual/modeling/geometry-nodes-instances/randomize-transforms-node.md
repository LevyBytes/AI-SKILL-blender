# Randomize Transforms Node

## Randomize Transforms Node

### Randomize Transforms Node

Randomize Transforms perturbs instances with random translation, rotation, and scale. Common use: natural variation in scattered objects (rocks, trees, etc.).

### Inputs

Instances
Input geometry containing instances.

Selection
Boolean: true = randomize, false = leave unchanged.

Local Space

- Enabled: transformations in each instance's local space.

- Disabled: randomization in global space.

Offset
Maximum translation per axis. Sets the random movement range.

Rotation
Maximum rotation per axis. Sets how much rotation varies.

Scale Axes
How scaling applies.

Uniform:
Single random scale factor for all axes.

Axes:
Independent factor per axis.

Scale
Maximum scaling amount.

Flipping
Randomly mirror instances along one or more axes.

Seed
Integer seed for the random-number generator. Different seeds yield different arrangements with identical parameters.

### Outputs

Instances
Result geometry with randomized instance transforms.

[Related references](INDEX.md).
