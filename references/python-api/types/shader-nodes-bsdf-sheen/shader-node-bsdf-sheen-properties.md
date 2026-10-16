# bpy.types.ShaderNodeBsdfSheen: properties

## ShaderNodeBsdfSheen(ShaderNode)

### ShaderNodeBsdfSheen(ShaderNode) 

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeBsdfSheen ( ShaderNode ) 

A reflection model suited to fabrics like cloth.
On its own it has limited value; it is usually layered over another shader such as a Diffuse Shader
distribution 

Shading model used for the sheen effect (default 'ASHIKHMIN' )

- ASHIKHMIN
Ashikhmin – The classic Ashikhmin velvet formulation (legacy model).

- MICROFIBER
Microfiber – A microflake formulation accounting for repeated scattering among fibers aligned to the normal.

Type :

Literal[‘ASHIKHMIN’, ‘MICROFIBER’]

[Related references](INDEX.md).
