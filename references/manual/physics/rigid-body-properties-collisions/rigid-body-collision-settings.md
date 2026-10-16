# Collisions: Physics ‣ Rigid Body ‣ Collisions, Rigid Body Collisions panel.

## Collisions

### Collisions 

Reference

Panel :

Physics ‣ Rigid Body ‣ Collisions

Rigid Body Collisions panel. 

Shape
Determines object collision shape; categories include primitives and mesh-based shapes.

Primitive shapes ( Box , Sphere , Capsule , Cylinder , and Cone )
optimize memory and speed but may not match actual geometry.
Bounding-box dimensions determine size; geometric centers provide mass-center locations.
Enabling Extras Overlay visualizes primitives.

Mesh-based shapes ( Convex Hull and Mesh ) derive from actual geometry, offering better representation.
Object origin defines mass center for these shapes.

Box :

Box-like geometry (cubes), including ground planes.
Bounding-box axes determine per-axis dimensions.

Sphere :

Sphere geometry.
Radius: the bounding box's largest axis.

Capsule :

Points toward the Z axis.

Cylinder :

Points toward the Z axis.
Height from Z axis; radius from the larger of X or Y axes.

Cone :

Points toward the Z axis.
Height from Z axis; radius from the larger of X or Y axes.

Convex Hull :

Mesh-like surface encompassing all vertices (shrink-wrapped geometry).
Convex approximation offering good performance and stability with fewer vertices.

Mesh :

Triangle-only mesh allowing detailed interactions beyond convex hulls.
Enables concave shapes, though slower and less stable.

Compound Parent :

Combines child collision shapes.
Enables concave construction from primitives, typically faster than Mesh shapes and more stable.

Source
Mesh source for collision-shape generation.

Base :

The object's base geometry.

Deform :

Applies shape keys and deform modifiers.

Final :

Includes all deformations and modifiers.

Deforming
Mesh shapes deform during simulation.

[Related references](INDEX.md).
