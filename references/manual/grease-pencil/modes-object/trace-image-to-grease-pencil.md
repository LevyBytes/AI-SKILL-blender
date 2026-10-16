# Trace Image to Grease Pencil

## Trace Image to Grease Pencil

The Trace Image to Grease Pencil tool vectorizes a black-and-white image into Grease Pencil strokes. Non-monochrome images undergo internal conversion (hand conversion typically yields superior results). Opt for lower image resolutions; high resolutions yield excessively dense stroke geometry.

**Usage.**

Place an Image Empty in the scene. Execute Trace Image to Grease Pencil.

**Options.**

Target Object — whether the image empty persists or gets replaced:
- New Object: creates a new Grease Pencil object while preserving the image empty.
- Selected Object: substitutes the image empty with the Grease Pencil object.

Radius — width of the generated strokes.

Color Threshold — luminance cutoff; strokes form above this value.

Turn Policy — resolves ambiguities arising during the image-to-path conversion:
- Black: favors linking black (foreground) areas.
- White: favors linking white (background) areas.
- Left: always turns leftward at intersections.
- Right: always turns rightward at intersections.
- Minority: favors the rarest color locally.
- Majority: favors the most common color locally.
- Random: selects pseudo-randomly.

Mode — specifies whether input is a single image or a sequence:
- Single: the image empty represents one still or one frame from a sequence.
- Sequence: the image empty is a full image sequence.

Start at Current Frame — when active, the trace process starts from the current frame index.

Trace Frame — targets a specific image sequence frame; use zero for all frames.

[Related references](INDEX.md).
