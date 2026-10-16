# bpy.types.SequencerTimelineOverlay: properties

show_fcurves

Draw the opacity or volume curve of strips (default False)

Type :

bool
show_grid

Draw vertical grid lines (default False)

Type :

bool
show_strip_duration

(default False)

Type :

bool
show_strip_name

(default False)

Type :

bool
show_strip_offset

Draw the in and out offsets of strips (default False)

Type :

bool
show_strip_retiming

Draw retiming keys over the top of strips (default False)

Type :

bool
show_strip_source

Draw the source file path, or the source data-block name (default False)

Type :

bool
show_strip_tag_color

Draw the color tags of strips in the sequencer (default False)

Type :

bool
show_thumbnails

Draw thumbnail previews on strips (default False)

Type :

bool
waveform_display_style

The way waveforms get drawn (default '`FULL_WAVEFORMS`' )

- `FULL_WAVEFORMS`
Full – Draw the complete waveform.

- `HALF_WAVEFORMS`
Half – Draw only the top half of the absolute-value waveform.

Type :

Literal[‘`FULL_WAVEFORMS`’, ‘`HALF_WAVEFORMS`’]
waveform_display_type

The way waveforms get drawn (default '`DEFAULT_WAVEFORMS`' )

- `ALL_WAVEFORMS`
On – Draw waveforms across every sound strip.

- `DEFAULT_WAVEFORMS`
Strip – Draw waveforms based on each strip's own setting.

- `NO_WAVEFORMS`
Off – Suppress waveforms on all sound strips.

Type :

Literal[‘`ALL_WAVEFORMS`’, ‘`DEFAULT_WAVEFORMS`’, ‘`NO_WAVEFORMS`’]

[Related references](INDEX.md).
