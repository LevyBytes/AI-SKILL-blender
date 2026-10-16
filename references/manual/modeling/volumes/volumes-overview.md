# Introduction

### Introduction

In Blender, a Volume object amounts to a thin shell wrapped around an OpenVDB file.
OpenVDB is both a library and a file format built for storing volumetric data and moving it between programs.
Other software, Houdini among them, can produce OpenVDB files,
as can Blender's own fluid simulation cache.

You make Volume objects from the Add menu in the 3D Viewport,
or simply by dragging vdb-files and dropping them into Blender.
To animate, bring in a frame sequence of OpenVDB files.

WDAS cloud data set rendered in wireframe, Workbench, and Cycles.

### Rendering

Rendering volumes works just like rendering smoke simulations. By default,
the Principled Volume shader
handles volume objects. It looks for grids named density ,
color and temperature out of the box. When those aren't around,
you'll need to point the shader nodes at a different grid name.

### Limitations

- OpenVDB is great at holding sparse volumes — ones that aren't packed
into a tight bounding box but may sprawl across space.
In Blender, though, they still get rendered as dense volumes,
which isn't great for performance or memory. A future release will improve this.

- OpenVDB files can additionally hold level sets and points.
Level set grids can be read, but rendering them as surfaces isn't supported yet.
Importing OpenVDB points isn't supported either.

[Related references](INDEX.md).
