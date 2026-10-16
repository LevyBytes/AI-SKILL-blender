# bpy.types.WeightedNormalModifier: properties

## WeightedNormalModifier(Modifier)

### WeightedNormalModifier(Modifier)

base classes — bpy_struct, Modifier
class bpy.types. WeightedNormalModifier ( Modifier )
invert_vertex_group

Flip the vertex group's influence (default False)

Type :

bool
keep_sharp

Preserve sharp edges as found for default custom normals, rather than assigning one weighted normal per vertex (default False)

Type :

bool
mode

Which weighted vertex-normal mode to apply (default '`FACE_AREA`' )

- `FACE_AREA`
Face Area – Weight normals by the area of each face.

- `CORNER_ANGLE`
Corner Angle – Weight normals by the angle at each corner.

- `FACE_AREA_WITH_ANGLE`
Face Area & Angle – Weight normals by face area and corner angle together.

Type :

Literal['`FACE_AREA`', '`CORNER_ANGLE`', '`FACE_AREA_WITH_ANGLE`']
thresh

How close two weights must be to count as equal (in [0, 10], default 0.01)

Type :

float
use_face_influence

Factor each face's influence into the weighting (default False)

Type :

bool
vertex_group

Vertex group name used to pick the affected areas (default "", never None)

Type :

str
weight

Correction factor applied to face weights; 50 is neutral, lower values favor weak faces and higher values favor strong faces (in [1, 100], default 50)

Type :

int

[Related references](INDEX.md).
