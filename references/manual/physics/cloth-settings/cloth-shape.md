# Shape

## Shape

### Shape

Reference

Panel :

Physics ‣ Cloth ‣ Shape

Cloth Shape. 

Pin Group
Vertex group for pinning.

Pinning secures cloth by anchoring it to a Vertex Group. Methods include Weight Painting target areas. Per-vertex weight regulates pin intensity.

Stiffness
Anchor position stiffness.

Sewing
An alternative to pinning involves sewing springs—virtual springs pulling one part's vertices toward another part's. Unlike pinning (which locks vertices in place or to objects), sewing allows sliding. A cloak clasp instantiates this: sewing pulls corners about a character's neck with realistic freedom.

Create sewing springs by introducing edges in the mesh not belonging to faces. They join vertices that should draw together—like cloak corners.

Max Sewing Force
Highest force sewing springs can exert. Zero permits unbounded force but risks instability in early frames when ends separate widely.

Shrinking Factor
Cloth reduction factor; negative = growth.

Dynamic Mesh
Enables resting-shape animation via shape keys or modifiers (Armature, deformation modifiers) placed above the Cloth modifier. When active, the resting shape updates each frame, allowing unpinned cloth to squash and stretch with deforming characters yet move under physics control.

Typically cloth preserves the object's initial-frame shape, keeping it constant through the sim. This suits full realism but fails for cartoon characters using squash-and-stretch.

Rest Shape Key
Initiates cloth simulation from a selected Shape Key as the rest state, rather than evaluating shape keys and preceding modifiers normally. Mutually exclusive with Dynamic Mesh.

Lets you start the sim with pre-draped cloth without applying that shape as a plastic deformation that relaxes springs.

Visible only if the mesh contains shape keys.

[Related references](INDEX.md).
