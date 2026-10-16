# Color Ramp Widget: Controls, Shortcuts

### Controls
Inserts a fresh stop midway between the selected stop and its predecessor.

Removes the selected color stop.

Tools
Holds further operators for the color ramp.

Flip Color Ramp
Reverses the gradient, mirroring where the stops sit.

Distribute Stops from Left
Spreads the stops so each step leaves equal room on its right. Pairs best with Constant interpolation mode.

Distribute Stops Evenly
Spreads the stops so the gap between every pair of neighbors is identical.

Eyedropper E
An Eyedropper for pulling a color or gradient off the interface into the color ramp.

Reset Color Ramp
Returns the color ramp to its default state.

Color Mode
Picks the Color Model that interpolation runs in.

RGB :

Mixes each channel separately and recombines them.

HSV/HSL :

Converts first to HSV or HSL, mixes there, then recombines. The payoff is that saturation holds across differing hues, where the RGB route would wash out — yielding a richer gradient.

Color Interpolation
Which interpolation method runs along the ramp.

RGB

B-Spline :

Uses a B-spline interpolation for the color stops.

Cardinal :

Uses a cardinal interpolation for the color stops.

Linear :

Uses a linear interpolation for the color stops.

Ease :

Uses an ease interpolation for the color stops.

Constant :

Uses a constant interpolation for the color stops.

HSV/HSL

Clockwise :

Clockwise interpolation around the HSV/HSL wheel.

Counter-Clockwise :

Counterclockwise around the HSV/HSL wheel.

Near :

Nearest route around the wheel.

Far :

Furthest route around the wheel.

HSV and HSL interpolation options.

Active Color Stop
The active stop's index (drawn as a dashed line). Hands you a fallback way to pick a stop when it crowds others too tightly to grab on its own.

Position
Where the selected color stop sits in the range is set by this slider.

Color
A color field for setting the chosen stop's color and alpha.

### Shortcuts

- LMB (drag) moves color stops.

- Ctrl - LMB (click) adds a new color stop.

[Related references](INDEX.md).
