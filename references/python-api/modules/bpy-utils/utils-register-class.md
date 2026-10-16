# bpy.utils: bpy.utils. register_class ( cls )

bpy.utils. register_class ( cls ) 

Make a subclass of one of Blender's type classes known to Blender.

Parameters :

cls (type[bpy.types.Panel | bpy.types.UIList | bpy.types.Menu | bpy.types.Header | bpy.types.Operator | bpy.types.KeyingSetInfo | bpy.types.RenderEngine | bpy.types.AssetShelf | bpy.types.FileHandler | bpy.types.PropertyGroup | bpy.types.AddonPreferences | bpy.types.NodeTree | bpy.types.Node | bpy.types.NodeSocket | bpy.types.Gizmo | bpy.types.GizmoGroup]) – Registerable Blender class type.

Raises :

ValueError – if the class is not a subclass of a registerable blender class.

Note

A register class method on the class, if present, runs ahead of registration.

[Related references](INDEX.md).
