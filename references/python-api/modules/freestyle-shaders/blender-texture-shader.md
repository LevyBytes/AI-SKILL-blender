# freestyle.shaders.BlenderTextureShader

class freestyle.shaders. BlenderTextureShader 

Class hierarchy: freestyle.types.StrokeShader > BlenderTextureShader

[Texture shader]
__init__ ( texture ) 

Builds a BlenderTextureShader object.

Parameters :

texture (bpy.types.LineStyleTextureSlot | bpy.types.ShaderNodeTree) – A line style texture slot or a shader node tree to define a set of textures.
shade ( stroke ) 

Attaches a blender texture slot to the stroke's shading so that marks can be simulated.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
