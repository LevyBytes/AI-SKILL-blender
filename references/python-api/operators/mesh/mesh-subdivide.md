# bpy.ops.mesh.subdivide

bpy.ops.mesh. subdivide ( * , number_cuts = 1 , smoothness = 0.0 , ngon = True , quadcorner = '`STRAIGHT_CUT`' , fractal = 0.0 , fractal_along_normal = 0.0 , seed = 0 ) 

Slice chosen spines into pieces

Parameters :

- number_cuts ( int ) – Number of Cuts, (in [1, 100], optional)

- smoothness ( float ) – Smoothness, How much to smooth (in [0, 1000], optional)

- ngon ( bool ) – Create N-Gons, When off, fresh faces get 3 or 4 corners only (optional)

- quadcorner ( Literal [ 'INNERVERT' , 'PATH' , '`STRAIGHT_CUT`' , 'FAN' ] ) – Quad Corner Type, How to split rectangular edges (anything but Straight Cut blocks n-gons) (optional)

- fractal ( float ) – Fractal, Randomness scaling (in [0, 1e+06], optional)

- fractal_along_normal ( float ) – Along Normal, Include fractal jitter perpendicular to the surface only (in [0, 1], optional)

- seed ( int ) – Random Seed, Seed to feed the randomizer (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
