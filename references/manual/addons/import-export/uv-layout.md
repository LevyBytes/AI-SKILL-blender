# UV Layout

## UV Layout

The UV Layout add-on saves a mesh's UV map out as an image through UV Editor ▸ UV ▸ Export UV Layout. It is on by default (otherwise enable "UV Layout" under Preferences ▸ Add-ons) and can write PNG, EPS, or SVG. Pick the faces in the 3D Viewport (not in the UV Editor). The drawing it produces is just the UV edge lines that land inside the UV Editor's standard grid; anything past that border is skipped, selected or not. People typically open that image in a paint program as a see-through guide while painting a texture, then load the finished texture back as part of a Blender material (see Image Textures for using images as textures).

Its properties: "All UVs" writes every UV instead of just the 3D-Viewport selection; "Export Tiles" chooses between the single [0,1] range and the complete set of UV tiles; "Modified" takes the UVs after the mesh's modifiers have been applied; Format is the file type (.png/.eps/.svg); Size is the pixel resolution; and Fill Opacity controls how opaque the fill is.

[Related references](INDEX.md).
