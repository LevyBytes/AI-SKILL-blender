# Mesh Deform Modifier

## Mesh Deform Modifier

The Mesh Deform modifier uses an arbitrary closed mesh as a deformation cage, allowing it to control another mesh's shape.

Setup is straightforward but binding computation can be slow.

Object specifies the cage mesh.

Vertex Group restricts deformation to group vertices; others remain unchanged.

Invert reverses the group influence.

Precision controls cage-to-deformed accuracy. Higher values increase binding calculation time but improve cage mapping accuracy.

This setting is unavailable after binding.

Dynamic, when enabled, factors other mesh-altering features (modifiers, shape keys) into binding for better deformation quality.

Dynamic is off by default to reduce memory and binding time. Unavailable after binding.

Bind connects the modified geometry's current vertices to the deforming cage.

An unbound Mesh Deform modifier has no effect; binding is necessary for the cage to alter the modified object.

Warning: depending on modifier settings and cage/object complexity, binding may take significant time, potentially freezing Blender. Save before proceeding; memory exhaustion and crashes are possible.

Unbind, after binding is complete, disassociates the modified object from its cage. The cage retains its current shape; it does not reset. The modified object reverts to its pre-binding shape.

To preserve the original cage form, save a copy before altering it.

Significant whole-cage transformations (like inversion) can introduce artifacts. Higher Precision reduces them but cannot eliminate them entirely—this is an inherent limitation.

Ensure cage mesh normals point outward (they determine inside/outside).

Additional faces inside the cage—loose or forming smaller cages—provide extra control. Smaller cages may overlap the main cage. For instance, small sphere cages around eyes enable fine eye deformation.

[Related references](INDEX.md).
