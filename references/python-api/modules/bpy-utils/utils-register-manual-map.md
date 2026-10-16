# bpy.utils: bpy.utils. register_manual_map ( manual_hook )

bpy.utils. register_manual_map ( manual_hook ) 

Register a function that supplies manual URL mappings.

Parameters :

manual_hook ( Callable [ [ ] , tuple [ str , list [ tuple [ str , str ] ] ] ] ) – A callable returning (prefix, mapping),
where mapping lists (pattern, url) pairs.

[Related references](INDEX.md).
