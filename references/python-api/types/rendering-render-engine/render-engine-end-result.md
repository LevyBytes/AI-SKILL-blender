# bpy.types.RenderEngine: end_result

end_result ( result , * , cancel = False , highlight = False , do_merge_results = False ) 

All pixels in the render result have been set and are final

Parameters :

- result (RenderResult) – Result

- cancel ( bool ) – Cancel, Don’t mark tile as done, don’t merge results unless forced (optional)

- highlight ( bool ) – Highlight, Don’t mark tile as done yet (optional)

- do_merge_results ( bool ) – Merge Results, Merge results even if cancel=true (optional)

[Related references](INDEX.md).
