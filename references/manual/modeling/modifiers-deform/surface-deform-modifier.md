# Surface Deform Modifier

## Surface Deform Modifier

The Surface Deform modifier uses an arbitrary mesh surface to control deformation of another, transferring its motion to the target. This is useful for cloth-simulation proxies that drive the motion of more detailed, simulation-unsuitable meshes.

Target specifies the surface to bind (unavailable after binding).

Target Mesh Validity

The target mesh must satisfy constraints; violating them prevents successful binding:

No edges may have more than two adjacent faces.

Faces must be convex (not concave).

No overlapping vertices (doubles).

Faces must not have collinear edges.

Interpolation Falloff controls how much vertices bound to one target face are affected by surrounding faces (unavailable after binding). Low values smooth deformations but may introduce slight artifacts.

Strength sets the overall modifier influence.

Vertex Group enables per-vertex influence control.

Invert reverses the group influence.

Sparse Bind records bind data only for vertices with nonzero group weights at binding time—an optimization that requires rebinding if new vertices are added to the group.

Bind connects the modified mesh's current state to the target mesh's current state. Afterward, target mesh changes deform the modified mesh. Binding is necessary; an unbound modifier has no effect.

Unbind, available after binding, disassociates the modified mesh from the target and reverts the modified mesh to its pre-binding shape.

Note: meshes are bound using global coordinates, but later object transformations are ignored. Objects can be freely moved and rotated after binding without affecting behavior. Only changes to the target's geometry itself matter.

Note: if the mesh deviates significantly from the target surface, artifacts become likely. Reasonably well-matched meshes produce better results.

[Related references](INDEX.md).
