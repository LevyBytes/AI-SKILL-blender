# bpy.ops.object.bake

bpy.ops.object. bake ( * , type = 'COMBINED' , pass_filter = set() , filepath = '' , width = 512 , height = 512 , margin = 16 , margin_type = 'EXTEND' , use_selected_to_active = False , max_ray_distance = 0.0 , cage_extrusion = 0.0 , cage_object = '' , normal_space = 'TANGENT' , normal_r = '`POS_X`' , normal_g = '`POS_Y`' , normal_b = '`POS_Z`' , target = '`IMAGE_TEXTURES`' , save_mode = 'INTERNAL' , use_clear = False , use_cage = False , use_split_materials = False , use_automatic_name = False , uv_layer = '' )

Process surface appearance information for chosen objects

Parameters :

- type (Literal[Bake Pass Type Items]) – Type, Type of pass to bake, some of them may not be supported by the current render engine (optional)

- pass_filter (set[Literal[Bake Pass Filter Type Items]]) – Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes (optional)

- filepath ( str ) – File Path, Image filepath to use when saving externally (optional, never None)

- width ( int ) – Width, Horizontal dimension of the baking map (external only) (in [1, inf], optional)

- height ( int ) – Height, Vertical dimension of the baking map (external only) (in [1, inf], optional)

- margin ( int ) – Margin, Extends the baked result as a post process filter (in [0, inf], optional)

- margin_type (Literal[Bake Margin Type Items]) – Margin Type, Which algorithm to use to generate the margin (optional)

- use_selected_to_active ( bool ) – Selected to Active, Bake shading on the surface of selected objects to the active object (optional)

- max_ray_distance ( float ) – Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit (in [0, inf], optional)

- cage_extrusion ( float ) – Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes (in [0, inf], optional)

- cage_object ( str ) – Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion (optional, never None)

- normal_space (Literal[Normal Space Items]) – Normal Space, Choose normal space for baking (optional)

- normal_r (Literal[Normal Swizzle Items]) – R, Axis to bake in red channel (optional)

- normal_g (Literal[Normal Swizzle Items]) – G, Axis to bake in green channel (optional)

- normal_b (Literal[Normal Swizzle Items]) – B, Axis to bake in blue channel (optional)

- target (Literal[Bake Target Items]) – Target, Where to output the baked map (optional)

- save_mode (Literal[Bake Save Mode Items]) – Save Mode, Where to save baked image textures (optional)

- use_clear ( bool ) – Clear, Clear images before baking (only for internal saving) (optional)

- use_cage ( bool ) – Cage, Cast rays to active object from a cage (optional)

- use_split_materials ( bool ) – Split Materials, Split baked maps per material, using material name in output file (external only) (optional)

- use_automatic_name ( bool ) – Automatic Name, Automatically name the output file with the pass type (optional)

- uv_layer ( str ) – UV Layer, UV layer to override active (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
