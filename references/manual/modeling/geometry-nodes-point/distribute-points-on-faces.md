# Distribute Points on Faces

## Distribute Points on Faces

Distribute Points on Faces

Places points on the input surface. Point, corner, and polygon attributes transfer to generated points, including vertex weights and UV maps. A stable ID in the id attribute identifies each point. When the mesh deforms or density changes, values stay consistent. Normal and Rotation outputs also include attributes.

Inputs
Mesh: Standard geometry input. Must contain faces.
Selection: Which face corners participate in distribution.
Distance Min: Minimum distance between points. Poisson Disk only. Default zero = Random mode behavior.
Density Max: Point density (points per square meter). Multiplies by Density input. Poisson Disk only. Capped by Distance Min—if density exceeds what distance allows, no new points add.
Density: Points per square meter per face. Multiplied by Density Attribute. In Poisson Disk mode, multiplied by Density Max.
Seed: Random seed for generating points.

Properties
Distribution Method:
  Random: Random surface placement. Fastest.
  Poisson Disk: Random with minimum distance constraint.
Legacy Normal: Uses smooth and custom normals by default. Older behavior (true normals only) available in Sidebar.

Outputs
Points: Generated points with named attributes copied from the mesh.
Normal: The normal of the triangle where each point scatters.
Rotation: XYZ Euler rotation built from the normal. Also buildable via Euler to Rotation Node. Z axis is arbitrary (normal has insufficient info for all three axes).

[Related references](INDEX.md).
