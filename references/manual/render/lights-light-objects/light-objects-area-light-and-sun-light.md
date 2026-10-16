# Light Objects: Area Light, Sun Light, Power of Lights

### Area Light

The area light replicates light released from a plane (or plane-approximation) supplier.
For instance, a movie screen, office fluorescent bulb, portal, or layers of clouds are samples of area light. The area light yields shadows with
gentle limits by sampling a light via a lattice the breadth of which comes from the designer.
This differs sharply from dot-like synthetic lights which yield sharp limits.

Power
Output measure of the light. Greater amounts boost the light's strength.
Negative quantities are permitted, however should get sidestepped for authentic plus unbiased outcomes.

Shape
Projection form of the light.

Rectangle :

The light form can get depicted as a four-sided shape plus modified with the "X" plus "Y" values.

Square :

The light form can get depicted as a four-sided shape plus modified with the Size variable.

Disk :

The light form can get depicted as a rounded shape plus modified with the Size variable.

Ellipse :

The light form can get depicted as an elliptical form plus modified with the X plus Y values.

Tip

Choosing the fitting projection for your area light improves the genuineness of your setting.
For instance, you could build an internal setting plus would like to mirror light moving through an entrance.
You could position a Four-sided area light inside an entrance (up) or from fluorescent bulbs (sideways)
with suitable ratio for Size X plus Size Y . For the simulation of the light released by
a movie screen, an up-facing Four-sided area light suits greatest in typical scenarios.

Size / Size X / Size Y
Dimensions for the Square or Rectangle .

### Sun Light

A sun light provides light of constant intensity emitted in a single direction from infinitely far away. It can be very handy for a uniform clear daylight open-space illumination. In the 3D Viewport, the sun light is represented by an encircled black dot with rays emitting from it, plus a dashed line indicating the direction of the light.

Note

This direction can be changed by rotating the sun light, like any other object, but because the light is emitted from a location considered infinitely far away, the location of a sun light does not affect the rendered result.

Strength
Strength of the lights. See more details at Power of Lights.

Angle
The size of the sun light according to its angular diameter as seen from earth.

### Power of Lights

When Normalize is enabled, the power of sun lights is specified in Watts per square meter. The power of point lights, spot lights, and area lights is specified in Watts.

But this is not the electrical Watts that consumer light bulbs are rated at. It is Radiant Flux or Radiant Power which is also measured in Watts. It is the energy radiated from the light in the form of visible light.

If you want to set the power to real world values, you have to convert the wattage of consumer bulbs or LED lights to radiant flux, but it is not a straightforward process. The wattage of bulbs means the electrical power required to power them. LED lights have a "Watt equivalent" which is neither the electrical power they require nor the amount of light they put out. Some consumer lights specify lumens or luminous flux which is the radiant flux weighted with the wavelengths perceived by the human eye.

To save you from doing the conversion, here is a table of typical power values for point, spot, and area lights:

| Real world light | Power | Suggested Light Type |
| --- | --- | --- |
| Candle | 0.05 W | Point |
| 800 lm LED bulb | 2.1 W | Point |
| 1000 lm light bulb | 2.9 W | Point |
| 1500 lm PAR38 floodlight | 4 W | Area, Disk |
| 2500 lm fluorescent tube | 4.5 W | Area, Rectangle |
| 5000 lm car headlight | 22 W | Spot, size 125 degrees |

And a table of typical Strength values for sun lights:

| Sun type | Strength |
| --- | --- |
| Clear sky | 1000 W/m 2 |
| Cloudy sky | 500 W/m 2 |
| Overcast sky | 200 W/m 2 |
| Moonlight | 0.001 W/m 2 |

These values will produce much brighter or dimmer lights than you would expect, because our eyes adapt while a render engine does not. So to compensate, adjust the Exposure in Render ‣ Film .

To get realistic results, remember to also set the light size and color to realistic values. The color of your lights will also influence how bright they appear to the human visual system. If you leave the power unchanged, a green light will seem the brightest, red darker and blue the darkest. Thus you might want to manually compensate for these perceived differences.

[Related references](INDEX.md).
