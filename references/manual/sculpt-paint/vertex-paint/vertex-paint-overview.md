# Introduction

### Introduction

Vertex Painting constitutes a direct approach to applying color to objects by modifying vertex pigmentation rather than texture data. It operates straightforwardly. Vertex Painting saves color information as a Color Attribute, usable by various rendering systems.

Color attribute selections appear in the header's palette selector.

Vertex Painting Mode.

As a vertex receives color application, the vertex pigmentation changes per brush parameters. The pigmentation flows across all exposed faces and edges touching that vertex, transitioning toward adjacent vertex colors. Occluded face coloring remains unchanged.

See also

Dynamic Paint
can create Color Attribute information during physics and animation playback.

### Viewing Color Attributes

Within material node systems, Color Attributes are available via the Color Attribute Node.

Color Attributes display in the 3D viewport through the Workbench engine. Activate this: switch the Viewport to Solid Shading and select Attribute Color option.

[Related references](INDEX.md).
