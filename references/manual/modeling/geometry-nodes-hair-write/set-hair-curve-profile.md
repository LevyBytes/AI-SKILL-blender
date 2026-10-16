# Set Hair Curve Profile

## Set Hair Curve Profile

### Set Hair Curve Profile

Set Hair Curve Profile sets strand radius down the length via a customizable profile shape, giving artists control over thickness variation from root to tip — natural tapering or stylized width tweaks.

### Inputs

Geometry
Geometry — the hair-curve geometry fed in, whose radius gets modified.

Replace Radius
On, the node swaps the existing radius attribute for a new one. Off, the new radius multiplies into the existing value.

Radius
The base radius applied to every curve when Replace Radius is on, setting the overall scale of hair thickness.

Shape
How the radius shifts down the curve — for instance, a tapered profile with thicker roots and thinner tips.

Factor Min
The radius multiplier at each curve's start (root), steering how thick the curve begins.

Factor Max
The radius multiplier at each curve's end (tip), steering how thin the curve gets toward the tip.

### Outputs

Geometry
Output geometry with updated radius attributes down each hair curve.

[Related references](INDEX.md).
