# Using UV Maps

## Using UV Maps

Using UV Maps

At some point, you'll want to apply image textures to your model using the UV Editor. The 3D Viewport shows your object being textured. Setting the 3D Viewport to Textured shading mode lets you see UV Editor changes immediately (and vice versa) through viewport shading, not actual rendering.

To render an image texture, you must:

Create a Material for the object.

Configure Blender to use UV textures for rendering.

Add a material by clicking Add New Material in the Shading context.

Two paths exist for using UV texture during rendering:

Quick method: use generated UV coordinates. Generated coordinates are the default for all Texture nodes except Image textures, which use UVs by default. Use the Texture Coordinate node's Generated output for images.

Standard method: use UV unwrapping to generate UV coordinates manually. Pair the Texture Coordinate node (UV output) or the UV Map node with a selected UV map (default: "UVMap").

See Image Textures for complete details.

Material is Essential for Rendering

You can UV texture a mesh in Blender without assigning a material and see it in textured viewport mode. However, render output will show default gray if no material is assigned, or black if no image is loaded. Without a texture using the image, the object renders according to procedural material settings alone.

Using Test Grids

For uniform pattern images that should look like cloth without stretching (unless intentional), test your UV mapping:

Two images show a test grid applied to UVs and the resulting geometry preview.

When rendered, the mesh displays the test grid. Blender includes a built-in test image: press New in the Image editor header and set Generated Type to UV Grid.

Modifying Image Textures

You can save textures as separate files (allowing easy swapping and external editing) or embed them in your project file (keeping everything in one .blend file).

[Related references](INDEX.md).
