# bpy.types.Object: instance_collection, instance_faces_scale, instance_type

instance_collection 

Create an instance of an existing collection

Type :

Collection
instance_faces_scale 

Scale factor for the per-face instance objects (in [0.001, 10000], default 1.0)

Type :

float
instance_type 

When set, which instancing method the object applies (default 'NONE' )

- NONE
None.

- VERTS
Vertices – Instantiate child objects on all vertices.

- FACES
Faces – Instantiate child objects on all faces.

- COLLECTION
Collection – Enable collection instancing.

Type :

Literal[‘NONE’, ‘VERTS’, ‘FACES’, ‘COLLECTION’]

[Related references](INDEX.md).
