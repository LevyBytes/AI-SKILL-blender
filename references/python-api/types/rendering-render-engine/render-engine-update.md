# bpy.types.RenderEngine: update, update_script_node, update_render_passes, update_custom_camera, update_result, update_stats, update_progress, update_memory_stats

update ( * , data = None , depsgraph = None ) 

Export scene data for render

Parameters :

- data (BlendData) – (optional)

- depsgraph (Depsgraph) – (optional)
update_script_node ( * , node = None ) 

Compile shader script node

Parameters :

node (Node) – (optional)
update_render_passes ( * , scene = None , renderlayer = None ) 

Update the render passes that will be generated

Parameters :

- scene (Scene) – (optional)

- renderlayer (ViewLayer) – (optional)
update_custom_camera ( * , cam = None ) 

Compile custom camera

Parameters :

cam (Camera) – (optional)
update_result ( result ) 

Signal that pixels have been updated and can be redrawn in the user interface

Parameters :

result (RenderResult) – Result
update_stats ( stats , info ) 

Update and signal to redraw render status text

Parameters :

- stats ( str ) – Stats, (never None)

- info ( str ) – Info, (never None)
update_progress ( progress ) 

Update progress percentage of render

Parameters :

progress ( float ) – Percentage of render that’s done (in [0, 1])
update_memory_stats ( * , memory_used = 0.0 , memory_peak = 0.0 ) 

Update memory usage statistics

Parameters :

- memory_used ( float ) – Current memory usage in megabytes (in [0, inf], optional)

- memory_peak ( float ) – Peak memory usage in megabytes (in [0, inf], optional)

[Related references](INDEX.md).
