# Physical Properties: Internal Springs, Pressure

### Internal Springs

Springs link surface mesh vertices, affecting only 2D surfaces. For 3D behavior resembling Soft Bodies, enable Internal Springs in the panel header.

Max Spring Creation Length
Upper limit on internal spring length during generation. Connections beyond this separation won't form. Zero = no limit.

Max Creation Diversion
Maximum permitted angle between internal connection and vertex normal direction.

Check Surface Normals
Requires connected points to possess opposite normal orientations.

Tension
Lengthening resistance.

Compression
Condensing resistance.

Vertex Group
A Vertex Group manages Tension and Compression for selected mesh portions and spring intensity.

Max Tension
Highest tension stiffness.

Max Compression
Highest compression stiffness.

### Pressure

Enclosed soft objects (balloons, filled spheres) can be modeled via cloth pressure, treating contents as gas. For incompressible behavior, maximize Pressure Scale without destabilizing. Activate via the Pressure panel header.

Note

Non-manifold meshes work, though pressure leaks through holes, causing drift. Exclude non-manifold portions via Vertex Group.

Pressure
Uniform force always applied. Units are Pressure Scale; negative values simulate inward pressure or collapse.

Custom Volume
Use Target Volume as the starting volume instead of computing from the mesh.

Target Volume
Volume where internal/external pressure equilibrate. Zero disables volume-based pressure adjustment.

Pressure Scale
Background pressure (kPa) balanced at target volume. Higher = stronger resistance to size change.

Fluid Density
Density of interior fluid (kg/liter; use 1 for water), generating hydrostatic gradient (weight). Negative models surrounding buoyancy. No actual fluid motion occurs, so realistic flow dynamics don't manifest, yet the setting helps plausible resting shapes and can add weight to flexible objects, even non-fluids.

Volume isn't preserved without Pressure Scale. Try fluid density × object size × 50 as an initial Pressure Scale to keep volume under 10% change if acceleration stays near standard gravity.

Vertex Group
A Vertex Group specifies mesh portions receiving pressure. Zero weight = no pressure; full weight = max pressure.

Note, faces containing a zero-weight vertex skip Target Volume calculation.

[Related references](INDEX.md).
