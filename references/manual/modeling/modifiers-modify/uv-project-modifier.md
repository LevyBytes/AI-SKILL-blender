# UV Project Modifier

## UV Project Modifier

### UV Project Modifier

Projecting the Blender logo onto Suzanne.

Picture a slide projector and you've got the UV Project modifier. It throws a UV map out from the negative Z axis of some controller object (an empty, say) and lays that map onto the object everywhere the "light" falls.

Download an example.

### Options

The UV Project modifier.

UV Map
Picks which UV map gets modified. Defaults to the active rendering layer.

Aspect X/Y
Adjusts the image's aspect ratio. Takes effect only when a camera serves as the projector object.

Scale X/Y
Sizes the image up or down. Takes effect only when a camera serves as the projector object.

Projectors
As many as ten projector objects can be used.
Every face latches onto the nearest projector aligned with its surface normal.
The projections fire from the negative Z axis, that is straight down out of a camera or light.
Where the projector is a camera, the projection respects its perspective or orthographic setting.

Object
Names the projector object or objects.

### Usage

### General

UV Project shines for giving spotlights more variety, and likewise for laying down decals that break up repetition.

The usual move is to add an Image Texture node, pointed at the UV map
the modifier drives, into the object's material.

### Known Limitations

### Perspective Projection on Low Poly Meshes

Casting a perspective UV projection onto low poly geometry, a plane for instance, can throw up obvious artifacts.
It's a built-in shortcoming, since UV interpolation makes no allowance for perspective projection.

Subdividing the geometry can lessen the problem.

### Vertices Behind the Camera

Project geometry in a perspective view and any vertices sitting behind the camera don't get mapped correctly.
The way around it is to subdivide so the faces ahead of the camera end up with properly mapped UVs.

[Related references](INDEX.md).
