# bpy.types.RenderEngine: bl_idname, bl_label, bl_use_custom_freestyle, bl_use_eevee_viewport, bl_use_gpu_context, bl_use_image_save, bl_use_materialx, bl_use_postprocess, bl_use_preview, bl_use_shading_nodes_custom, bl_use_spherical_stereo, bl_use_stereo_viewport

bl_idname 

(default “”, never None)

Type :

str
bl_label 

(default “”, never None)

Type :

str
bl_use_custom_freestyle 

Takes care of freestyle rendering itself rather than passing it on to EEVEE (default False)

Type :

bool
bl_use_eevee_viewport 

Relies on EEVEE for viewport shading while in Material Preview mode (default False)

Type :

bool
bl_use_gpu_context 

Turn on an OpenGL context for the render method, intended for engines that render with OpenGL (default False)

Type :

bool
bl_use_image_save 

Write images/movies to disk during an animation render. Turning saving off is only allowed when bl_use_postprocess is likewise off. (default True)

Type :

bool
bl_use_materialx 

Rely on MaterialX when exporting materials to Hydra (default False)

Type :

bool
bl_use_postprocess 

Run compositing over the render results (default False)

Type :

bool
bl_use_preview 

The render engine can be used to render material, light, and world previews (default False)

Type :

bool
bl_use_shading_nodes_custom 

Keep Cycles and EEVEE shading nodes out of the node editor interface so that separate nodes can take their place (default True)

Type :

bool
bl_use_spherical_stereo 

Handle spherical stereo camera models (default False)

Type :

bool
bl_use_stereo_viewport 

Handle stereo 3D viewport rendering (default False)

Type :

bool

[Related references](INDEX.md).
