# Graph View

## Graph View

Graph View displays tracking motion and error via colored curves.

Red and green lines show tracker velocity per frame (green = vertical, red = horizontal); first frames always zero.

Blue line (clickable film strip output) displays average per-frame error; post-solve only, non-editable. This line should be flat and close to zero—peaks reveal inaccurate tracking regions.

Out-of-range frames darken.

Graph View display.

Header

Only Show Selected
Displays selected-tracker graph.

Display Hidden
Displays hidden-object channels.

Show Frames
Visualizes per-frame average reprojection error of all active-object tracks.

Show Tracks Motion
Shows X/Y velocity curves.

Show Tracks Error
Shows per-frame reprojection error.

Usage

Curves reveal whether particular trackers deviate from the average. Spikes typically indicate tracking error.

Manual curve editing: select a point, drag or delete—this modifies the corresponding tracker on that frame.

Lock to Selection L
Anchors view to selected markers during playback.

[Related references](INDEX.md).
