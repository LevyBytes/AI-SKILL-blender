# Render Baking: Selected to Active, Output, Margin

### Selected to Active 

Bakes the shading off the selected objects' surfaces onto the active object.
The rays head inward from the low-poly object toward the high-poly one.
Where the high-poly object is not fully wrapped by the low-poly one, set where the rays start through Max Ray Distance or Extrusion (which one depends on whether you run a cage).
For tighter control still, bring in a Cage Object .

Note

Every object you bake from carries a fixed CPU memory cost. Join the high-poly objects before baking to keep memory from running out and crashing.

Cage
Fire the rays at the active object off a cage.
Picture the cage as the low-poly mesh puffed outward, formed for you from the ray distance or set up by hand from an object you point to.
Drop the cage and the rays ride the mesh normals, which litters the edges with glitches, yet that is the wiser route when you bake onto planes, since it spares you extra edge loops.

Cage Object
The object to stand in as cage, rather than deriving one from the active object with Cage Extrusion .

Cage Extrusion
The inward ray-cast distance once Selected to Active and Cage are both at work.
The inward rays fire from a copy of the active object with its Edge Split Modifiers off.
Keep clear of hard splits, an applied Edge Split Modifier for one, since they hand you non-smooth normals around the edges.

Note

When extruding the base mesh comes up short, copy that mesh and reshape the copy to serve as a Cage .
The two meshes must share one Topology, meaning an identical face count and face order.

Max Ray Distance
The inward ray-cast distance under Selected to Active .
On offer only when no Cage is running.

### Output 

Target
Where the baked map goes.

Image Textures :

Bake to the image data-block bound to the active, selected Image Texture node. Should a material carry no active, selected image texture node, nothing bakes for it.

Clear Image
When on, wipes the image clean before the bake render.

Active Color Attribute :

Send the bake into the active mesh's Active Color Attributes layer.
Mind that the active object has to be a mesh, since other object types own no Color Attributes.

### Margin 

When baking to images, Blender by default lays a margin around each UV "island."
This wards off breaks at UV seams that texture filtering and mip-mapping would otherwise bring.

Type
How the margin gets built.

Extend :

Push the border pixels out past the edge.

Adjacent Faces :

Pull pixels from the neighboring faces across each UV seam to pack the margin.

Size
The margin's width in pixels.

[Related references](INDEX.md).
