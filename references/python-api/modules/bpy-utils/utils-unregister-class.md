# bpy.utils: bpy.utils. unregister_class ( cls )

bpy.utils. unregister_class ( cls ) 

Remove the Python class from Blender.

Parameters :

cls (type[bpy.types.Panel | bpy.types.UIList | bpy.types.Menu | bpy.types.Header | bpy.types.Operator | bpy.types.KeyingSetInfo | bpy.types.RenderEngine | bpy.types.AssetShelf | bpy.types.FileHandler | bpy.types.PropertyGroup | bpy.types.AddonPreferences | bpy.types.NodeTree | bpy.types.Node | bpy.types.NodeSocket | bpy.types.Gizmo | bpy.types.GizmoGroup]) – Blender type class,
see bpy.utils.register_class() for classes which can
be registered.

Note

An unregister class method on the class, if present, runs ahead of unregistration.

[Related references](INDEX.md).
