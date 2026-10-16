# bpy.app: methods

static bpy.app. help_text ( * , all = False )
Returns the help text as a string.
Parameters: all ( bool ) – Return all arguments, even those which aren't available for the current platform.
Returns: Help text.
Return type: str
static bpy.app. is_job_running ( job_type )
Checks whether a job of the given type is running.
Parameters: job_type ( str ) – job type in Wm Job Type Items.
Returns: Whether a job of the given type is currently running.
Return type: bool
static bpy.app. memory_usage_undo ( )
Gets undo memory-usage information.
Returns: Memory usage of the undo stack in bytes.
Return type: int

[Related references](INDEX.md).
