# Light Objects: Beam Shape

### Beam Shape

Spot option modifications update the spotlight's visual representation in the 3D Viewport.

Angle
The breadth of the outer cone of a spot light, which sets how broad the light disperses.
Narrower angles produce tight, focused projection, while broader angles create wider,
softer spread region.

This metric denotes the apex angle of the light cone in degrees,
and spans from 1.0° (tight projection) to 180.0° (expansive projection).

| Description | Description |
| --- | --- |
| Angle: 45° | Angle: 60° |

Blend
The Blend variable governs the interior cone of the spot.
The Blend figure can run from (0.0 to 1.0).
The figure is proportionate and conveys that portion of space that the interior cone must
fill in the outer cone Size .

The interior cone edge shows the boundary line where light from the spot will start to blurry/mellow;
previous to here it stays practically full strength.
Raising the Blend value creates blurrier/mellower spotlight limits,
and lowers the interior cone's round zone (by initiating blur/soften earlier).

To make the spot deliver a quicker fade price and therefore less blurry/mellow limits,
lower the Blend value.
At Blend of 0.0 you receive extremely sharp spotlight limits, zero transition in between light and dark.

The fade price of the spot light is determined by the gap separating Blend and Size values;
the bigger the round opening separating them, the more steady the light darkens separating Blend and Size .

Blend and Size regulate the spot light cone's opening and mellowness ("radial" falloff);
they do not regulate the shadow's mellowness as displayed below.

Render showing the mellow edge spotlighted zone and the crisp/firm item shadow.

Notice in the picture that the item's shadow stays crisp because of path-tracing,
whereas the spotlight openings turn mellow.
To get additional items casting mellow shadows inside the spot zone, you have to change further shadow settings.

Show Cone
Displays a semi-transparent column in 3D Viewport to show which items stay inside it.

[Related references](INDEX.md).
