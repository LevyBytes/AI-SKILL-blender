# bmesh.types.BMLayerAccessVert

class bmesh.types. BMLayerAccessVert
Exposes custom-data layer attributes.
bool
A generic boolean custom-data layer.
Type: bmesh.types.BMLayerCollection[bool]
color
A generic 8-bit-precision RGBA color custom-data layer.
Type: bmesh.types.BMLayerCollection[mathutils.Vector]
deform
Vertex deform weight bmesh.types.BMDeformVert (TODO).
Type: bmesh.types.BMLayerCollection[bmesh.types.BMDeformVert]
float
A generic float custom-data layer.
Type: bmesh.types.BMLayerCollection[float]
float_color
A generic float-precision RGBA color custom-data layer.
Type: bmesh.types.BMLayerCollection[mathutils.Vector]
float_vector
A generic float-precision 3D vector custom-data layer.
Type: bmesh.types.BMLayerCollection[mathutils.Vector]
int
A generic int custom-data layer.
Type: bmesh.types.BMLayerCollection[int]
shape

Vertex shape-key absolute location (as a 3D Vector).
Type: bmesh.types.BMLayerCollection[mathutils.Vector]
skin
Accessor for the skin layer.
Type: bmesh.types.BMLayerCollection[ bmesh.types.BMVertSkin ]
string
A generic string custom-data layer (exposed as bytes, 255 max length).
Type: bmesh.types.BMLayerCollection[bytes]

[Related references](INDEX.md).
