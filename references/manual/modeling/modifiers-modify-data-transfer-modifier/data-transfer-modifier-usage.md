# Data Transfer Modifier: Usage

## Data Transfer Modifier

### Data Transfer Modifier

Certain categories of data, UV maps, color attributes, custom normals, and the like, get copied from one outside mesh onto the modified mesh by the Data Transfer modifier.

Working through the modified mesh element by element (vertex, edge, or face), the modifier hunts down one or several matching elements over in the source mesh and then interpolates across the values those source elements hold.

Transferring a UV map from a low resolution mesh to a high resolution one
using interpolation.

See also

Transfer Mesh Data Operator

### Usage

- Pick the Source mesh whose data you want to copy.

- Should the source and modified meshes not sit on top of one another in world space,
clear Object Transform (the axes icon beside the source mesh).

- Pick which kind of data to copy (vertex groups, UV maps, and so on).

- To copy just one particular vertex group, UV map, or similar, choose it under Layer Selection .

- If the vertex groups or similar you want to copy aren't yet present on the modified mesh,
hit Generate Data Layers to make them.

[Related references](INDEX.md).
