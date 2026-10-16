# Solidify Modifier

## Solidify Modifier

This modifier adds thickness or depth to any mesh surface, converting surfaces into shells.

Mode: Simple extrudes geometry directly but fails on edges with more than two adjacent faces. Important: when adjacent face normals do not point in the same general direction, Simple mode cannot solidify the boundary; recalculate normals or avoid one-sided surfaces like Möbius strips.

Complex handles all geometric situations, including Möbius strips, Klein bottles, and architectural layouts, guaranteeing manifold output but running slower. Recommended for special cases only.

Thickness Mode (Complex): Fixed maintains constant distance to original vertices (like Simple without Even Thickness), Even adjusts for sharp corners similar to Simple with Even Thickness and High Quality Normals (may fail with 3+ faces), Constraints provides advanced thickness solving (guaranteed optimal for 3 faces, approximate beyond).

Boundary (Complex): None applies no fix (stable results), Round adjusts inward-facing boundaries (like a hole in an egg), Flat creates flat planar openings (like a cut sphere).

Thickness specifies the solid depth. Important: calculated using local vertex coordinates, so non-uniform scale causes varying thickness; Apply or Clear the scale to fix.

Offset positions solidified output from -1 to 1 relative to the original mesh (0.0 centers it).

Even Thickness (Simple) maintains thickness by adjusting for sharp corners; sometimes improves quality but increases computation.

Merge Threshold (Complex) merges degenerated geometry within this distance.

Rim – Fill creates edge loops and faces between inner and outer surfaces on face edges (slow; disable when unnecessary).

Only Rim (Simple) leaves only extruded surface and perpendicular rim, (Complex) leaves only the rim.

Vertex Group weights multiplied onto thickness; lower weights produce less thick geometry. Vertices outside the group have zero weight. Invert reverses weights.

Factor controls weight influence (0.0 = zero weight has no thickness, 0.5 = half thickness, 1.0 = weights ignored).

Flat Faces (Complex) uses minimum vertex weight to keep new faces parallel to originals; slow, disable if unused.

Flip Normals reverses all geometry normals.

High Quality Normals (Simple) calculates normals for more even thickness; sometimes improves quality but increases computation.

Material Offset selects a material slot for new geometry as an offset from the original (0 = same, 1 = next slot, -2 = two slots back). Values clamp to available slots.

Rim assigns a separate material to rim faces.

Inner/Outer/Rim (Simple) set creases on interior, exterior, and rim edges respectively.

Bevel Convex adds bevel weight to outside edges.

Clamp prevents self-intersection by clamping offsets based on shortest adjacent edge length (0 to 2).

Angle Clamp includes geometric angles in clamping calculations, not just lengths.

Shell and Rim Vertex Groups weight generated geometry for selective modifier application.

Known limitations: Even Thickness is approximate and not guaranteed to be exact, especially for vertices with 3+ faces. Maintaining precise wall thickness requires adding/removing faces (not performed by this modifier). Complex mode with constraints thickness provides the best approximation but is still not guaranteed perfect.

Rim Vertex Group weights generated rim geometry, allowing other modifiers to affect only rim geometry via their vertex group influence settings.

Known limitations on Even Thickness: the modifier's Even Thickness and High Quality Normals produce good results, but final wall thickness is approximate and may vary with mesh topology, especially at vertices with more than three adjacent faces.

Preserving exact wall thickness everywhere would require adding or removing faces during solidification, a complexity this modifier avoids. Complex mode with Constraints thickness mode offers the best solution but still cannot guarantee perfection in all cases.

[Related references](INDEX.md).
