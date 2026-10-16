# bpy.types.GeometryNodeSetMeshNormal: properties

## GeometryNodeSetMeshNormal(GeometryNode)

### GeometryNodeSetMeshNormal(GeometryNode) 

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeSetMeshNormal ( GeometryNode ) 

Records a normal vector against each element of a mesh.
domain 

The attribute domain where free custom normals get kept (default 'POINT' )

Type :

Literal[Attribute Domain Only Mesh No Edge Items]
mode 

How custom normal data is held (default 'SHARPNESS' )

- SHARPNESS
Sharpness – Keeps a per-face or per-edge sharpness value, working much like the “Shade Smooth” and “Shade Flat” operators..

- FREE
Free – Holds custom normals as plain vectors expressed in the mesh's local space; these are not guaranteed to refresh on their own when the mesh is later deformed..

- `TANGENT_SPACE`
Tangent Space – Holds normals within a custom transformation space that follows deformation. It runs slower, yet tends to behave better when later operations alter the mesh without dealing with normals directly..

Type :

Literal[‘SHARPNESS’, ‘FREE’, ‘`TANGENT_SPACE`’]

[Related references](INDEX.md).
