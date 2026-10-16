# bmesh.utils: bmesh.utils. uv_select_check ( bm , / , * , sync = True , flush = False , contiguous = False )

bmesh.utils. uv_select_check ( bm , / , * , sync = True , flush = False , contiguous = False )
Checks the UV selection state for consistency issues.
Parameters:
- bm (bmesh.types.BMesh) – The BMesh to check.
- sync ( bool ) – Check the data is properly synchronized between UV's and the underlying mesh. Failure to synchronize with the mesh selection may cause tools not to behave properly.
- flush ( bool ) – Check the selection has been properly flushed between elements (based on the current bmesh.types.BMesh.select_mode).
- contiguous ( bool ) – Check connected UV's and edges have a matching selection state.
Returns: An error dictionary, or None when no errors are found.
Return type: dict[str, int] | None

[Related references](INDEX.md).
