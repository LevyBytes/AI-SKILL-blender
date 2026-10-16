# Curve bevel cross sections

Bevel:

Apply a Bevel to turn the 1D line (or 2D ribbon with Extrude)
into a 3D tube.

Round:

The tube's cross section is circular (or pill-shaped with Extrude).
Half circles are possible via Fill Mode.

Depth
Cross-section size.

| Description | Description |
| --- | --- |
| Small Depth.  | Large Depth.  |

Resolution
Count of cross-section vertices.

| Description | Description |
| --- | --- |
| Low Resolution creates blocky mesh.  | High Resolution creates smooth mesh.  |

Fill Caps
Seal tube ends.

Object:

Fully customize cross-section shape using a separate Curve object.

Object
The curve defining the cross section. May be closed (cyclic)
or open.

Important

This curve must lie flat in its local XY plane; other planes produce unexpected results.

Note

If the selected curve has modifiers, they don't apply.
The bevel uses the original curve shape. This is because curves become meshes
when they have modifiers; at that point they can't serve as cross section curves.

Workaround: disable beveling on the path curve, then add geometry nodes:
use an Object Info Node to fetch the cross section curve,
convert it from mesh back to curve via a Mesh to Curve Node,
and finally send both to a Curve to Mesh Node.

Profile:

Customize cross-section shape without a separate Curve object. Unlike the Object option where the curve fully defines the cross section,
the Profile in the Curve Widget defines a quarter which repeats and mirrors.

Black dots show sample points (where mesh vertices form). Increase Resolution for more samples and smoothness.

Preset
Choose predefined profiles instead of building your own.
Support Loops and Steps presets generate based on Resolution
and need reapplication if you change it.

Reverse Path
Mirror the profile along the diagonal.

Toggle Profile Clipping
Restrict control point X and Y coordinates to [0, 1].

Sample Straight Edges
Sample the profile at the middle of perfectly straight segments
(lines between Vector-handle points).
Disabled by default, as sampling at control points usually suffices.

Sample Even Lengths
By default, each profile segment gets the same sample point count.
Enable to distribute sample points evenly
across the entire profile length.

[Related references](INDEX.md).
