# Children: Roughness, Kink

### Roughness 

Reference

Panel :

Particle System ‣ Children ‣ Roughness

Use Roughness Curve

Provides Curve Widget as substitute for numeric input.

Uniform, Size

Varies strand paths according to child position, producing consistent variation for nearby children.

Endpoint, Shape

"Rough End" randomizes path completion (resembling inverse clumping). Shape ranges from <1 (parabolic) to 10.0 (hyperbolic).

Random, Size, Threshold

Follows random vector distribution, creating variance independent of spatial proximity. Threshold permits selective application to designated children only. Beneficial for generating isolated strays behaving differently.

### Kink 

Reference

Panel :

Particle System ‣ Children ‣ Kink

Child particles with Kink. 

From left to right: Curl, Radial, Wave, Braid, Spiral.

Kink manipulates child rotation around progenitor particles. Consult Fig. Child particles with Kink. above for different Kink category examples.

Kink Type

Nothing
Inactive.

Curl
Children spiral around the parent hair.

Radial
Children create wave geometry passing through parent hair.

Wave
Children form unidirectional waves.

Braid
Children weave around the parent hair.

Spiral
Creates spiral formations at hair endpoints.

Radius, Resolution

Establish overall scale dimensions.

Shape

Directs spiral expansion inward or outward.

Note

Alignment Limitations

Vertically oriented hair (along the designated spiral axis, typically Z) may not display spirals. This reflects a projection technique constraint. Tilting or randomizing hair orientation resolves this.

Amplitude

The maximum extent of the offset.

Clump

Magnitude of clump impact on kink amplitude.

Flatness

The degree of hair flatness.

Frequency

The oscillation repetition rate (1/strand length). Increased frequency produces more rotations.

Shape

Determines where rotation begins (rotation offset point).

[Related references](INDEX.md).
