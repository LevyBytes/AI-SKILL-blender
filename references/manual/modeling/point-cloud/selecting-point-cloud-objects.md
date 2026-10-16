# Selecting Point Cloud Objects

## Selecting Point Cloud Objects

### Selecting Point Cloud Objects

Working with point clouds in Edit Mode gives you a set of selection operators, covered here.
With them you can swiftly mark or clear points ahead of further editing or transformation.

### All

Reference

Mode :

Edit Mode

Menu :

Select ‣ All

Shortcut :

A

Marks every point in the cloud as selected.

### Select None

Reference

Mode :

Edit Mode

Menu :

Select ‣ None

Shortcut :

Alt - A

Clears the selection from any points currently selected in the cloud.

### Select Invert

Reference

Mode :

Edit Mode

Menu :

Select ‣ Invert

Shortcut :

Ctrl - I

Flips each point's selection state across the whole cloud:

- Anything that had been selected is now cleared.

- Anything that had been left out is now picked up.

A quick way to grab whatever you didn't already have selected.

### Select Random

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select Random

Picks out a random handful of the cloud's points.

Seed
The starting number fed to the pseudo-random generator.
Change it and a different set of points ends up randomly chosen.

Probability
A figure from 0.0 to 1.0 setting what share of points get picked.
Set it to 0.25, for instance, and about a quarter of the points are selected.

Useful for procedural modeling, scattering, or trying out effects with a randomly spread selection.

[Related references](INDEX.md).
