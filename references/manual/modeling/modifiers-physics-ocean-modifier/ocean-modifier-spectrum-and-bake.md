# Ocean Modifier: Spectrum, Bake, Example

### Spectrum

Spectrum
Picks which wave spectrum model gets used.
Wave spectra describe how energy travels through waves at various frequencies.
That energy moves differently depending on the water's depth and the wind speed.

Turbulent Ocean
For turbulent seas carrying foam (Phillips).

Established Ocean
For a broad, established ocean stretching for miles
with wind blowing for days, long enough for the waves to settle into equilibrium (Pierson-Moskowitz method).

Established Ocean (Sharp Peaks)
Much like plain Established Ocean, except the waves keep growing over time,
sharpening the peaks ( JONSWAP and Pierson-Moskowitz method).
An additional parameter sets how sharp those peaks get.

Shallow Water
For shallow water under roughly 10 meters deep, which makes it ideal
for small lakes and ponds without strong wind (JONSWAP and TMA – Texel-Marsen-Arsloe methods).

| Turbulent Ocean. | Established Ocean. |
| --- | --- |
| Established Ocean (Sharp Peaks). | Shallow Water. |

Sharpness Peak
A contrived factor governing how sharp the wave peaks come out in
the Established Ocean (Sharp Peaks) and Shallow Water spectrum models.

Fetch
The fetch is the distance out from a lee shore, the run over which the wind holds a steady speed.
Both the Established Ocean (Sharp Peaks) and Shallow Water spectrum models draw on it.

### Bake

Rather than running the ocean data live, you can bake it out to files in a directory of your choosing. After a sim is baked, the simulator engine drops out of the picture completely and everything the modifier or texture needs is read back from the baked files.

Baking has the following advantages:

- Pulling stored data is quicker than working it out afresh.

- It opens the door to rendering ocean data in outside renderers.

- It makes richer foam maps possible.

The sim data lands as sequences of OpenEXR image maps,
one apiece for displacement, normals, and foam (where foam is set to be generated).
As these baked files load, each frame of the bake sequence gets held
in memory the moment it's read. So reaching those loaded frames again later is quick,
sparing you the cost of going back to the drive.

Because these baked files are ordinary OpenEXR's,
any other application or renderer that reads the format can open and render them too.

Cache Path
The folder where the baked EXR files are kept.
The sequences take the form disp_####.exr , normal_####.exr ,
and foam_####.exr , where #### is the four digit frame number.
Should the cache path folder not exist, it gets created.

Frame Start, End
Which frames of the simulation to bake (inclusive).
Reaching for frames outside the baked span just repeats the bake's start and end frames.

Foam Fade
Baking brings better foam handling along with it. Running live,
the ocean simulator fetches data only for the current frame.
For the foam map, that amounts to the tips of the wave crests on that one frame.
In real life, once wave interactions throw up foam,
it lingers atop the wave surface for a time as it breaks apart. Baking lets you
approximate that, gathering foam from earlier frames
so it stays sitting on the surface.

### Example

Blender built and rendered the example below;
notice the white wave crests, an effect the foam data produces.

[Related references](INDEX.md).
