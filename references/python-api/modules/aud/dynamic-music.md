# aud.DynamicMusic

class aud.DynamicMusic

DynamicMusic handles music playback tied to scene context, managing transitions automatically with customizable options. Default is crossfade, default scene is silent with id 0.
addScene(scene)

Adds a music scene.

Parameters:

scene (Sound) – The music sound.

Returns:

The new scene identifier.

Return type:

int
addTransition(ini, end, transition)

Adds a transition between scenes.

Parameters:

- ini (int) – The starting scene for the transition.

- end (int) – The ending scene for the transition.

- transition (Sound) – The transition sound.

Returns:

false if ini or end don't exist, true otherwise.

Return type:

bool
pause()

Pauses the music scene.

Returns:

Success status.

Return type:

bool
resume()

Resumes music playback.

Returns:

Success status.

Return type:

bool
stop()

Stops the music scene.

Returns:

Success status.

Return type:

bool
fadeTime

Crossfade length in seconds.
position

Music playback position in seconds.
scene

The active music scene.
status

Music playback state: playing, paused, or stopped (invalid).

volume

Music loudness.

[Related references](INDEX.md).
