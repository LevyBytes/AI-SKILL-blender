# Introduction

### Introduction

To start a mask, flip an Image or Movie Clip editor's header mode over to Mask.
Doing so brings up the tools and properties masks need in the editor panels
while tucking away the ones that don't apply.

Masks serve plenty of purposes. In a motion tracking workflow they can mask out
or steer a particular object within the footage.
They handle manual rotoscoping to lift an object out of the footage,
or act as a rough matte for green-screen keying. Since a mask isn't bound to any one image or movie clip,
it works just as well for building motion graphics or other Compositor effects.

Using the Mask node to isolate an object in compositing.

Masks get edited in the Movie Clip Editor and Image Editor,
whereas the Compositor and Sequencer merely consume masks that already exist.

A mask can be animated over time so it tracks some object in the footage —
a running actor, for instance. Pull that off with shape keys, or by parenting the mask to tracking markers.

### Mask Data-block

A mask data-block bundles together multiple mask layers and splines.
It's the top-level entity used for masking.
Masks can be reused across different places and carry global parameters covering every entity inside them.

[Related references](INDEX.md).
