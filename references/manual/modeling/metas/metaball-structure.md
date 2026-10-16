# Metaball Structure

## Metaball Structure

A meta object is formally described as a directing structure that generates a static field—either positive or negative, causing neighboring structures to attract or repel.

The implicit surface emerges where this 3D field reaches a specific value. A ball meta, whose directing structure is a point, produces an isotropic field (uniform in all directions), so surfaces of constant field value form concentric spheres around that point.

Metas are mathematical expressions performing logical and arithmetic operations—AND, OR, addition, subtraction. This approach is called Constructive Solid Geometry. CSG uses minimal memory but demands significant computation.

Edit Mode allows changing the underlying structure type from the Active Element panel or the Sidebar Transform panel.

Ball (point structure) produces the simplest meta with no extra settings. The point generates an isotropic field, yielding a spherical surface.

Capsule (line-segment structure) is shaped by the field of a finite line segment, producing a cylinder with hemispherical ends.

Size X sets the line length (and capsule length).

Plane (rectangular structure) is shaped by the field of a rectangular plane, creating a box-like surface with uniform thickness and rounded borders.

Size X/Y specifies the rectangle width and height.

Ellipsoid (ellipsoid-volume structure) is shaped by an ellipsoid's field, yielding an ellipsoid surface.

Size X/Y/Z sets the ellipsoid dimensions.

Cube (cubic-volume structure) is shaped by a cubic volume's field, creating a box with rounded edges.

Size X/Y/Z specifies the cube dimensions.

[Related references](INDEX.md).
