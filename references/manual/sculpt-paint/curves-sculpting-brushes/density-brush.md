# Density Brush

## Density Brush

### Density Brush

Create (or remove) curves based on a target distance. It generates a high number of points and then rejects the ones that are too close to existing points.

### Brush Settings

Density Mode
Determines whether the brush adds or removes curves.

Auto :

Either add or remove curves depending on the distance between existing curve roots under the cursor.

Add :

Add new curves between existing curves, taking the minimum distance into account.

Remove :

Remove curves whose root points are too close.

Distance Min
Goal distance between the curve roots.

Edit Minimum Distance R
Interactively sets the Distance Min value by displaying a graphic inside the brush cursor, giving a representation of the density.

The density can be adjusted by moving the mouse cursor closer or farther from the paint cursor. The Distance Min will be changed once the operator is confirmed.

Count Max
The maximum amount of points that the brush tries to sample in the surface.

[Related references](INDEX.md).
