# bpy.types.ShaderNodeScript: properties

## ShaderNodeScript(ShaderNode)

### ShaderNodeScript(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeScript ( ShaderNode )

Builds an OSL shader from a text data-block or an external file.
Note: OSL shaders are not supported on all GPU backends
bytecode

Compile bytecode for shader script node (default “”, never None)

Type :

str
bytecode_hash

Hash of compile bytecode, for quick equality checking (default “”, never None)

Type :

str
filepath

Shader script path (default “”, never None, blend relative // prefix supported)

Type :

str
mode

(default 'INTERNAL' )

- INTERNAL
Internal – Use internal text data-block.

- EXTERNAL
External – Use external .osl or .oso file.

Type :

Literal[‘INTERNAL’, ‘EXTERNAL’]
script

Internal shader script to define the shader

Type :

Text
use_auto_update

Reloads the shader on its own whenever the external .osl file is changed (external scripts only) (default False)

Type :

bool

[Related references](INDEX.md).
