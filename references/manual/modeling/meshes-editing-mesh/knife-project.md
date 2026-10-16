# Knife Project

## Knife Project

### Knife Project 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Knife Project

Casts the silhouette of one or more "cookie cutter" objects onto the edited object, cutting fresh
edges where it lands.

Cutter objects have to be Curves or non-manifold meshes — flat shapes, loose edges, and the like.

Tip

Select Non-Manifold will highlight the cutting edges
of mesh objects.

Projection is done along the viewing direction.

### Usage 

- Select the object(s) that should receive the cut and switch to Edit Mode .

- Select the object(s) that should perform the cut by clicking them with Ctrl - LMB in the
3D Viewport or the Outliner.

- Click Mesh ‣ Knife Project in the menu.

Should Blender drop back to Object Mode as you pick the cutter objects, check that
Edit ‣ Lock Object Modes is ticked in the topbar.

### Options 

Cut Through
Drives the cut through the whole mesh, back faces you can't see included.

### Examples 

| Before projecting from a text object.  | Resulting knife projection.  |
| --- | --- |
| Before projecting from a mesh object.  | Resulting knife projection (extruded after).  |
| Before projecting from a 3D curve object.  | Resulting knife projection (extruded after).  |

### Known Limitations 

Cut several meshes at once in Edit Mode and geometry from one of them won't block separate mesh
objects sitting behind it.

[Related references](INDEX.md).
