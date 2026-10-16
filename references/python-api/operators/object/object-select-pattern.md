# bpy.ops.object.select_pattern

bpy.ops.object. select_pattern ( * , pattern = '*' , case_sensitive = False , extend = True ) 

Highlight objects matching a title pattern

Parameters :

- pattern ( str ) – Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards (optional, never None)

- case_sensitive ( bool ) – Case Sensitive, Perform case-aware matching (optional)

- extend ( bool ) – Extend, Add to the existing selection instead of replacing it (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object.py:45

[Related references](INDEX.md).
