# bpy.types.RenderEngine: bake

bake ( depsgraph , object , pass_type , pass_filter , width , height ) 

Bake passes

Parameters :

- pass_type (Literal[Bake Pass Type Items]) – Pass, Pass to bake

- pass_filter ( int ) – Pass Filter, Filter to combined, diffuse, glossy and transmission passes (in [0, inf])

- width ( int ) – Width, Image width (in [0, inf])

- height ( int ) – Height, Image height (in [0, inf])

[Related references](INDEX.md).
