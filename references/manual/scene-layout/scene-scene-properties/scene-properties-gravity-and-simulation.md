# Scene Properties: Gravity, Simulation, Keying Sets, Audio, Rigid Body World

### Gravity

Reference

Panel :

Properties ‣ Scene ‣ Gravity

Options governing universal gravity for simulation effects.

Consult the Physics documentation for thorough information.

### Simulation

Simulation Range
Apply a simulation period distinct from the scene period for
Simulation Nodes
that don't establish their own frame bounds.

Start, End
The frame at which simulation commences/terminates.

### Keying Sets

Reference

Panel :

Properties ‣ Scene ‣ Keying Sets

See Keying Sets.

### Audio

Reference

Panel :

Properties ‣ Scene ‣ Audio

Options managing universal sound characteristics.
For control of sound replay from within Blender itself, consult the sound options
in the Settings.

Volume
Sound magnitude for the scene.

Distance Model
Specifies how volume reduction relates to distance.
The Inverse method is most physically accurate,
though linear and exponential options exist as alternatives.
The clamped versions restrict volume to not exceed 100% (1.0),
meaning that if separation is smaller than the baseline separation, volume remains 100%.
For in-depth explanations of each mode
consult the OpenAL specification.

Doppler Speed
Sound velocity for Doppler shift math.
The standard measurement is 343.3 m/s in standard conditions, around 1560 m/s in seawater for instance.

Doppler Factor
Affects the magnitude of the Doppler shift.
You can amplify or minimize pitch variation intensity, with 1.0 being physically accurate.

Update Animation Cache
Refreshes the sound animation record. Beneficial if audio artifacts emerge.

### Rigid Body World

Reference

Panel :

Properties ‣ Scene ‣ Rigid Body World

The Rigid Body World organizes rigid body components,
supplying parameters applicable to each rigid body within the environment.

See Rigid Body World for detailed documentation.

[Related references](INDEX.md).
