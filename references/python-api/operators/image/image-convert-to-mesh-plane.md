# bpy.ops.image.convert_to_mesh_plane

bpy.ops.image.convert_to_mesh_plane ( * , interpolation = 'Linear' , extension = 'CLIP' , use_auto_refresh = True , relative = True , shader = 'PRINCIPLED' , emit_strength = 1.0 , use_transparency = True , render_method = 'DITHERED' , use_backface_culling = False , show_transparent_back = True , overwrite_material = True , name_from = 'OBJECT' , delete_ref = True )
Transform active reference images into textured plane geometry

Parameters:
- interpolation ( Literal [ 'Linear' , 'Closest' , 'Cubic' , 'Smart' ] ) – Interpolation, How pixels are interpolated (optional)
- Linear: Linear interpolation
- Closest: No interpolation (nearest texel)
- Cubic: Cubic interpolation
- Smart: Bicubic magnification, bilinear otherwise (OSL only)
- extension ( Literal [ 'CLIP' , 'EXTEND' , 'REPEAT' ] ) – Extension, Behaviour at image edges (optional)
- CLIP: Truncate at edge and make surrounding transparent
- EXTEND: Extend edge pixels across boundary
- REPEAT: Tile the image horizontally and vertically
- use_auto_refresh ( bool ) – Auto Refresh, Rerender image on every frame change (optional)
- relative ( bool ) – Relative Paths, Store file paths as relative (optional)
- shader ( Literal [ 'PRINCIPLED' , 'SHADELESS' , 'EMISSION' ] ) – Shader, Which material shader to apply (optional)
- PRINCIPLED: Use principled shader
- SHADELESS: Visible to camera and reflections only
- EMISSION: Use emission shader
- emit_strength ( float ) – Emission Strength, Radiance magnitude (in [0, inf], optional)
- use_transparency ( bool ) – Use Alpha, Employ alpha for blending (optional)
- render_method ( Literal [ 'DITHERED' , 'BLENDED' ] ) – Render Method, (optional)
- DITHERED: Use hash-based opacity with pass/raytracing compatibility (deferred rendering)
- BLENDED: Colored transparency (incompatible with passes/raytracing, forward rendering)
- use_backface_culling ( bool ) – Backface Culling, Hide rear-facing surface (optional)
- show_transparent_back ( bool ) – Show Backface, Render stacked transparent layers (may create sorting issues) (optional)
- overwrite_material ( bool ) – Overwrite Material, Swap existing material with matching title (optional)
- name_from ( Literal [ 'OBJECT' , 'IMAGE' ] ) – Name After, What to name the new plane and material (optional)
- OBJECT: Use object name with suffix
- IMAGE: Use image name
- delete_ref ( bool ) – Delete Reference Object, Discard the image reference once plane is created (optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

File:
startup/bl_operators/image_as_planes.py:1133

[Related references](INDEX.md).
