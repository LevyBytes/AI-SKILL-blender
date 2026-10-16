# UV Tangent Node

## UV Tangent Node

UV Tangent Node

Generates tangent vectors from a UV map. Unit-length, on-surface vectors point along increasing U. Uses: normal mapping, anisotropy.

Exact or approximate computation, trading precision vs. performance.

Inputs
Method: Algorithm for tangent computation.
  Exact: MikkTSpace algorithm, consistent with Blender's shading and exports. Aligns with normal map space.
  Fast: Approximate, interpolates across matching UV corners. Similar results, lower cost, less consistent on complex surfaces. Cross with normal for exact alignment.
UV: Map for tangent calculation. Determines orientation across the surface.

Outputs
Tangent: Tangent vector from the UV map. Normalized field on the surface, points along increasing U. Combine with normals and bitangents for tangent space basis.

[Related references](INDEX.md).
