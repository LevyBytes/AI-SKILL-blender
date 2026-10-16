# Canvas: Settings, Surface, Surface Type

## Canvas

### Canvas

Reference

Panel :

Physics ‣ Dynamic Paint

Type :

Canvas

A Canvas accepts paint from Dynamic Paint brushes.

### Settings

Canvas main panel. 

Paint Surface
Dynamic Paint surface list. Surfaces behave as independent paint layers with individual parameters and separate baking.

Is Active
Toggles surface activity. Inactive surfaces skip computation.

Below, configure surface type and quality/timing adjustments.

Format
Each surface has format and type. Format decides how data stores and outputs.

Vertex :

Dynamic Paint operates on mesh vertex data. Results cache and display in viewports. Requires highly subdivided meshes.

Image Sequences :

Dynamic Paint generates UV-wrapped image files at specified resolution as output.

Resolution
Output image dimensions. 256 produces 256×256 output. Doubling resolution quadruples baking time.

Anti-Aliasing
5× multisampling edge smoothing.

Frame Start, End
Surface processing boundaries.

Sub-Steps
Extra frame samples, needed for very fast brushes.

### Surface

Reference

Type :

Canvas

Panel :

Physics ‣ Dynamic Paint ‣ Surface

Canvas advanced panel. 

Surface panel adjusts surface type and settings.

### Surface Type

Each surface has a "type" defining its role.

[Related references](INDEX.md).
