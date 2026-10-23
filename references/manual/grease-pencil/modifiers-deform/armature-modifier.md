# Armature Modifier

## Armature Modifier

The Armature Modifier erects skeletal rigs for pose animation of characters and other poseable assets.

Attaching an armature to an object enables automatic deformation, freeing geometry from hand-keyframing requirements.

See also: armature section for armature mechanics.

This documentation covers the Armature Modifier tailored to Grease Pencil objects. For other object types, consult the general Armature Modifier.

**Options.**

Object: the armature object referenced by this modifier.

Vertex Group: the object's vertex group whose weights regulate this modifier's blending with other Armature modifiers.

Applies only when at least two Armature modifiers coexist on the same object with Multi Modifier engaged.

Invert: reverses the vertex group's influence directivity (flips weight polarity).

Bind to:
- Vertex Groups: when active, bones by name deform points in vertex groups of the same name (e.g., a "forearm" bone affects only "forearm" group points). Influence scales with the point's group weight—precise but setup-intensive versus Bone Envelopes.
- Bone Envelopes: when active, bones warp adjacent points per each bone's envelope span and reach; switch on/off per deformation need.

The Armature modifier constructs skeletal rigs for posing and animating characters and deformable objects.

By binding an armature system to geometry, that shape deforms according to the rig's bone movements without manual vertex-by-vertex animation.

The modifier panel displays the armature object name.

Vertex Group restricts the modifier's output blending to vertices in a specified group—useful only when multiple Armature modifiers are active with Multi Modifier enabled.

Invert reverses the group's weight influence.

Preserve Volume uses quaternion-based deformation to prevent volume loss during high-angle rotations. Without it, geometry near joints shrinks as bones rotate far from rest position (nearly to zero at 180°). With it enabled, the geometry stays full but develops a discontinuity at exactly 180°.

Multi Modifier uses output from a previous modifier (typically another Armature) as its input, allowing multiple armatures to deform the same geometry independently rather than sequentially. Results mix using vertex-group weights as blending guides.

Armature modifiers can be quickly stacked by parenting objects to an armature.

Bind to selects how the armature links to the mesh.

Vertex Groups (for meshes and lattices): bones named identically to vertex groups deform only those group vertices, weighted by their values. This is precise but setup-intensive.

Bone Envelopes: bones deform nearby vertices within their envelope radius and falloff distance. Less precise but faster to set up.

When envelopes are disabled, existing vertex group names determine which bones are evaluated, reducing computational overhead. Removing unused groups is beneficial, especially when the mesh is used as a constraint target.

[Related references](INDEX.md).
