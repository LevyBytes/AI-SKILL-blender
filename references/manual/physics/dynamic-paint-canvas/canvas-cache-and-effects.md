# Canvas: Cache, Effects, Initial Color, Output, Vertex, Image Sequence

### Cache

Reference

Type :

Canvas

Panel :

Physics ‣ Dynamic Paint ‣ Cache

Canvas cache panel. 

Currently visible for Vertex format only. Adjust and bake point cache here.

### Effects

Reference

Type :

Canvas

Panel :

Physics ‣ Dynamic Paint ‣ Effects

Effects panel. 

For "Paint" surfaces, generates animated canvas movement.

Effects

Spread
Paint expands gradually to adjacent points, filling connected zones.

Drip
Paint flows by Blender force fields, gravity, and velocity with user adjustments.

Shrink
Painted area gradually contracts and vanishes.

Spread and Drip affect "wet paint" only; drying slows motion until stopping.

### Initial Color

Reference

Type :

Canvas

Panel :

Physics ‣ Dynamic Paint ‣ Initial Color

Sets the canvas starting color. (Todo 2.62)

- None

- Color

- UV Texture

- Vertex Color

### Output

Reference

Type :

Canvas

Panel :

Physics ‣ Dynamic Paint ‣ Output

Canvas Output panel. 

Output panel controls how the surface sends results.

### Vertex

For Vertex format, select a mesh data layer (color/weight by surface type) for output. "+"/"-" icons add/remove named layers. Missing layers appear red.

### Image Sequence

For Image Sequence surfaces, specify UV maps, output directory, filename, and format.

[Related references](INDEX.md).
