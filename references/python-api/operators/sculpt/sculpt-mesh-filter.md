# bpy.ops.sculpt.mesh_filter

bpy.ops.sculpt. mesh_filter ( * , start_mouse = (0, 0) , area_normal_radius = 0.25 , strength = 1.0 , iteration_count = 1 , event_history = None , type = 'INFLATE' , deform_axis = {'X', 'Y', 'Z'} , orientation = 'LOCAL' , surface_smooth_shape_preservation = 0.5 , surface_smooth_current_vertex = 0.5 , sharpen_smooth_ratio = 0.35 , sharpen_intensify_detail_strength = 0.0 , sharpen_curvature_smooth_iterations = 0 )

Enact a transformation to adjust the present surface

Parameters :

- start_mouse ( Sequence [ int ] ) – Starting Mouse, (array of 2 items, in [0, 16384], optional)

- area_normal_radius ( float ) – Normal Radius, Span for computing surface orientation when clicked, measured as a share of brush radius(in [0.001, 5], optional)

- strength ( float ) – Strength, How much the filter affects the surface (in [-10, 10], optional)

- iteration_count ( int ) – Repeat, How many times to execute the filter (in [1, 10000], optional)

- event_history ( bpy_prop_collection [ OperatorStrokeElement ]) – (optional)

- type ( Literal [ 'SMOOTH' , 'SCALE' , 'INFLATE' , 'SPHERE' , 'RANDOM' , 'RELAX' , '`RELAX_FACE_SETS`' , '`SURFACE_SMOOTH`' , 'SHARPEN' , '`ENHANCE_DETAILS`' , '`ERASE_DISPLACEMENT`' ] ) – Filter Type, Transformation that will be applied to the surface (optional)

- SMOOTH
Smooth – Smooth mesh.

- SCALE
Scale – Scale mesh.

- INFLATE
Inflate – Inflate mesh.

- SPHERE
Sphere – Morph into sphere.

- RANDOM
Random – Randomize vertex positions.

- RELAX
Relax – Relax mesh.

- `RELAX_FACE_SETS`
Relax Face Sets – Smooth the edges of all the face sets.

- `SURFACE_SMOOTH`
Surface Smooth – Smooth the surface of the mesh, preserving the volume.

- SHARPEN
Sharpen – Sharpen the cavities of the mesh.

- `ENHANCE_DETAILS`
Enhance Details – Enhance the high frequency surface detail.

- `ERASE_DISPLACEMENT`
Erase Displacement – Deletes the displacement of the Multires Modifier.

- deform_axis ( set [ Literal [ 'X' , 'Y' , 'Z' ] ] ) – Deform Axis, Which axis receives the deformation (optional)

- X
X – Deform in the X axis.

- Y
Y – Deform in the Y axis.

- Z
Z – Deform in the Z axis.

- orientation ( Literal [ 'LOCAL' , 'WORLD' , 'VIEW' ] ) – Orientation, Frame of reference used to constrain the filter displacement (optional)

- LOCAL
Local – Use the local axis to limit the displacement.

- WORLD
World – Use the global axis to limit the displacement.

- VIEW
View – Use the view axis to limit the displacement.

- surface_smooth_shape_preservation ( float ) – Shape Preservation, What amount of the base form remains when smoothing (in [0, 1], optional)

- surface_smooth_current_vertex ( float ) – Per Vertex Displacement, The amount the position of every individual vertex influences the result (in [0, 1], optional)

- sharpen_smooth_ratio ( float ) – Smooth Ratio, What amount of smoothing occurs on polished zones (in [0, 1], optional)

- sharpen_intensify_detail_strength ( float ) – Intensify Details, How much surface indentations and ridges are heightened (in [0, 10], optional)

- sharpen_curvature_smooth_iterations ( int ) – Curvature Smooth Iterations, How much the final shape is softened, disregarding surface texture (in [0, 10], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
