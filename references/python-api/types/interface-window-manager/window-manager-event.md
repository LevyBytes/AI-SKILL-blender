# bpy.types.WindowManager: event_timer_add, event_timer_remove

event_timer_add ( time_step , * , window = None )

Add a timer to the given window, to generate periodic 'TIMER' events

Parameters :

- time_step ( float ) – Time Step, Interval in seconds between timer events (in [0, inf])

- window (Window) – Window to attach the timer to, or None (optional)

Return type :

Timer
event_timer_remove ( timer )

event_timer_remove

Parameters :

timer (Timer) – (never None)

[Related references](INDEX.md).
