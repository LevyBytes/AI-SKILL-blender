# Sky Texture Node

## Sky Texture Node

### Sky Texture Node

This node builds a procedural sky, normally paired with the World Output Node.

### Inputs

Vector
Where the texture is sampled; with nothing plugged in it falls back to Generated coordinates.

### Properties

Sky Type
Sky model to use.

Single Scattering
An improved take on the 1993 model by Nishita et al, accounting for single bounces in the atmosphere. Legacy, and may be dropped in a future version.

Multiple Scattering
Based on this work by Fernando García Liñán, the most accurate model on offer since it accounts for multiple bounces of light in the atmosphere.

Preetham
Based on the 1999 paper by Preetham et al. Legacy, and will be dropped in a future version.

Hosek/Wilkie
Based on the 2012 paper by Hosek and Wilkie. Legacy, and will be dropped in a future version.

Note

Single and Multiple Scattering skies are, accurately, very bright by default. Lower the scene's Exposure in Properties ‣ Color Management ‣ Exposure to bring it down.

Sun Direction
Sun direction vector.

Turbidity
Atmospheric turbidity.

- 2: Arctic like

- 3: clear sky

- 6: warm/moist day

- 10: hazy day

Ground Albedo
How much light the planet surface bounces back into the atmosphere.

Sun Disc Cycles Only
Turn sun-disc lighting on or off.

Sun Size
Angular diameter of the sun disc (in degrees).

Sun Intensity
Multiplier for sun disc lighting.

Sun Elevation
How far the sun is rotated up from the horizon (in degrees).

Sun Rotation
How far the sun is rotated around the zenith (in degrees).

Altitude
Height above sea level of the camera. Place the camera on a beach and 0 is right; put it in an airliner cockpit and 10 km fits better.

Air
Density of air molecules. A value of 1 is roughly urban city air; 0 is no air.

Aerosols
Density of aerosol particles (water droplets). A value of 1 is roughly urban city aerosols; 0 is none.

Ozone
Density of ozone molecules, useful for pushing the sky bluer. A value of 1 is roughly urban city ozone; 0 is none.

### Outputs

Color
Texture color output.

### Examples

Example of lighting with Sky Texture.

[Related references](INDEX.md).
