# Texture paint perspective limitations

### Introduction

### Perspective View & Faces Behind the View

When painting faces partly outside the perspective view, those faces resist painting. To fix this, back away or switch to orthographic perspective.

### Perspective View & Low Poly

In perspective mode, painting low-resolution objects with normals pointing away from you may fail; deactivate Normal Falloff in stroke settings to work around this.

Typically happens when painting cube sides (see Blender bug #34665).

[Related references](INDEX.md).
