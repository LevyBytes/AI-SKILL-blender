# bpy.types.RenderEngine: begin_result

begin_result ( x , y , w , h , * , layer = '' , view = '' ) 

Create render result to write linear floating-point render layers and passes

Parameters :

- x ( int ) – X, (in [0, inf])

- y ( int ) – Y, (in [0, inf])

- w ( int ) – Width, (in [0, inf])

- h ( int ) – Height, (in [0, inf])

- layer ( str ) – Layer, Single layer to get render result for (optional, never None)

- view ( str ) – View, Single view to get render result for (optional, never None)

Returns :

Result

Return type :

RenderResult

[Related references](INDEX.md).
