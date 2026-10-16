# IES Texture Node

## IES Texture Node

### IES Texture Node

The IES Texture matches real-world lights using IES files ( IES ). An IES file records how a light source spreads its intensity across directions.

### Inputs

Vector
Coordinate used to look the light distribution up; with nothing supplied it takes the normal.

Strength
Light strength multiplier.

### Properties

Mode
Where the IES file is loaded from.

Internal :

Use an IES profile embedded in a text data-block inside the blend-file, which makes it easy to ship.

External :

Load an IES profile from a file on the drive.

### Outputs

Factor
Light intensity, usually fed into the Strength input of an Emission node.

### Examples

Lights with different IES profiles.

[Related references](INDEX.md).
