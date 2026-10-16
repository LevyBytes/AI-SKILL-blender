# Mask: Mask From Face Sets Boundary, Mask by Color, Random Mask

### Mask From Face Sets Boundary

Reference

Mode:
Sculpt Mode

Menu:
Mask ‣ Mask from Face Sets Boundary

Builds a mask per Face Set isolation. Settings are provided
in the Adjust Last Operation section.

Mode
How the generated mask combines with present masking. Default substitutes the current mask via
"Mix".

Mix Factor
Blend proportion. Governs intensity of the fresh mask on the present one.

Automask Settings
Identical choices as the Auto-Masking configurations.

Propagation Steps
Identical to Auto-Masking.

### Mask by Color

Reference

Mode:
Sculpt Mode

Menu:
Mask ‣ Mask by Color

Select any hue on the geometry to generate masking (per the live color characteristic).

Threshold
How color divergence affects masking computation. Smaller scope limits related hues.
Broader scope captures significantly more matching hues.

Contiguous
Mask just touching color zones. Disconnected hues don't activate.

Invert
Flip the resulting masking.

Preserve Previous Mask
Maintain present masking and add or remove the fresh masking from hue choice.

See also

Mask by Color Tool

### Random Mask

Reference

Mode:
Sculpt Mode

Menu:
Mask ‣ Random Mask

Generates masking with random values for the full component per multiple connectivity options.

Per Vertex
Assigns distinct random masking for each point.

Per Face Set
Assigns distinct random masking for each Face Set.

Per Loose Mask
Assigns distinct random masking for each unattached component section.

[Related references](INDEX.md).
