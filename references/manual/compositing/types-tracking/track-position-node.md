# Track Position Node

## Track Position Node

The Track Position node feeds a tracking marker's information into the Compositor. Inputs: Mode, which marker position to output — Absolute (a marker's absolute position), Relative Start (positions relative to the track's first marker), Relative Frame (positions relative to a given Frame's markers), or Absolute Frame (absolute positions at a given Frame). Properties: Movie Clip (the clip to use; see the Data-Block Menu), Tracking Object (the camera object to read track info from), and Track (the track name to read from). Outputs: X/Y (the marker's location) and Speed (its velocity in pixels per frame, usable to fake motion blur by connecting it to the Vector Blur Node).

[Related references](INDEX.md).
