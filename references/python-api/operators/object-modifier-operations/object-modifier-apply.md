# bpy.ops.object.modifier_apply

bpy.ops.object. modifier_apply ( * , modifier = '' , report = False , merge_customdata = True , single_user = False , all_keyframes = False , use_selected_objects = False ) 

Lock a modifier into the geometry and take it off the stack

Parameters :

- modifier ( str ) – Modifier, Name of the modifier to edit (optional, never None)

- report ( bool ) – Report, Issue a message window after the procedure finishes (optional)

- merge_customdata ( bool ) – Merge UVs, For mesh objects, unify UV locations that reference the same vertex to reduce floating-point artifacts (optional)

- single_user ( bool ) – Make Data Single User, Break any shared references in the object's data if necessary (optional)

- all_keyframes ( bool ) – Apply to all keyframes, For Grease Pencil objects, apply the modifier to every keyframe (optional)

- use_selected_objects ( bool ) – Selected Objects, Affect all selected objects instead of just the active object (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
