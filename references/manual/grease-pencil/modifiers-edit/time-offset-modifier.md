# Time Offset Modifier

## Time Offset Modifier

The Time Offset Modifier shifts Grease Pencil keyframes along the animation timeline. When duplicating Grease Pencil objects, this modifier on duplicated versions can offset animations to achieve more organic appearances. Using this modifier, Grease Pencil ranges can be configured as looping sequences. Looped 2D animation traditionally features characters in motion, billowing smoke, or cascading precipitation. In Fixed Frame mode, the modifier allows individual drawings to appear independent of where the playhead sits on the timeline. This is useful when you want certain graphics to display repeatedly throughout your sequence—such as switching among several predefined mouth positions.

Mode: Regular offsets keyframes in forward playback direction (left to right). Reverse offsets in backward playback (right to left). Fixed Frame displays the frame set by the Frame parameter, which must be animated for onscreen changes during playback. Ping Pong loops animation back and forth. Chain combines the modes sequentially. Repeat sets the number of cycle repeats. Frame Offset is the number of frames to shift from the original keyframes. Scale governs frame playback speed, where 1 matches standard frame rate; positive values speed up, negative ones slow down. Keep Loop repositions the final frame to the animation start to sustain continuity.

Custom Range: When active, animation playback occurs only within specified frame boundaries. Frame Start/End define the range limits.

Influence: See Influence Filters.

[Related references](INDEX.md).
