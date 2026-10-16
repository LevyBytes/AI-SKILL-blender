# Mesh Primitives: Common Options, Plane, Cube

## Mesh Primitives

### Mesh Primitives

Reference

Mode :

Object Mode, Edit Mode

Menu :

Add ‣ Mesh

Shortcut :

Shift - A

Meshes are the most common object type used in 3D scenes. As launch points for modeling, Blender ships a set of built-in mesh primitives. You can drop them in from either Object Mode or Edit Mode, and they show up at the 3D Cursor.

Blender's standard mesh primitives.

Tip

Flat primitives such as Plane , Circle , and Grid turn three-dimensional once you pull vertices off their starting plane.

Note

More primitives become available via add-on extensions. See Get Extensions for more information.

### Common Options

The Adjust Last Operation panel, shown right after creation, exposes these settings. The ones shared across more than one primitive are:

Generate UVs
Lays down a default UV unwrap for the new geometry, placing it in the first UV layer (adding that layer if there isn't one).

Align to View, Location, Rotation
See Common Object Options.

### Plane

A plain plane is one quad: four vertices, four edges, a single face. Flat and without thickness, it's strictly two-dimensional.

You'll see planes standing in for floors, walls, tabletops, or mirrors, and just as often serving as emitters, camera backdrops, or projection-mapping surfaces.

Size
The plane's width and height, edge to edge.

See also

Mesh Plane allows importing an image as a textured plane. The plane's dimensions are automatically scaled to match the image's aspect ratio.

Tip

A plane makes a good base for panels, ceilings, cloth sims, or sculpting surfaces. Run a modifier such as Subdivision Surface or Displace over it and the flat sheet becomes detailed geometry.

### Cube

Drops in a standard cube: six quad faces, eight vertices, twelve edges. Among the most fundamental and heavily used primitives, it's a natural starting block for boxes, crates, buildings, or sculpt bases.

Size
Total width, height, and depth, that is, the full diameter on each axis. At a size of 2 the cube reaches from -1 to +1 everywhere.

Tip

For hard-surface work the cube is the go-to base, and it pairs well with modifiers like Subdivision Surface , Boolean , or Bevel .

[Related references](INDEX.md).
