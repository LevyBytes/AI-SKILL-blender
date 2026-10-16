# bpy.types.WindowManager: progress_begin, progress_update, progress_end

progress_begin ( min , max )

Start progress report

Parameters :

- min ( float ) – min, any value in range [0,9999] (in [-inf, inf])

- max ( float ) – max, any value in range [min+1,9998] (in [-inf, inf])
progress_update ( value )

Update the progress feedback

Parameters :

value ( float ) – value, Any value between min and max as set in progress_begin() (in [-inf, inf])
progress_end ( )

Terminate progress report

[Related references](INDEX.md).
