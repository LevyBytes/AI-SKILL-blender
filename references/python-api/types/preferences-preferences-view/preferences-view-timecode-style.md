# bpy.types.PreferencesView: timecode_style

timecode_style 

How a timecode is shown when timing is not given as frames (default 'MINIMAL' )

- MINIMAL
Minimal Info – Most compact representation, uses ‘+’ as separator for sub-second frame numbers, with left and right truncation of the timecode as necessary.

- SMPTE
SMPTE (Full) – Full SMPTE timecode (format is HH:MM:SS:FF).

- `SMPTE_COMPACT`
SMPTE (Compact) – SMPTE timecode showing minutes, seconds, and frames only - hours are also shown if necessary, but not by default.

- MILLISECONDS
Compact with Decimals – Similar to SMPTE (Compact), except that the decimal part of the second is shown instead of frames.

- `SECONDS_ONLY`
Only Seconds – Direct conversion of frame numbers to seconds.

Type :

Literal[‘MINIMAL’, ‘SMPTE’, ‘`SMPTE_COMPACT`’, ‘MILLISECONDS’, ‘`SECONDS_ONLY`’]

[Related references](INDEX.md).
