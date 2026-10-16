# freestyle.types.Nature

class freestyle.types. Nature 

Class hierarchy: int > Nature

The range of possible natures for the 0D and 1D elements of the ViewMap.

Vertex natures:

- Nature.POINT: True for any 0D element.

- Nature.`S_VERTEX`: True for SVertex.

- Nature.`VIEW_VERTEX`: True for ViewVertex.

- Nature.`NON_T_VERTEX`: True for NonTVertex.

- Nature.`T_VERTEX`: True for TVertex.

- Nature.CUSP: True for CUSP.

Edge natures:

- Nature.`NO_FEATURE`: True for non feature edges (always false for 1D
elements of the ViewMap).

- Nature.SILHOUETTE: True for silhouettes.

- Nature.BORDER: True for borders.

- Nature.CREASE: True for creases.

- Nature.RIDGE: True for ridges.

- Nature.VALLEY: True for valleys.

- Nature.`SUGGESTIVE_CONTOUR`: True for suggestive contours.

- Nature.`MATERIAL_BOUNDARY`: True for edges at material boundaries.

- Nature.`EDGE_MARK`: True for edges having user-defined edge marks.

[Related references](INDEX.md).
