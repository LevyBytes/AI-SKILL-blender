# bpy.utils: bpy.utils. register_tool ( tool_cls , * , after = None , separator = False , group = False )

bpy.utils. register_tool ( tool_cls , * , after = None , separator = False , group = False ) 

Add a tool to the toolbar.

Parameters :

- tool_cls (type[bpy.types.WorkSpaceTool]) – A tool subclass.

- after ( Sequence [ str ] | set [ str ] | None ) – Optional identifiers after which this tool is placed.

- separator ( bool ) – If true, insert a separator ahead of this tool.

- group ( bool ) – If true, start a new nested group of tools.

[Related references](INDEX.md).
