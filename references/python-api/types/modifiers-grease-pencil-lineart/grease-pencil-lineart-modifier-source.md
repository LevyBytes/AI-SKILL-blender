# bpy.types.GreasePencilLineartModifier: source_camera, source_collection, source_object, source_type, source_vertex_group

source_camera

Use the named camera object when generating Line Art strokes

Type :

Object
source_collection

Build strokes from the objects within this collection

Type :

Collection
source_object

Build strokes from this object

Type :

Object
source_type

Line Art stroke source type (default 'COLLECTION' )

Type :

Literal[‘COLLECTION’, ‘OBJECT’, ‘SCENE’]
source_vertex_group

Match against the start of vertex group names on mesh objects; an empty value matches everything (default “”, never None)

Type :

str

[Related references](INDEX.md).
